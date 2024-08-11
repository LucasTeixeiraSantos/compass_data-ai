def maiores_que_media(conteudo: dict) -> list:
    precos = list(conteudo.values())
    media = sum(precos) / len(precos)
    
    produtos_acima_media = {
        nome: preco for nome, preco in conteudo.items() if preco > media
    }
    
    produtos_ordenados = sorted(produtos_acima_media.items(), key=lambda x: x[1])
    
    return produtos_ordenados
