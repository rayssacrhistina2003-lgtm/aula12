#crie um dataframe que tera 3 colunas e 3 linhas: NOME, CARGO, E SALARIO

import pandas as pd

dicionario = {"NOME": ["Rayssa", "christina", "santos"], "CARGO": ["analista", "gerente", "assistente"], "SALARIO": [1000, 2000, 3000]}

df = pd.DataFrame(dicionario)

print(df)

df.to_csv("pandas exercicio 1.csv", index=False, sep=";")