import os
import shutil

# Caminho base para o diretório desorganizado
base_diretorio = os.path.join(os.path.expanduser("~"), "Desktop", "Análise e Visualização de Dados", "ComUM", "Etiqueta_UMinho")

# Caminho base para o diretório de destino
destino_base = os.path.join(os.path.expanduser("~"), "Desktop", "Análise e Visualização de Dados", "ComUM", "Etiqueta_UMinho_org")

# Cria o diretório de destino se não existir
if not os.path.exists(destino_base):
    os.makedirs(destino_base)

# Percorre a estrutura de diretórios
for ano in range(2013, 2025):
    ano_dir = os.path.join(base_diretorio, str(ano))
    if os.path.exists(ano_dir):
        for num_dir in os.listdir(ano_dir):
            num_dir_path = os.path.join(ano_dir, num_dir)
            if os.path.isdir(num_dir_path):
                for artigo_dir in os.listdir(num_dir_path):
                    artigo_dir_path = os.path.join(num_dir_path, artigo_dir)
                    if os.path.isdir(artigo_dir_path):
                        index_html = os.path.join(artigo_dir_path, 'index.html')
                        if os.path.exists(index_html):
                            novo_nome = os.path.join(destino_base, f'{artigo_dir}.html')
                            print(f'Movendo {index_html} para {novo_nome}')
                            shutil.move(index_html, novo_nome)
                        else:
                            print(f'index.html não encontrado em {artigo_dir_path}')
            else:
                print(f'{num_dir_path} não é um diretório')
    else:
        print(f'Diretório do ano {ano} não encontrado: {ano_dir}')
