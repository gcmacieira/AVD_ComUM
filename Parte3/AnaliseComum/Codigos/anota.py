import spacy 
from jjcli import *
#pip install -U spacy

#python -m spacy download en_core_web_sm


# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("pt_core_news_lg")

# Process whole documents
#text = ("Viva a Daniella que escreveu um programa Python.")
cl = clfilter("")

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

contador = 0
output = open ("corpus-anotado.txt",'w', encoding="UTF-8")
# Find named entities, phrases and concepts
#for entity in doc.ents:
   # print(entity.text, entity.label_)
for par in cl.paragraph():
    contador += 1
    #if contador > 50:  #Comentar para trabalhar com o corpus inteiro
       # break  #sair "daqui"
    doc = nlp(par)
    with doc.retokenize() as retokenizer:
        for entity in doc.ents:
            retokenizer.merge(entity)

    for sentence in doc.sents:
        print(file=output)
        for word in sentence:
            print(f'{word.text}\t{word.lemma_}\t{word.pos_}\t{word.ent_type_}', file=output)