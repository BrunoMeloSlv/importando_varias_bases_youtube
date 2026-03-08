# Importando várias bases com Python

Este repositório contém o código utilizado no vídeo do YouTube onde mostro como **automatizar a importação de várias planilhas Excel usando Python**.

Esse é um problema muito comum no dia a dia de quem trabalha com **análise de dados**: receber várias planilhas e precisar consolidar tudo em uma única base.

Com Python e Pandas é possível resolver isso **em poucos segundos**.

---

## 🎥 Vídeo da Aula

Assista a aula completa no YouTube:

https://youtu.be/uJcR_2RzF4o

## 📊 O que o projeto faz

O script:

1. Lê todos os arquivos `.xlsx` dentro de uma pasta
2. Importa cada planilha como um DataFrame
3. Armazena os DataFrames em uma lista
4. Consolida todas as bases em uma única tabela
5. Exporta o resultado final

---

## 🐍 Exemplo de Código

```python
import pandas as pd
import os

arquivos = os.listdir("planilhas")

dfs = []

for arquivo in arquivos:

    caminho = f"planilhas/{arquivo}"

    df = pd.read_excel(caminho)

    dfs.append(df)

base_final = pd.concat(dfs)

base_final.to_excel("base_consolidada.xlsx", index=False)

pip install pandas faker numpy openpyxl

👨‍💻 Autor

Bruno Melo

Criador de conteúdo na área de Dados, Estatística e Automação com Python.

YouTube
LinkedIn
Instagram


