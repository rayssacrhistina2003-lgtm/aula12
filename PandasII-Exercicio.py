#crie o dataframe a partir do dicionario e faça os seguintes filtros:
#funcionarios com salario maior que 3000.00
#funcionarios com o cargo de vendedor

import pandas as pd 

dicionario = {"NOME": ["Geronino", "martha", "patrocolos", "triberios", "janaina", "mercedes"],
               "CARGO": ["gerente", "gerente", "vendedor", "secretario", "vendedora", "vendedor"],
                 "SALARIO": [9600.56, 9600.56, 2600.90, 4500.45, 2600.90, 2600.90]}

df = pd.DataFrame(dicionario)

print(df[df["SALARIO"] > 3000.00])

print(df[df["CARGO"] == "vendedor"])

print(df[(df["CARGO"] == "vendedor") | (df["CARGO"] == "vendedora")])

df.to_csv("pandas exercicio 2.csv", index=False, sep=";")