import pandas as pd

data = [
    ("04/07", "farmácia", None, 13.90),
    ("04/07", "padaria", "pão", 8.71),
    ("05/07", "padaria", "pão", 6.36),
    ("06/07", "padaria", "manteiga", 24.45),
    ("06/07", "sacolão", None, 9),
    ("06/07", "lanchonete", "hambúrguer", 26),
    ("07/07", "padaria", "pão", 6.43),
    ("07/07", "sacolão", "brócolis", 7),
    ("07/07", "sacolão", "Salsinha", 2),
    ("07/07", "mercado", "carne moída", 13.32),
    ("07/07", "mercado", "filé de frango", 13.83),
    ("07/07", "mercado", "pimenta do reino", 2.68),
    ("07/07", "mercado", "folha de louro", 2.48),
    ("07/07", "mercado", "orégano", 2.28),
    ("07/07", "mercado", "café", 19),
    ("07/07", "mercado", "açúcar", 4),
    ("07/07", "mercado", "papel higiênico", 19),
    ("07/07", "mercado", "sabão em pó", 9),
    ("07/07", "mercado", "detergente", 2.39),
    ("09/07", "padaria", None, 15.35),
    ("09/07", "farmácia", "cr dental", 4),
    ("09/07", "farmácia", "sabonete", 5.40),
    ("10/07", "pet shop", "ração", 18.50),
    ("10/07", "açougue", "calabresa", 5.50),
    ("11/07", "padaria", "pão", 8.12),
    ("11/07", "lanchonete", "frango frito", 30),
    ("13/07", "padaria", "pão", 6.50),
]

df = pd.DataFrame(data, columns=["data", "local", "incluindo", "valor"])
print(df)
print("\nO gasto total até o momento foi de R$", round(df["valor"].sum(), 2))

