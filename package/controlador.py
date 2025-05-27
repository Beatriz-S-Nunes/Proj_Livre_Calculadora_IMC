from package.pessoa import Pessoa

class ControladorIMC:
  def __init__(self):
    self.__lista_pessoas = []

  def adicionar_pessoa(self, pessoa: Pessoa):
    self.__lista_pessoas.append(pessoa)

  def mostrar_todos(self):
    for pessoa in self.__lista_pessoas:
      print(pessoa)
