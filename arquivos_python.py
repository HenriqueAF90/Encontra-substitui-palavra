"""
Etapas
1 - Ler o arquivo txt que será gerado pelo comando cmd 
2 - Salvar cada linha do array e abrir o arquivo fazendo um busca por palavra chave
3 - Adequar ás variaveis para que a biblioteca consiga abrir esses arquivos 
4 - Ler o arquivo inteiro e procurar por uma palavra especifica
5 - substituir a palavra definida inicialmente
6 - salvar em uma outra pasta as modificações realizadas
7 - listar qual os arquivos tinham a palavra ou seja lista os que sofreram alteração

"""

from cgitb import text
from dataclasses import replace
from gettext import find
import os
from re import T, sub

#insira o caminho do arquivo que contem os caminhos dos arquivos
arquivo = open("exercicios/arquivos/read.txt", "r")
arquivo_array = []
linhas = arquivo.readlines()
# gerando um array com cada linha do arquivo
for linhas in linhas:
    arquivo_array.append(linhas)
arquivo.close()

#cria um arquivo de log para informar quals foram os arquivos alterados
arquivo_log =  open("log.txt", "w")

# conta o tamanho da lista
cont = len(arquivo_array)
# percorre toda a lista e abre cada arquivo
for c in range(cont):
    texto = arquivo_array[c][:-1]
    nome_arquivo = os.path.basename(texto)
    with open(texto, "r") as file:
        conteudo =  file.read()
        # lê o arquivo e substitui a palavra desejada 
        if "localizar" in conteudo:
            substitui = conteudo.replace("localizar", "substituir")
            
            #grava um arquivo na pasta alterados com o mesmo nome
            salva_arquivo = open(f'alterado\{nome_arquivo}', "w")
            salva_arquivo.write(substitui)
            # grava dentro do arquivo de log o caminho de onde foi encontrada a palavra solciitada
            arquivo_log.write(f'Localizado em: {texto} \n')
arquivo_log.close()
print('fim do programa')