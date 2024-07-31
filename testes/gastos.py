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
    ("06/07/24", "lanchonete", "hambúrguer", 26),
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
    ("10/07/24", "pet shop", "ração", 18.5),
    ("10/07/24", "açougue", "calabresa", 5.5),
    ("11/07/24", "padaria", "pão", 8.12),
    ("11/07/24", "lanchonete", "frango frito", 30),
    ("13/07/24", "padaria", "pão", 6.5),
    ("13/07/24", "lanchonete", "pizza", 25.99),
    ("14/07/24", "mercado", "arroz", 29),
    ("14/07/24", "lanchonete", "pizza", 41),
    ("16/07/24", "padaria", "pão", 7.92),
    ("16/07/24", "lanchonete", "pizza", 26),
    ("18/07/24", "mercado", "feijão", 5),
    ("18/07/24", "mercado", "frango", 15.1),
    ("18/07/24", "mercado", "detergente", 2.4),
]

df= pd.DataFrame(data= dados, columns= colunas)
print(df)
print("\nO gasto total até o momento foi de R$",\
        round(df["valor"].sum(), 2))

