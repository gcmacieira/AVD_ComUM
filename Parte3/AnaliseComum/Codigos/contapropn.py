import spacy 
from jjcli import *
from collections import Counter

cl = clfilter("")
all_propn = Counter()

for linha in cl.input():
    palavras = linha.split("\t")  #.split()
    if len(palavras) == 4: 
        if palavras[2] == "PROPN": 
            lema = palavras[1]
           #if lema[-1] != "r":   #encontrar o r
               #continue
           # print(palavras[1])
            all_propn.update([palavras[1]])


print(all_propn)
output  = open ("propn.csv", 'w', encoding="UTF-8")
for verbo, oco in all_propn.items():
   print(f'{verbo},{oco}', file = output) 