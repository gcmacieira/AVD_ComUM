import spacy 
from jjcli import *
from collections import Counter

cl = clfilter("")
all_propn = Counter()
for linha in cl.input():
    palavras = linha.split("\t")
    if len(palavras) == 4:
        #if palavras[2] == "VERB":
        if palavras[2] == "PROPN":
            if palavras[3] != "LOC":
                continue
            #print(palavras[1])
            lema = palavras[1]
            #if lema[-1] != "r":  #comentar para nomes, adjetivos, PROPN
                #continue
            all_propn.update([palavras[1]])

#print(all_verbs)
output = open ("loc.csv",'w', encoding="UTF-8")
for verbo, oco in all_propn.items():
    print(f"{verbo},{oco}", file = output)
