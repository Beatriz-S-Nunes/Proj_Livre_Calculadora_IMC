import tkinter as tk
from tkinter import messagebox
from package.pessoa import Pessoa, PessoaAtleta

def calcular():
  nome = entry_nome.get()
  peso = float(entry_peso.get())
  altura = float(entry_altura.get())
    
  if var_tipo.get() == ""comum":
    pessoa = Pessoa(nome, peso, altura)
  else:
    pessoa = PessoaAtleta(nome, peso, altura)
  
  resultado - str(pessoa)
  messagebox.showinfo("Resultado", resultado)

janela = tk.Tk()
janela.title("Calculadora de IMC")

tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Peso (kg):")pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

tk.Label(janela, text="Altura (m):").pack
entry_altura = tk.Entry(janela)
entry_altura.pack()

var_tipo = tk.StringVar(value="comum")
tk.Radiobutton(janela, text="Pessoa comum", variable=var_tipo, value="comum").pack()
tk.Radiobutton(janela, text="Pessoa atleta", variable=var_tipo, value="atleta").pack()

tk.Button(janela, text="Calcular IMC", command=calcular).pack()

janela.mainloop()
