import os
import random
import names

# Gerar uma lista de 250 inteiros aleatórios
lista_inteiros = [random.randint(0, 1000) for _ in range(250)]

# Inverter a lista
lista_inteiros.reverse()

# Imprimir o resultado
print(lista_inteiros)

# Lista de 20 animais
lista_animais = ['Cachorro', 'Gato', 'Leão', 'Tigre', 'Elefante', 'Girafa', 'Cavalo', 'Pinguim', 'Urso', 'Raposa',
                 'Lobo', 'Canguru', 'Golfinho', 'Foca', 'Tartaruga', 'Águia', 'Leopardo', 'Baleia', 'Corvo', 'Coelho']

# Ordenar a lista em ordem crescente
lista_animais.sort()

# Iterar e imprimir os animais
[print(animal) for animal in lista_animais]

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, 'animais.csv')
# Salvar os itens em um arquivo CSV
with open(caminho_arquivo, 'w', encoding='utf-8') as file:
    for animal in lista_animais:
        file.write(animal + '\n')



# Definir semente de aleatoriedade e parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gerar nomes únicos
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

# Gerar nomes aleatórios
dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

# Obter o diretório do script atual

# Definir o caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_atual, 'nomes_aleatorios.txt')

# Salvar os nomes no arquivo
with open(caminho_arquivo, 'w') as file:
    for nome in dados:
        file.write(nome + '\n')

# Verificação: Abrir e ler o arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    print(file.readlines()[:10])  # Imprimir as primeiras 10 linhas para verificação
