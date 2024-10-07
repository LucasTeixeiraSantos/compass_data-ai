# !pip install names

import os
import random
import names

lista_inteiros = [random.randint(0, 1000) for _ in range(250)]
lista_inteiros.reverse()
print("Lista de Inteiros:", lista_inteiros)

lista_animais = ['Cachorro', 'Gato', 'Leão', 'Tigre', 'Elefante', 'Girafa', 'Cavalo', 'Pinguim', 'Urso', 'Raposa',
                 'Lobo', 'Canguru', 'Golfinho', 'Foca', 'Tartaruga', 'Águia', 'Leopardo', 'Baleia', 'Corvo', 'Coelho']
lista_animais.sort()

print("Lista de Animais:")
for animal in lista_animais:
    print(animal)

caminho_arquivo_animais = '/content/animais.csv'

with open(caminho_arquivo_animais, 'w', encoding='utf-8') as file:
    for animal in lista_animais:
        file.write(animal + '\n')

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]
print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

caminho_arquivo_nomes = '/content/nomes_aleatorios.txt'

with open(caminho_arquivo_nomes, 'w', encoding='utf-8') as file:
    for nome in dados:
        file.write(nome + '\n')

with open(caminho_arquivo_nomes, 'r', encoding='utf-8') as file:
    print("Primeiros 10 nomes aleatórios gerados:")
    print(file.readlines()[:10])
