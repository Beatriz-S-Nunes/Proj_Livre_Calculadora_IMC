# Proj_Livre_Calculadora_IMC
  Este é um projeto de calculadora de IMC (Índice de Massa Corporal) em Python, que tem como objetivo, permitir que o usuário possa inserir seu peso e altura e receber o resultado do cálculo e sua categoria correspondente (ex: Magreza, Normal, Sobrepeso etc.).
  
  Ele usa 4 dos princípios da Orientação a Objetos:
    - Herança
    - Polimorfismo
    - Encapsulamento
    - Composições fortes

  Casos de Uso:
  
    Caso de Uso 1: Cálculo de IMC
      **Ator**: Usuário  
      **Descrição**: O usuário informa peso e altura. O sistema calcula o IMC e mostra o resultado e a classificação.
      
    Caso de Uso 2: Registro de múltiplos perfis
      **Ator**: Usuário  
      **Descrição**: O usuário pode registrar dados de diferentes pessoas e consultar posteriormente o IMC de cada uma.

+-----------------------+

| Pessoa |

+------------------------+

|   - __nome: str          |

|   - __peso: float        |

|   - __altura: float      |

+------------------+

| +calculo_do_imc()      |

| +classificar()         |

| +__str__()             |

+------------------------+

           ▲
           │ Herança
           │
+------------------------+

|     PessoaAtleta       | 

+------------------------+

| (herda atributos)      |

+------------------------+

| +classificar()         |

+------------------------+


               ◄◄◄◄◄◄◄◄◄◄◄◄◄◄
                usada por (composição)
                
+----------------------------+

|      ControladorIMC        |


+----------------------------+

| - __lista_pessoas: list    |

+----------------------------+

| +adicionar_pessoa()        |

| +mostrar_todos()           |

+----------------------------+

+----------------------------+

|   classificar_imc(imc)     |

|  (função externa utilitária) |

+----------------------------+

+----------------------------+

|     serializador.py        |

+----------------------------+

| +salvar_pessoas()          |

| +carregar_pessoas()        |

+----------------------------+



calculadora_imc/

├── main.py

├── README.md

├── imc_gui.py 

│

├── pessoas.json              

│

├── requirements.txt           

│

├── package/

│  ├── __init__.py

│   ├── pessoa.py

│   ├── controlador.py

│   └── classificacao.py

│   └── serializador.py 

