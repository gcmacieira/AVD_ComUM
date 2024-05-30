from jjcli import *
from textblob import TextBlob

def calcula_sentimento(texto):
    analysis = TextBlob(chapter)

    # Verifica o sentimento da frase
    if analysis.sentiment.polarity > 0:
        sentiment = "Positivo"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return sentiment, analysis.sentiment.polarity

hp_file = open("../Ficheiros_utilizados/HarryPotter/HP.txt", "r", encoding="utf8").read()
hp_chapters = hp_file.split("#")                              #Divide por capitulos, através do cardinal (#)
results = ""

# Realiza a análise de sentimentos
for chapter in hp_chapters:                                              # Analisa os sentimentos por capitulo
    sentiment_chapter, analysis_chapter = calcula_sentimento(chapter)
    chapter_number = chapter.splitlines()[0].replace(' ', '')               #O número de capitulo, sem espaços

    if '-' in chapter_number:
        results += "Introdução\n"                                           #Caso tenha um traço é uma introdução, não um capitulo
       # print(f"Introdução")
    else:
        results += "Capítulo " + chapter_number + "\n"                      #Dá print do número do capitulo
       # print(f"Capítulo {chapter_number}")

    results += "Sentimento: " + sentiment_chapter + "\n"
    #print(f"Sentimento: {sentiment_chapter}")                             #Print dos sentimentos

    results += "Polaridade do Sentimento: " + str(analysis_chapter) + "\n"
    #print(f"Polaridade do Sentimento: {analysis_chapter}")                    #Print da polaridade
    print(f"{chapter_number} , {analysis_chapter}")
   # results += "-" * 50 + "\n"                                           #Print dos traços para dividir os resultados
   # print("-" * 50)

sentiment_book, analysis_book = calcula_sentimento(hp_file)                 #Calculo do livro todo

results += "Livro completo\n"
print(f"Livro completo")

results += "Sentimento: " + sentiment_book + "\n"
print(f"Sentimento: {sentiment_book}")

results += "Polaridade do Sentimento: " + str(analysis_book) + "\n"
print(f"Polaridade do Sentimento: {analysis_book}")

results += "-" * 50
print("-" * 50)

with open("../Resultados/resultados.txt", "w") as file1:
    file1.write(results)
                                                          #Guardar os resultados num ficheiro
file1.close