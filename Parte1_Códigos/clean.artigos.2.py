import os
import shutil

# Definir os caminhos dos diretórios de origem e destino
base_diretorio = os.path.join(os.path.expanduser("~"), "Desktop", "Análise e Visualização de Dados", "ComUM", "Etiqueta_UMinho_org")

destino_base = os.path.join(os.path.expanduser("~"), "Desktop", "Análise e Visualização de Dados", "ComUM", "Etiqueta_UMinho_clean")

# Palavras-chave para identificar artigos que não devem ser incluídos
palavras_chave_exclusao = ['arquivo', 'perfil', 'abc braga']

# Função para verificar se um arquivo contém alguma das palavras-chave de exclusão
def contem_palavras_chave(caminho_arquivo, palavras_chave):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            for palavra in palavras_chave:
                if palavra in conteudo:
                    return True
    except Exception as e:
        print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
    return False

# Criar o diretório de destino se não existir
os.makedirs(destino_base, exist_ok=True)

# Percorrer a estrutura de diretórios e analisar os arquivos
for root, dirs, files in os.walk(base_diretorio):
    for file in files:
        if file.endswith('.html'):  # Verifica se é um arquivo HTML
            caminho_arquivo = os.path.join(root, file)
            if not contem_palavras_chave(caminho_arquivo, palavras_chave_exclusao):
                # Definir o caminho de destino
                caminho_destino = os.path.join(destino_base, os.path.relpath(caminho_arquivo, base_diretorio))
                # Criar diretórios de destino se não existirem
                os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
                # Copiar o arquivo
                shutil.copy2(caminho_arquivo, caminho_destino)
                print(f'Arquivo copiado: {caminho_arquivo} para {caminho_destino}')
            else:
                print(f'Arquivo contém palavras-chave de exclusão: {caminho_arquivo}')
