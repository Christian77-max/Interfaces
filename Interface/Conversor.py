import customtkinter as ctk 

janela = ctk.CTk()

janela = ctk.CTk()
janela.title("Conversor de Moedas")
janela.geometry("600x400")
janela.resizable(False, False)

def converter_para_dolar():
    valor_real = float(moeda.get())
    valor_dolar = valor_real / 5.0
    resultado = f"R$ {valor_real:.2f} é equivalente a $ {valor_dolar:.2f}"
    ctk.CTkLabel(janela, text=resultado, font=("Arial", 14)).pack(pady=10)

def converter_para_real():
    valor_dolar = float(moeda.get())
    valor_real = valor_dolar * 5.0
    resultado = f"$ {valor_dolar:.2f} é equivalente a R$ {valor_real:.2f}"
    ctk.CTkLabel(janela, text=resultado, font=("Arial", 14)).pack(pady=10)

titulo = ctk.CTkLabel(janela, 
                      text="Conversor de Moedas", 
                      font=("Arial", 20))
titulo.pack(pady=20)

moeda = ctk.CTkEntry(janela,
                    width=200,
                    height=30,
                    border_color = 'blue',
                    border_width=2, 
                    )
moeda.pack(pady=10)

dolar = ctk.CTkButton(janela,
                     text="Dólar",
                     font=("Arial", 14),
                     width=200,
                     command=converter_para_dolar)

dolar.pack(pady=10)

real = ctk.CTkButton(janela,
                     text="Real",    
                    font=("Arial", 14),
                    width=200,
                     command=converter_para_real)

real.pack(pady=10)

janela.mainloop()
