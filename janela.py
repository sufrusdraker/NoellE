
import os
import tkinter as tk
from ot1p import gerar_resposta  
import threading 
#importar as bibliotecas

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "Llama-3.2-3B-Instruct-Q4_0.gguf")
memory_file = os.path.join(current_dir, "memoria.json")
#carregar o modelo da NoellE

fala = False

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
     global fala
     

     mensagem = input.get()
     historico.config(state="normal")
     historico.insert(tk.END, f"usuario: {mensagem}\n", "usuario")
     historico.config(state="disabled")

     print("tem calma, ainda não quebrou") #debug

     user_input = input.get()
     resposta = gerar_resposta(user_input)
     fala = True
     historico.config(state="normal")
     historico.insert(tk.END, f"NoellE: {resposta}\n", "NoellE")
     historico.config(state="disabled")
     input.delete(0, tk.END) 
     fala = False

     root.after(0, lambda: input.config(state="normal"))
     
def thread():
     thread = threading.Thread(target=NoellE)
     
     thread.start()

#cria e configura a tela do codigo  
root = tk.Tk()
root.title("NoellE")
root.geometry("800x400")

title = tk.Label(root, text="NoellE", font=("Arial", 20))
title.place(relx=0.1, rely=0.1, relheight= 0.1, relwidth=0.8)

input = tk.Entry(root)
input.place(relx=0.18, rely=0.8, relwidth=0.4, height=20)
input.config(fg="#000000")

if fala == True:
     input.config(state="disabled")
else:
     input.config(state="normal")


enviar = tk.Button(root, text="Enviar", command=thread)
enviar.place(relx=0.7, rely=0.8, width=80)

dark = tk.BooleanVar(value=True)

DM = tk.Checkbutton(root, text="dark mode", variable=dark, onvalue=True, offvalue=False, command=fundo)
DM.place(relx=0.9, rely=0.2, width=80)
    
historico = tk.Text(root, state="disabled")
historico.place(relx=0.18, rely=0.2, relwidth=0.7, relheight=0.6)

historico.tag_config("usuario", foreground="#000000")
historico.tag_config("NoellE", foreground="#dc143c")
    

fundo()
root.mainloop()
    