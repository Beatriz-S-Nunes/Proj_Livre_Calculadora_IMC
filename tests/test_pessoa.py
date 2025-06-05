import pytest
from package.pessoa import Pessoa, PassoaAtleta

def test_pessoa_de_imc_normal():
  pessoa = Pessoa("João", 70, 1.75)
  assert round(pessoa.calculo_imc(), 2)
