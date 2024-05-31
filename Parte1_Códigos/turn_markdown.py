from jjcli import *
import os
from bs4 import BeautifulSoup

# Ler o arquivo HTML:

diretorio = "C:\\Users\\Maria Francisca\\Desktop\\Análise e Visualização de Dados\\ComUM\\Artigos_ComUM"

html_content_list = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".html"): # pegar em todos os ficheiros html
        caminho_arquivo = os.path.join(diretorio, arquivo) # construir o caminho completo para o arquivo
        with open(caminho_arquivo, "r", encoding="utf-8") as file: # abrir o arquivo e ler o conteúdo
            html_content_list.append(file.read()) # adicionar o conteúdo do arquivo à lista

# Analisar o HTML:
            
soup_list = []

for html_content in html_content_list:
    soup = BeautifulSoup(html_content, "html.parser")
    soup_list.append(soup)

# Extrair as informações:
    
for i, soup in enumerate(soup_list):
    titulo = soup.find("h1", class_="title entry-title").get_text(strip=True)

    subtitulo_element = soup.find('h2', class_='post-subtitle')
    subtitulo = subtitulo_element.get_text(strip=True) if subtitulo_element else ''

    data_element = soup.find("div", class_="date updated")
    data = data_element.get_text(strip=True) if data_element else ''

    byline_element = soup.find("div", class_="byline")

    autor_element = byline_element.find("a") if byline_element else ''
    autor = autor_element.get_text(strip=True) if autor_element else ''

    descricao_element = soup.find("meta", attrs={"name": "description"})
    descricao = descricao_element["content"] if descricao_element else ''

    url_element = soup.find("meta", property="og:url")
    url = url_element["content"] if url_element else ''

    site_element = soup.find("meta", property="og:site_name")
    site = site_element["content"] if site_element else ''

    tipo_element = soup.find("meta", property="og:type")
    tipo = tipo_element["content"] if tipo_element else ''

    tags_elements = soup.find_all("meta", property="article:tag")
    tags = [meta["content"] for meta in tags_elements]
    tags_concatenadas = ', '.join(tags)

    div_postcontent = soup.find('div', class_='postcontent content')
    paragrafos = [p.get_text() for p in div_postcontent.find_all("p")]
    paragrafos_concatenados = "\n\n".join(paragrafos)

    imagecover_element = soup.find("div", class_="imagecover")
    imagem = imagecover_element.find("img")["src"] if imagecover_element else ''

# Formatação:
    
    artigo_markdown = f"""---
date: {data}
author: {autor}
image: {imagem}
title: {titulo}
url: {url}
site: {site}
description: {descricao}
tags: {tags_concatenadas}
type: {tipo}
---


# {titulo}

## {subtitulo}

{data} | {autor}

{paragrafos_concatenados}

"""

# Escrever no arquivo de texto:

    nome_arquivo = f"artigo_{i+1}.md" 
    with open(nome_arquivo, "w", encoding="utf-8") as file:
        file.write(artigo_markdown)