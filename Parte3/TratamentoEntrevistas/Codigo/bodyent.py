import spacy
from collections import Counter
import csv

nlp = spacy.load("pt_core_news_lg")

with open('entrevista_nca.md', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

# Identifica e conta as entidades nomeadas PROPN
all_propn = Counter()

for ent in doc.ents:
    if ent.label_ == "PER" or ent.label_ == "ORG" or ent.label_ == "LOC":
        all_propn[ent.text] += 1

print(all_propn)

# Escreve os resultados num arquivo CSV
with open("propnnca.csv", 'w', encoding="UTF-8", newline='') as output:
    writer = csv.writer(output)
    writer.writerow(['PROPN', 'Frequência'])
    for propn, freq in all_propn.items():
        writer.writerow([propn, freq])

print("Os resultados foram salvos em 'propn.csv'.")
