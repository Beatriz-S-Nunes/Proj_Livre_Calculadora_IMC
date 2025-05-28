from package.pessoa import Pessoa
from package.controlador import ControladorIMC

def main():
  controlador = ControladorIMC

  while True:
    nome = input("Nome da pessoa (ou 'sair'): ")
    if nome.lower() == 'sair':
      break
    peso == float(input("Peso (kg): "))
    altura == float(input("Altura (m): "))
   
    pessoa = Pessoa(nome, peso, altura)
    controlador.adicionar_pessoa(pessoa)
     
  print("\nResultados:")
  controlador.mostrar_todos()
