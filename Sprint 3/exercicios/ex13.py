nome_arquivo = 'arquivo_texto.txt'

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

    print(conteudo, end='')
