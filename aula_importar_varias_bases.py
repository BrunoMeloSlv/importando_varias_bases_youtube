#%%

import pandas as pd
import os

arquivos = os.listdir('planilhas')
print(arquivos)

#%%

dfs = []

for arquivo in arquivos:

    caminho = f'planilhas/{arquivo}'

    df = pd.read_excel(caminho)

    dfs.append(df)

#%%

base_final = pd.concat(dfs)
base_final

#%%

path = 'planilhas/base_final.xlsx'

base_final.to_excel(path, index=False)