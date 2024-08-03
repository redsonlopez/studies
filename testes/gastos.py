import pandas as pd

colunas= ["data", "local", "produto", "valor"]
dados= [
    ("04/07/24", "farmácia", None, 13.90),
    ("04/07/24", "padaria", "pão", 8.71),
    ("05/07/24", "padaria", "pão", 6.36),
    ("06/07/24", "padaria", "manteiga", 12),
    ("06/07/24", "padaria", "pão", 8.95),
    ("06/07/24", "padaria", "biscoito", 3.5),
    ("06/07/24", "sacolão", None, 9),
    ("06/07/24", "lanche", "hambúrguer", 26),
    ("07/07/24", "padaria", "pão", 6.43),
    ("07/07/24", "sacolão", "brócolis", 7),
    ("07/07/24", "sacolão", "Salsinha", 2),
    ("07/07/24", "mercado", "carne moída", 13.32),
    ("07/07/24", "mercado", "filé de frango", 13.83),
    ("07/07/24", "mercado", "pimenta do reino", 2.68),
    ("07/07/24", "mercado", "folha de louro", 2.48),
    ("07/07/24", "mercado", "orégano", 2.28),
    ("07/07/24", "mercado", "café", 19),
    ("07/07/24", "mercado", "açúcar", 4),
    ("07/07/24", "mercado", "papel higiênico", 19),
    ("07/07/24", "mercado", "sabão em pó", 9),
    ("07/07/24", "mercado", "detergente", 2.39),
    ("09/07/24", "padaria", None, 15.35),
    ("09/07/24", "farmácia", "cr dental", 4),
    ("09/07/24", "farmácia", "sabonete", 5.4),
    ("10/07/24", "petshop", "ração", 18.5),
    ("10/07/24", "açougue", "calabresa", 5.5),
    ("11/07/24", "padaria", "pão", 8.12),
    ("11/07/24", "lanche", "frango frito", 30),
    ("13/07/24", "padaria", "pão", 6.5),
    ("13/07/24", "lanche", "pizza", 25.99),
    ("14/07/24", "mercado", "arroz", 29),
    ("14/07/24", "lanche", "pizza", 41),
    ("16/07/24", "padaria", "pão", 7.92),
    ("16/07/24", "lanche", "pizza", 26),
    ("18/07/24", "mercado", "feijão", 5),
    ("18/07/24", "mercado", "frango", 15.1),
    ("18/07/24", "mercado", "detergente", 2.4),
    ("20/07/24", "padaria", "pão", 7.92),
    ("20/07/24", "padaria", "biscoito", 7),
    ("20/07/24", "padaria", "trento", 6),
    ("22/07/24", "mercado", "sabonete", 5),
    ("22/07/24", "mercado", "abs", 5.55),
    ("22/07/24", "lanche", "janta", 50),
    ("22/07/24", "lanche", "caldo", 30),
    ("23/07/24", "sacolão", None, 8),
    ("23/07/24", "padaria", "pão", 9),
    ("24/07/24", "farmácia", None, 21.50),
    ("24/07/24", "açougue", "filé de frango", 16.1),
    ("24/07/24", "açougue", "bacon", 5.4),
    ("24/07/24", "açougue", "salsicha", 4.8),
    ("24/07/24", "açougue", "calabresa", 5.6),
    ("24/07/24", "padaria", "pão", 8.22),
    ("24/07/24", "padaria", "biscoito", 3.5),
    ("24/07/24", "padaria", "molho de tomate", 3),
    ("24/07/24", "sacolão", None, 11.85),
    ("25/07/24", "lanche", "hamburger", 30),
    ("26/07/24", "padaria", "pão", 7),
    ("27/07/24", "padaria", "pão", 8.7),
    ("28/07/24", "lanche", "rodízio", 270),
    ("28/07/24", "padaria", None, 20),
    ("30/07/24", "sacolão", None, 2.8),
    ("30/07/24", "padaria", "café", 12),
    ("30/07/24", "padaria", "pão", 9),
    ("03/08/24", "padaria", None, 21),
]

df= pd.DataFrame(data= dados, columns= colunas)
#df= df[df["data"]== "08/24"]

lanches= df[df["local"]== "lanche"]
basico= round(df["valor"].sum() - lanches["valor"].sum(), 2)

print(f"Os locais de gastos foram:\n{df['local'].unique()}.")
print(f"\nO gasto total até o momento foi de R${round(df["valor"].sum(), 2)}.")
print(f"Os gastos com lanches foram de R${round(lanches['valor'].sum(), 2)}.")
print(f"O gasto básico foi de R${basico}.")

print(f"\nOs gastos com lanches foram:\n{lanches['produto'].unique()}.")

