import json
from typing import List
from package.pessoa import Pessoa 

def salvar_pessoas(pessoas: List[Pessoa],caminho: str = "pessoas.json") -> None:
  dados = [{"nome": p._Pessoa__nome, "peso": p._Pessoa__peso, "altura": p._Pessoa__altura} 
             for p in pessoas]
  try:
    with open(caminho, "w", encoding="utf-8") as f:
      json.dump(dados, f, indent=2, ensure_ascii=False)
  except Exception as e:
    raise IOError(f"Falha ao salvar: {str(e)}")

def carregar_pessoas(caminho: str = "pessoas.json") -> List[Pessoa]':
  try:
    with open(caminho, "r", encoding="utf-8") as f:
      dados = json.load(f)
      return [Pessoa(p["nome"], p["peso"], p["altura"]) for p in dados]
  except FileNotFoundError:
    return []
  except Exception as e:
    raise IOError(f"Falha ao carregar: {str(e)}")
