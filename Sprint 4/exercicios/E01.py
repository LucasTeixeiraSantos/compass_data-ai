with open('number.txt') as n:
    numeros = list(map(int, n.readlines()))

pares = list(filter(lambda x: x % 2 == 0, numeros))
pares_ordenados = sorted(pares, reverse=True)
cinco_maiores_pares = pares_ordenados[:5]
soma_cinco_maiores = sum(cinco_maiores_pares)

print(cinco_maiores_pares)
print(soma_cinco_maiores)
