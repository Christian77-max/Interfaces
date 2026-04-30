import os
import customtkinter as ctk
os.system("cls")

#function -----------

def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    calculo = (d / c) * p
    resultado.configure(text=f"O gasto total da viagem é: R$ {calculo:.2f}")    
    

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("App Viagem")
janela.geometry("640x400")
janela.resizable(False, False)

titulo = ctk.CTkLabel(janela, text_color="blue", text="APP VIAGEM", font=("Arial", 20))
titulo.pack(pady=20)

distancia = ctk.CTkEntry(janela,
                     width=200,
                     height=30,
                      placeholder_text_color = "gray",
                      border_color = "black",
                      
                      placeholder_text="Digite a distância da viagem em KM:")
distancia.pack(pady=20)

consumo = ctk.CTkEntry(janela,
                     width=200,
                     height=30,
                      placeholder_text_color = "gray",
                      border_color = "black",
                      
                      placeholder_text="Digite o consumo do seu veículo:")
consumo.pack(pady=20)

preco = ctk.CTkEntry(janela,
                     width=200,
                     height=30,
                      placeholder_text_color = "gray",
                      border_color = "black",
                      
                      placeholder_text="Digite o preço do combustível:")
preco.pack(pady=20)

button = ctk.CTkButton(janela, 
                       text="Calcular Gasto", width=100, height=30, command=calcular)



button.pack(pady=20)

resultado = ctk.CTkLabel(janela, text_color="blue", text="", font=("Arial", 16))
resultado.pack(pady=20)

janela.mainloop()