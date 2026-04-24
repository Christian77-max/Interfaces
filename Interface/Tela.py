import customtkinter as ctk

ctk.set_appearance_mode('dark')


#aqui Começa a Janela
janela = ctk.CTk()
janela.geometry('600x400')
janela.resizable(False,False)
janela.title('Sistema De Acesso')
janela.iconbitmap('03.ico')

#Elementos de Dentro Da Janela

titulo = ctk.CTkLabel(janela,
                      text='Sistema de Acesso',
                      text_color='Blue',
                      font=('Verdana',40))
titulo.pack(pady=20)


login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='Digite o Seu Login',
                     border_color='blue')




login.pack()


senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='Digite a sua Senha',
                     border_color='blue',
                     show='🥉'
                     )
senha.pack(pady=20)



botao = ctk.CTkButton(janela,
                      text='Adentrar',
                      width=150,
                      height=40,
                      font=('verdana',20),
                      fg_color='blue',
                      text_color='black')
botao.pack(pady=30)




janela.mainloop()