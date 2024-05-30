import spacy
import pandas as pd
from matplotlib import pyplot as plt

file = open("../Ficheiros_utilizados/Output/output_2136.md", "r", encoding='utf8')
text = file.read()

def main():
    verbos = procVerbos(text)
    toponimos = procToponimos(text)
    nomes_proprios = procNomesProprios(text)
    adjetivos = procAdjetivos(text)
    adverbios = procAdverbios(text)
    contagemExcel(verbos, toponimos, nomes_proprios, adjetivos, adverbios)


def procVerbos(texto):
     verbos=[]
     nlp=spacy.load("pt_core_news_lg")
     doc=nlp(texto)
     for pal in doc:
         if pal.pos_=='VERB':
            verbos.append(pal.lemma_)
     print(f"{len(verbos)}\n{verbos}\n\n")
     return verbos

def procNomesProprios(texto):
     nomesProprios=[]
     nlp=spacy.load("pt_core_news_lg")
     doc=nlp(texto)
     for ent in doc.ents:
         if ent.label_=='PER':
            nomesProprios.append(ent.text)
     print(f"{len(nomesProprios)}\n{nomesProprios}\n\n")
     return nomesProprios

def procToponimos(texto):
     toponimos=[]
     nlp=spacy.load("pt_core_news_lg")
     doc=nlp(texto)
     for ent in doc.ents:
         if ent.label_=='LOC':
            toponimos.append(ent.text)
     print(f"{len(toponimos)}\n{toponimos}\n\n")
     return toponimos

def procAdjetivos(texto):
     adjetivos=[]
     nlp=spacy.load("pt_core_news_lg")
     doc=nlp(texto)
     for pal in doc:
         if pal.pos_=='ADJ':
            adjetivos.append(pal.lemma_)
     print(f"{len(adjetivos)}\n{adjetivos}\n\n")
     return adjetivos

def procAdverbios(texto):
     adverbios=[]
     nlp=spacy.load("pt_core_news_lg")
     doc=nlp(texto)
     for pal in doc:
         if pal.pos_=='ADV':
            adverbios.append(pal.lemma_)
     print(f"{len(adverbios)}\n{adverbios}\n\n")
     return adverbios


def contagemExcel(verbos, toponimos, nomesProprios, adjetivos, adverbios):

     frequencia_absoluta_verbos = pd.Series(verbos).value_counts()              #Frequência de cada classe gramatical
     frequencia_absoluta_toponimos = pd.Series(toponimos).value_counts()
     frequencia_absoluta_nomesProprios = pd.Series(nomesProprios).value_counts()
     frequencia_absoluta_adjetivos = pd.Series(adjetivos).value_counts()
     frequencia_absoluta_adverbios = pd.Series(adverbios).value_counts()

     df_verbos = pd.DataFrame({'Verbos': frequencia_absoluta_verbos.index, 'Total de Verbos': frequencia_absoluta_verbos.values})
     df_toponimos = pd.DataFrame({'Topónimos': frequencia_absoluta_toponimos.index, 'Total de Topónimos': frequencia_absoluta_toponimos.values})
     df_nomesProprios = pd.DataFrame({'Nomes Próprios': frequencia_absoluta_nomesProprios.index, 'Total de Nomes Próprios': frequencia_absoluta_nomesProprios.values})
     df_adjetivos = pd.DataFrame({'Adjetivos': frequencia_absoluta_adjetivos.index, 'Total de Adjetivos': frequencia_absoluta_adjetivos.values})
     df_adverbios = pd.DataFrame({'Advérbios': frequencia_absoluta_adverbios.index, 'Total de Advérbios': frequencia_absoluta_adverbios.values})   #Converte para Dataframe

     # Juntar a nova coluna ao DataFrame original usando merge
     df_merge_1 = pd.merge(df_verbos, df_toponimos, left_index=True, right_index=True, how="outer")
     df_merge_2 = pd.merge(df_merge_1, df_nomesProprios, left_index=True, right_index=True, how="outer")
     df_merge_3 = pd.merge(df_merge_2, df_adjetivos, left_index=True, right_index=True, how="outer")
     df_merge_4 = pd.merge(df_merge_3, df_adverbios, left_index=True, right_index=True, how="outer")

     with pd.ExcelWriter('../Resultados/Contagens.xlsx') as writer:
          df_merge_4.to_excel(writer, index=False, sheet_name='Contagens')   #converte para um ficheiro excel

          workbook = writer.book
          centrar = workbook.add_format({'align': 'center', 'valign': 'vcenter'})   #centrar os nomes das colunas

          # Definir o tamanho da coluna A como 20
          worksheet = writer.sheets['Contagens']
          worksheet.set_column('A:A', 20, centrar)
          worksheet.set_column('B:B', 20, centrar)
          worksheet.set_column('C:C', 20, centrar)
          worksheet.set_column('D:D', 20, centrar)
          worksheet.set_column('E:E', 20, centrar)
          worksheet.set_column('F:F', 20, centrar)
          worksheet.set_column('G:G', 20, centrar)
          worksheet.set_column('H:H', 20, centrar)
          worksheet.set_column('I:I', 20, centrar)
          worksheet.set_column('J:J', 20, centrar)

main()

df_contagens = pd.read_excel('../Resultados/Contagens.xlsx', sheet_name='Contagens')

df_contagens['Total de Adjetivos'].plot(kind='hist', bins=20, title='Total de Adjetivos')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()

df_contagens['Total de Nomes Próprios'].plot(kind='hist', bins=20, title='Total de Nomes Próprios')
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()

df_contagens.plot(kind='scatter', x='Total de Nomes Próprios', y='Total de Adjetivos', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()