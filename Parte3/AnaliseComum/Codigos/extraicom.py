#!/usr/bin/env python3

import re
import yaml
import pandas as pd
from jjcli import *
import glob

docs = glob.glob("ComUM/*.md")
print(f"ComUm: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs)

# Lista para armazenar os dados dos artigos
articles_data = []

for txt in cl.text():
    #print(txt[:100])
    for meta in re.findall(r'---(.*?)---', txt, flags=re.S):
        #print(meta)
        dicmeta = yaml.safe_load(meta)
        date = dicmeta.get('date')
        title = dicmeta.get('title')
        filename = cl.filename()

        # Contando as palavras do artigo (considerando o texto fora dos metadados)
        article_content = re.sub(r'---.*?---', '', txt, flags=re.S).strip()
        word_count = len(article_content.split())

        # Adiciona os dados do artigo à lista
        articles_data.append([date, title, filename, word_count])

# Criando um DataFrame do pandas
df = pd.DataFrame(articles_data, columns=['Date', 'Title', 'Filename', 'Word Count'])

# Salvando o DataFrame em um arquivo Excel
df.to_excel('articles_data.xlsx', index=False)

print("Dados dos artigos salvos em 'articles_data.xlsx'")
