
import tkinter as tk

#criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia frases")

#Adiciona um frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x' , expand=True)

# Adiciona o Label
label = tk.Label(frame, text="Olá Mundo")
label.pack(fill='x', expand=True)

#Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

#Alterar o texto do label
def click():
    label.config(text=frase_inp.get())

#Adicionando botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop()
