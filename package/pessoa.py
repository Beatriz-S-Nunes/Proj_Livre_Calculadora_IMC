class Pessoa:
  def __init__(self, nome: str, peso: float, altura: float):
    self.__nome = nome
    self.__peso = peso
    self.__altura = altura
  
  def calculo_do_imc(self) -> float:
    return self.__peso / (self.__altura**2)
  
  def classificao(self) -> str:
    imc = self.calculo_do_imc()
    if imc < 18.5:
      return "Magreza"
    elif 18.5 <= imc < 24.9:
      return "Normal"
    elif 25 <= imc < 29.9:
      return "Sobrepeso"
    else:
      return "Obesidade"
  
  def __str__(self):
    return f"{self.__nome} - IMC: {self.calculo_do_imc():.2f} ({self.classicacao()})"
