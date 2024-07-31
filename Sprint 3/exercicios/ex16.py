def soma(string_numeros):
    numeros = string_numeros.split(',')
    soma = sum(int(numero) for numero in numeros)
    return soma
    
    
string = "1,3,4,6,10,76"
print(soma(string))