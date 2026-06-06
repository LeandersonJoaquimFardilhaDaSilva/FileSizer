import os, bitmath

path_atual = os.getcwd()

lista_de_arquivos = os.listdir()

arquivo_atual = ''
lista_de_arquivos = []
contador = 0

for itens in os.walk(path_atual):
    arquivo_atual_tamanho = 0
    if contador == 0:
        contador = 1
        continue
    if contador == 1:
        arquivo_atual = itens[0]
        contador = 2
    elif arquivo_atual not in itens[0]:
        arquivo_atual = itens[0]
    for files in itens[2]:
        arquivo = os.path.join(itens[0], files)
        arquivo_atual_tamanho += os.stat(arquivo)[6]
    if contador == 2:
        lista_de_arquivos.append([arquivo_atual, arquivo_atual_tamanho])
        contador = 3
    elif arquivo_atual != lista_de_arquivos[-1][0]:
        lista_de_arquivos.append([arquivo_atual, arquivo_atual_tamanho])
    else:
        lista_de_arquivos[-1][1] += arquivo_atual_tamanho

lista_de_arquivos.sort(key=lambda x : x[1], reverse=True)
for arquivos in lista_de_arquivos:
    arquivos[1] = int(bitmath.Byte(arquivos[1]).to_MiB())

with open('lista dos arquivos.txt', 'a', encoding='utf-8') as txt:
    txt.write('\n' + '=' * 70 + '\n')
    txt.write('RELATÓRIO DE TAMANHO DE DIRETÓRIOS\n')
    txt.write('=' * 70 + '\n\n')
    
    total_mib = 0

    for arquivo_ordenado in lista_de_arquivos:
        caminho = arquivo_ordenado[0].replace(path_atual, '')
        tamanho = arquivo_ordenado[1]
        total_mib += tamanho
        txt.write(f'{caminho:_<50} >>> {tamanho:>6} MiB\n')

    txt.write('\n' + '-' * 70 + '\n')
    txt.write(f'{"TOTAL":.<50} >>> {total_mib:>6} MiB\n')
    txt.write('-' * 70 + '\n')


#copia
"""
# %%
import os, bitmath

path_atual = os.getcwd()

print(path_atual)

# %%
lista_de_arquivos = os.listdir()
lista_de_arquivos.remove('FileSizer.ipynb')
print(lista_de_arquivos)

# %%
arquivo_atual = ''
lista_de_arquivos = []
contador = 0

for itens in os.walk(path_atual):
    arquivo_atual_tamanho = 0
    display(itens)
    if contador == 0:
        contador = 1
        continue
    if contador == 1:
        arquivo_atual = itens[0]
        contador = 2
    elif arquivo_atual not in itens[0]:
        arquivo_atual = itens[0]
    for files in itens[2]:
        print(f'join>>> {os.path.join(itens[0], files)}, <<<<<<<  1  >>>>>>>>')
        arquivo = os.path.join(itens[0], files)
        print(f'os.stat>>> {os.stat(arquivo)}, <<<<<<<  2  >>>>>>>>')
        arquivo_atual_tamanho += os.stat(arquivo)[6]
        print(arquivo_atual_tamanho, '<<<<<<<  3  >>>>>>>>')
    if contador == 2:
        lista_de_arquivos.append([arquivo_atual, arquivo_atual_tamanho])
        contador = 3
        print('<<<<<<<  4  >>>>>>>>')
    elif arquivo_atual != lista_de_arquivos[-1][0]:
        print(lista_de_arquivos[-1][0],'<<<<<<<  5  >>>>>>>>')
        lista_de_arquivos.append([arquivo_atual, arquivo_atual_tamanho])
    else:
        lista_de_arquivos[-1][1] += arquivo_atual_tamanho
        print(('<<<<<<<  6  >>>>>>>>'))



# %%

lista_de_arquivos.sort(key=lambda x : x[1], reverse=True)
for arquivos in lista_de_arquivos:
    print(arquivos)
    arquivos[1] = int(bitmath.Byte(arquivos[1]).to_MiB())
print(lista_de_arquivos, '<<<<<<<<<')


# %%
with open('lista dos arquivos.txt', 'a', encoding='utf-8') as txt:
    for arquivo_ordenado in lista_de_arquivos:
        txt.write(f'{arquivo_ordenado[0].replace(path_atual,''):_<50} >>>PENSADO:')
        txt.write(f'{arquivo_ordenado[1]}MB\n')


"""
