import pandas as pd
from matplotlib import pyplot as plt
from jjcli import *
from textblob import TextBlob

def calcula_sentimento(texto):
    analysis = TextBlob(texto)

    # Verifica o sentimento da frase
    if analysis.sentiment.polarity > 0:
        sentiment = "Positivo"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return sentiment, analysis.sentiment.polarity

# Leitura do arquivo do livro
hp_file = open("../Ficheiros_utilizados/HarryPotter/HP.txt", "r", encoding="utf8").read()
hp_chapters = hp_file.split("#")
results = []

# Realiza a análise de sentimentos por capítulo
for chapter in hp_chapters:
    sentiment_chapter, analysis_chapter = calcula_sentimento(chapter)
    chapter_number = chapter.splitlines()[0].replace(' ', '')

    if '-' in chapter_number:
        chapter_number = "Introdução"
    else:
        chapter_number = "Capítulo " + chapter_number

    results.append((chapter_number, sentiment_chapter, analysis_chapter))

# Adiciona a análise de sentimentos do livro completo
sentiment_book, analysis_book = calcula_sentimento(hp_file)
results.append(("Livro Completo", sentiment_book, analysis_book))

# Cria um DataFrame para armazenar os resultados
df = pd.DataFrame(results, columns=["Capítulo", "Sentimento", "Polaridade"])

# Gráfico de barras da polaridade por capítulo
plt.figure(figsize=(10, 6))
plt.bar(df["Capítulo"], df["Polaridade"], color='skyblue')
plt.xlabel('Capítulo')
plt.ylabel('Polaridade')
plt.title('Polaridade de Sentimento por Capítulo')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

