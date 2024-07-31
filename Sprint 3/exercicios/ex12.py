def my_map(lista, f):
    return [f(x) for x in lista]

def quadrado(x):
    return x ** 2

lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista_entrada, quadrado)
print(resultado)
