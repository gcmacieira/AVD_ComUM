import os
import shutil

# Defina os caminhos das pastas de origem
pasta_entrevista_clean = 'C:/Users/Maria Francisca/Desktop/Análise e Visualização de Dados/ComUM/Etiqueta_Entrevista_clean'
pasta_uminho_clean = 'C:/Users/Maria Francisca/Desktop/Análise e Visualização de Dados/ComUM/Etiqueta_UMinho_clean'
pasta_universidade_do_minho_clean = 'C:/Users/Maria Francisca/Desktop/Análise e Visualização de Dados/ComUM/Etiqueta_UniversidadeDoMinho_clean'

# Defina o caminho da pasta de destino
pasta_destino = 'C:/Users/Maria Francisca/Desktop/Análise e Visualização de Dados/ComUM/Artigos_ComUM'

# Criar a pasta de destino se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Função para copiar arquivos únicos de uma pasta para a pasta de destino
def copiar_arquivos_unicos(pasta_origem, arquivos_copiados):
    for file in os.listdir(pasta_origem):
        if file.endswith('.html'):
            caminho_arquivo_origem = os.path.join(pasta_origem, file)
            if file not in arquivos_copiados:
                caminho_arquivo_destino = os.path.join(pasta_destino, file)
                shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)
                arquivos_copiados.add(file)
                print(f'Arquivo copiado: {file}')
            else:
                print(f'Arquivo duplicado não copiado: {file}')

# Conjunto para armazenar os nomes dos arquivos já copiados
arquivos_copiados = set()

# Copiar arquivos únicos de cada pasta de origem
copiar_arquivos_unicos(pasta_entrevista_clean, arquivos_copiados)
copiar_arquivos_unicos(pasta_uminho_clean, arquivos_copiados)
copiar_arquivos_unicos(pasta_universidade_do_minho_clean, arquivos_copiados)

print(f'Total de arquivos copiados para {pasta_destino}: {len(arquivos_copiados)}')
