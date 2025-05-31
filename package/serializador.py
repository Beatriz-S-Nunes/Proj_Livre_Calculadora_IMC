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
    
  for pessoa in pessoas:
        dados.append({
            "nome": pessoa._Pessoa__nome,  ributo privado __nome
            "peso": pessoa._Pessoa__peso,   
            "altura": pessoa._Pessoa__altura
        })
  try:
    with open(caminho, "w", encoding="utf-8") as arquivo:
      json.dump(dados, arquivo, indent=2, ensure_ascii=False)
  except (IOError, PermissionError) as e:
    print(f"Ocorreu um erro ao salvar arquivo: {e}")

def carregar_pessoas(caminho: str = "pessoas.json") -> List[Pessoa]:
  try:
    with open(caminho, "r", encoding="utf-8") as arquivo:
      dados = json.load(arquivo)
            return [Pessoa(p["nome"], p["peso"], p["altura"]) for p in dados]
    except FileNotFoundError:
        return []  # Retorna lista vazia se o arquivo não existir
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Erro ao ler arquivo: {e}")
        return []
    except (IOError, PermissionError) as e:
        print(f"Erro ao acessar arquivo: {e}")
        return []
