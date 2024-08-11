def conta_vogais(texto:str)-> int:
    texto = texto.lower()
    vogais = 'aeiou'
    
    filtro_vogais = filter(lambda char: char in vogais, texto)
    
    return len(list(filtro_vogais))
