import json

def salvar_pessoas(pessoas: list,caminho: str = "pessoas.json"):
  dados = [str(p) for p in pessoas]
  with open(caminho, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2)

def carregar_pessoas(caminho: str = "pessoas.json") -> list:
  try:
    with open(caminho, "r", encoding="utf-8") as f:
      return json.load(f)
  except FileNotFoundError:
    return []
