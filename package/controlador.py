from package.pessoa import Pessoa
from package.serializador import salvar_pessoas, carregar_pessoas
from typing import List

class ControladorIMC:
  def __init__(self):
    self.__lista_pessoas: List[Pessoa] = carregar_pessoas()
    # self.carregar_dados()

  def adicionar_pessoa(self, pessoa: Pessoa) -> None:
    if not isinstance(pessoa, Pessoa):
      raise TypeError("Objeto deve ser do tipo Pessoa")
    self.__lista_pessoas.append(pessoa)
    salvar_pessoas(self.__lista_pessoas)
    
  def get_historico(self) -> List[Pessoa]:
    return self.__lista_pessoas.copy()
    
  def limpar_historico(self) -> None:
    self.__lista_pessoas.clear()
    salvar_pessoas(self.__lista_pessoas)
      
