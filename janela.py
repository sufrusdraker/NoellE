import json
import os
import tkinter as tk
from core import gerar_resposta  
import threading 
from login import cadastrar_usuario
from login import verificar_usuario
#importar as bibliotecas

usuarios = "usuarios.json"
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "Llama-3.2-3B-Instruct-Q4_0.gguf")
memory_file = os.path.join(current_dir, "memoria.json")
#carregar o modelo da NoellE



def cadastro():
     #função para cadastrar o usuário
    
     email = entry_email.get()
     senha = entry_senha.get()
     
     cadastrar_usuario(email, senha, admin=False)
     

def login():
     #função para verificar o usuário
     email = entry_email.get()
     senha = entry_senha.get()

     verificar_usuario(email, senha)
     


def tela_de_login():
     #criar a janela de login
     global login_window, entry_email, entry_senha
     login_window = tk.Toplevel(root)
     login_window.title("login")
     login_window.geometry("300x200")

     label_email = tk.Label(login_window, text="email: ")
     label_email.pack(pady=5)
     entry_email = tk.Entry(login_window)
     entry_email.pack(pady=5)

     label_senha = tk.Label(login_window, text="senha: ")
     label_senha.pack(pady=5)
     entry_senha = tk.Entry(login_window, show="*")
     entry_senha.pack(pady=5)

     botão_login = tk.Button(login_window, text="entrar", command=login)
     botão_login.pack(pady=5)

     botão_cadastro = tk.Button(login_window, text="cadastrar", command=cadastro)
     botão_cadastro.pack(pady=5)

def fundo():    
        if dark.get() == True:
            root.configure(background="#000000")
            input.config(background="#4f4f4f")
            historico.config(background="#4f4f4f")
            title.config(fg="#dc143c", background="#000000")
            DM.config(fg="#f0f0f0", background="#000000")
        else:   
            root.configure(background="#f0f0f0")
            input.config(background="#c0c0c0")  
            historico.config(background="#c0c0c0")
            title.config(fg="#dc143c", background="#f0f0f0")
            DM.config(fg="#000000", background="#f0f0f0")

def NoellE():
     enviar.config(state="disabled")

     mensagem = input.get()
     historico.config(state="normal")
     historico.insert(tk.END, f"usuario: {mensagem}\n", "usuario")
     historico.config(state="disabled")

     print("tem calma, ainda não quebrou") #debug

     user_input = input.get()
     resposta = gerar_resposta(user_input)
     historico.config(state="normal")
     historico.insert(tk.END, f"NoellE: {resposta}\n", "NoellE")
     historico.config(state="disabled")
     input.delete(0, tk.END) 
     
     enviar.config(state="normal")
     root.after(0, lambda: enviar.config(state="normal"))

     
def thread():
     thread = threading.Thread(target=NoellE, daemon=True)
     
     thread.start()

# Criação e configuração da interface

root = tk.Tk()
root.title("NoellE")
root.geometry("800x400")

root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.bind("<F11>", lambda event: root.attributes("-fullscreen", True))

# Título da janela
title = tk.Label(root, text="NoellE", font=("Sacramento", 36))  # Fonte mais equilibrada
title.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

# Campo de entrada de texto
input = tk.Entry(root)
input.place(relx=0.18, rely=0.75, relwidth=0.6, height=25)
input.config(fg="#000000", font=("Arial", 14))

# Botão de envio
enviar = tk.Button(root, text="Enviar", command=thread, font=("Arial", 12))
enviar.place(relx=0.78, rely=0.75, width=80, height=25)

# Modo escuro/Claro
dark = tk.BooleanVar(value=True)
DM = tk.Checkbutton(root, text="Dark Mode", variable=dark, onvalue=True, offvalue=False, command=fundo, font=("Arial", 10))
DM.place(relx=0.9, rely=0.1, width=80)

# Histórico de mensagens
historico = tk.Text(root, state="disabled", font=("Arial", 12))
historico.place(relx=0.18, rely=0.2, relwidth=0.7, relheight=0.5)

# Definição de estilos para o histórico
historico.tag_config("usuario", foreground="#000000", font=("Arial", 12))
historico.tag_config("NoellE", foreground="#dc143c", font=("Dancing Script", 16))

Blogin = tk.Button(root, text="Login", command=tela_de_login, font=("Arial", 12))
Blogin.place(relx=0.18, rely=0.9, width=80)


# Aplica o modo inicial
fundo()

# Inicia a interface
root.mainloop()


#resolver a tela de login, a interface está pronta porém falta integrar com o modulo de login
#boa sorte futuro eu