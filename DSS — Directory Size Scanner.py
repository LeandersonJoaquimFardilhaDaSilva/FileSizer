import os, bitmath

raiz_atual = os.getcwd()

diretorios_encontrados = list()

diretorios_com_tamanho = list()


#_____________________________________________________________________
def listar_diretorios(root_dir):
    for item in os.scandir(root_dir):
        if item.is_dir():
            diretorios_encontrados.append(item.path)
#_____________________________________________________________________

def calcular_tamanhos(diretorios):
    for diretorio in diretorios:
        tamanho_bytes = 0
        diretorio_info = {"tamanho_mib": tamanho_bytes, "caminho": diretorio}
        for raiz, subdirs, arquivos in os.walk(diretorio):
            if arquivos:
                for nome_arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, nome_arquivo)
                    tamanho_bytes += os.stat(caminho_arquivo).st_size
                    diretorio_info["tamanho_mib"] = int(bitmath.Byte(tamanho_bytes).to_MiB())
        diretorios_com_tamanho.append(diretorio_info)
#_____________________________________________________________________


listar_diretorios(raiz_atual)
calcular_tamanhos(diretorios_encontrados)

print(diretorios_com_tamanho)





