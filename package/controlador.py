from package.pessoa import Pessoa
from package.serializador import salvar_pessoas

class ControladorIMC:
  def __init__(self):
    self.__lista_pessoas = []
    self.carregar_dados()

  def carregar_dados(self):
    from package.serializador import carregar_pessoas
    self.__lista_pessoas = carregar_pessoas()

  def adicionar_pessoa(self, pessoa: Pessoa):
    self.__lista_pessoas.append(pessoa)

  def mostrar_todos(self):
    for pessoa in self.__lista_pessoas:
      print(pessoa)
    salvar_pessoas(self.__lista_pessoas)
