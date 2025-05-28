def classificar_imc(imc: float) -> str:
    imc = self.calculo_do_imc()
    if imc < 18.5:
      return "Magreza"
    elif 18.5 <= imc < 24.9:
      return "Normal"
    elif 25 <= imc < 29.9:
      return "Sobrepeso"
    else:
      return "Obesidade"
