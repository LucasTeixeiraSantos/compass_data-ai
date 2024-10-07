# Etapa 1

```py
lista_inteiros = [random.randint(0, 1000) for _ in range(250)]
lista_inteiros.reverse()
print("Lista de Inteiros:", lista_inteiros)
```

![image](https://github.com/user-attachments/assets/eb735021-a770-497a-a284-d2acb34a5fac)

# Etapa 2

```py
lista_animais = ['Cachorro', 'Gato', 'Leão', 'Tigre', 'Elefante', 'Girafa', 'Cavalo', 'Pinguim', 'Urso', 'Raposa',
                 'Lobo', 'Canguru', 'Golfinho', 'Foca', 'Tartaruga', 'Águia', 'Leopardo', 'Baleia', 'Corvo', 'Coelho']
lista_animais.sort()

for animal in lista_animais:
    print(animal)

caminho_arquivo_animais = '/content/animais.csv'

with open(caminho_arquivo_animais, 'w', encoding='utf-8') as file:
    for animal in lista_animais:
        file.write(animal + '\n')
```
![image](https://github.com/user-attachments/assets/fda40f95-c981-486a-bb1a-245a25aa197d)

# Etapa 3
  - Passo 1
```py
# !pip install names
```

  - Passo 2

```py
import random, time, os, names
```

  - Passo 3

```py
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000
```
  - Passo 4

```py
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]
print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]
```

![image](https://github.com/user-attachments/assets/d2264bee-e237-4502-8d7a-a05322757e50)

  - Passo 5

```py
caminho_arquivo_nomes = '/content/nomes_aleatorios.txt'

with open(caminho_arquivo_nomes, 'w', encoding='utf-8') as file:
    for nome in dados:
        file.write(nome + '\n')

with open(caminho_arquivo_nomes, 'r', encoding='utf-8') as file:
    print("Primeiros 10 nomes aleatórios gerados:")
    print(file.readlines()[:10])
```

![image](https://github.com/user-attachments/assets/83fee7f2-0db9-4685-beaf-96fc81acc08b)

  - Passo 6

![image](https://github.com/user-attachments/assets/2f3b3ce0-080f-4dbe-84ff-e8c9df5e2b27)
