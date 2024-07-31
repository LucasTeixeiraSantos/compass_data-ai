def elementos_repetidos(lista):
    conjunto = set(lista)
    repetidos = [item for item in conjunto if lista.count(item) > 1]
    return repetidos

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '12']

resultado = elementos_repetidos(lista_teste)
print(resultado)
