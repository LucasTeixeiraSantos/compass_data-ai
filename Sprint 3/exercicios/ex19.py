import random

random_list = random.sample(range(500), 50)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

media = sum(random_list) / len(random_list)

sorted_list = sorted(random_list)

if len(sorted_list) % 2 == 0:
    mid_index = len(sorted_list) // 2
    mediana = (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
else:
    mid_index = len(sorted_list) // 2
    mediana = sorted_list[mid_index]

print(f"Media: {media}",end = ", ")
print(f"Mediana: {mediana}",end = ", ")
print(f"Mínimo: {valor_minimo}",end = ", ")
print(f"Máximo: {valor_maximo}")

