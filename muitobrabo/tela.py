import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ================= BANCO =================
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("estoque.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            quantidade INTEGER,
            preco REAL
        )
        """)
        self.conn.commit()

    def add(self, nome, qtd, preco):
        self.cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                            (nome, qtd, preco))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, nome, qtd, preco):
        self.cursor.execute("""
        UPDATE produtos SET nome=?, quantidade=?, preco=? WHERE id=?
        """, (nome, qtd, preco, id))
        self.conn.commit()

    def search(self, nome):
        self.cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%' + nome + '%',))
        return self.cursor.fetchall()


# ================= APP =================
class EstoqueApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Sistema de Estoque PRO 🚀")
        self.root.geometry("900x600")
        self.root.configure(bg="#121212")

        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        # Notebook (abas)
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        self.tab_estoque = tk.Frame(self.tabs, bg="#121212")
        self.tab_cadastro = tk.Frame(self.tabs, bg="#121212")

        self.tabs.add(self.tab_estoque, text="Estoque")
        self.tabs.add(self.tab_cadastro, text="Cadastro")

        self.setup_estoque_tab()
        self.setup_cadastro_tab()

    # -------- ABA ESTOQUE --------
    def setup_estoque_tab(self):
        top_frame = tk.Frame(self.tab_estoque, bg="#121212")
        top_frame.pack(fill="x", pady=10)

        tk.Label(top_frame, text="Buscar:", fg="white", bg="#121212").pack(side="left", padx=5)

        self.search_entry = tk.Entry(top_frame)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(top_frame, text="Buscar", command=self.search).pack(side="left", padx=5)
        tk.Button(top_frame, text="Mostrar Todos", command=self.load_data).pack(side="left", padx=5)

        # Tabela
        cols = ("ID", "Nome", "Qtd", "Preço")
        self.tree = ttk.Treeview(self.tab_estoque, columns=cols, show="headings")

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Botões
        btn_frame = tk.Frame(self.tab_estoque, bg="#121212")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Deletar", bg="red", fg="white",
                  command=self.delete_item).pack(side="left", padx=10)

        tk.Button(btn_frame, text="Editar", bg="orange",
                  command=self.load_selected).pack(side="left", padx=10)

    # -------- ABA CADASTRO --------
    def setup_cadastro_tab(self):
        frame = tk.Frame(self.tab_cadastro, bg="#121212")
        frame.pack(pady=50)

        tk.Label(frame, text="Nome", fg="white", bg="#121212").grid(row=0, column=0, pady=5)
        self.nome = tk.Entry(frame)
        self.nome.grid(row=0, column=1)

        tk.Label(frame, text="Quantidade", fg="white", bg="#121212").grid(row=1, column=0)
        self.qtd = tk.Entry(frame)
        self.qtd.grid(row=1, column=1)

        tk.Label(frame, text="Preço", fg="white", bg="#121212").grid(row=2, column=0)
        self.preco = tk.Entry(frame)
        self.preco.grid(row=2, column=1)

        self.btn_add = tk.Button(frame, text="Salvar", bg="green", fg="white",
                                command=self.save_item)
        self.btn_add.grid(row=3, column=0, columnspan=2, pady=10)

    # -------- FUNÇÕES --------
    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for row in self.db.get_all():
            self.tree.insert("", tk.END, values=row)

    def save_item(self):
        nome = self.nome.get()
        qtd = self.qtd.get()
        preco = self.preco.get()

        if not nome or not qtd or not preco:
            messagebox.showerror("Erro", "Preencha tudo!")
            return

        self.db.add(nome, int(qtd), float(preco))
        self.clear_fields()
        self.load_data()

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected)
        self.db.delete(item['values'][0])
        self.load_data()

    def load_selected(self):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected)['values']

        self.nome.delete(0, tk.END)
        self.qtd.delete(0, tk.END)
        self.preco.delete(0, tk.END)

        self.nome.insert(0, item[1])
        self.qtd.insert(0, item[2])
        self.preco.insert(0, item[3])

        self.tabs.select(self.tab_cadastro)

    def search(self):
        termo = self.search_entry.get()

        for i in self.tree.get_children():
            self.tree.delete(i)

        for row in self.db.search(termo):
            self.tree.insert("", tk.END, values=row)

    def clear_fields(self):
        self.nome.delete(0, tk.END)
        self.qtd.delete(0, tk.END)
        self.preco.delete(0, tk.END)


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()