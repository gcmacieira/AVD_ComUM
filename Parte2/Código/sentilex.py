from matplotlib import pyplot as plt
from jjcli import *
from wordcloud import WordCloud
from collections import Counter

output_positivos = "../Resultados/positivos.txt"
output_negativos = "../Resultados/negativos.txt"

def gera_negativos_positivos(ficheiro):
    open(output_positivos, 'w').close()
    open(output_negativos, 'w').close()
    with open(ficheiro, 'r') as f:
        for linha in f:
            if "POL:N0=-1" in linha:
                word = linha.split("POL:N0-=1")[0].strip().split(",")[0]
                with open(output_negativos, 'a') as file:
                    file.write(word + '\n')
            elif "POL:N0=1" in linha:
                word = linha.split("POL:N0=1")[0].strip().split(",")[0]
                with open(output_positivos, 'a') as file:
                    file.write(word + '\n')

def generate_wordcloud(ficheiro):
    with open(ficheiro, 'r') as file:
        texto = file.read()

    words = texto.splitlines()
    texto_minusculas = texto.lower()

    # Contagem da frequência de palavras que são negativas
    word_counts = Counter(texto_minusculas.split())
    negative_counts = {word: word_counts[word] for word in words if word in word_counts}

    # Nuvém de palavras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(negative_counts)

    # Criação da nuvém de palavras
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

gera_negativos_positivos("../Ficheiros_utilizados/Sentilex/sentilexjj.txt")
generate_wordcloud(output_positivos)
generate_wordcloud(output_negativos)