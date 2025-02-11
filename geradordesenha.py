import string
from random import choice
import customtkinter as ct

ct.set_appearance_mode("Dark")
janela = ct.CTk()
janela.title('Gerador de senha')
janela.geometry('1900x700')

def gerar_senha():
    try:
        tamanho_senha = int(tamanho.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(choice(caracteres) for _ in range(tamanho_senha))
        if tamanho.get():
            senha_text.configure(text=f'Tamanho da senha gerada é: {tamanho_senha}\nsenha : {senha}',font=('Arial', 16))
    except ValueError:
        print(f'Insira uma entrada válida(Numerica)')
texto = ct.CTkLabel(janela, text= f'{' Gerador de Senha ':-^30}',font=('Arial', 14))
texto.place(x = 290, y = 20)


tamanho = ct.CTkEntry(janela,placeholder_text='Tamanho de caracteres da senha: ')
tamanho.place(x = 300, y = 100)


senha_text = ct.CTkLabel(janela, text='')
senha_text.place(x = 250, y = 300)
  
botao_senha = ct.CTkButton(janela, text='Gerar senha',command=gerar_senha)
botao_senha.place(x = 300, y = 200)
janela.mainloop()
