from package.classificacao import classificar_imc

class Pessoa:
  def __init__(self, nome: str, peso: float, altura: float):
    self.__nome = nome
    self.__peso = peso
    self.__altura = altura
  
  def calculo_do_imc(self) -> float:
    return self.__peso / (self.__altura**2)
  
  def classificar(self) -> str:
    imc = self.calculo_do_imc()
    return classificar_imc(imc)
  
  def __str__(self):
    return f"{self.__nome} - IMC: {self.calculo_do_imc():.2f} ({self.classificar()})"

class PessoaAtleta(Pessoa):
  def classificar(self) -> str:
    imc = self.calculo_do_imc()
    if imc < 20:
      return "Atleta - Abaixo do ideal"
    elif 20 <= imc < 25:
      return "Atleta - No ideal"
    else:
      return "Atleta - Acima do ideal"
