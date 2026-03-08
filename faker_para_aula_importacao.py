import pandas as pd
import numpy as np
from faker import Faker
import os

fake = Faker("pt_BR")
np.random.seed(42)

os.makedirs("planilhas", exist_ok=True)

meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "marco",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

produtos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "Headset",
    "Webcam"
]

for mes_num, mes_nome in meses.items():

    n = np.random.randint(80, 120)

    # gera todas as datas possíveis do mês
    datas_mes = pd.date_range(
        start=f"2025-{mes_num:02d}-01",
        end=f"2025-{mes_num:02d}-28"
    )

    dados = {
        "id_venda": range(1, n + 1),
        "cliente": [fake.name() for _ in range(n)],
        "produto": np.random.choice(produtos, n),
        "valor": np.round(np.random.uniform(50, 5000, n), 2),
        "cidade": [fake.city() for _ in range(n)],
        "data": np.random.choice(datas_mes, n)
    }

    df = pd.DataFrame(dados)

    caminho = f"planilhas/vendas_{mes_nome}.xlsx"

    df.to_excel(caminho, index=False)

print("Planilhas geradas com sucesso!")