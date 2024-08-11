import csv

def processar_estudantes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        dados = list(leitor)
    
    def calcular_media_maiores_notas(notas):
        notas = sorted(notas, reverse=True)[:3]
        media = round(sum(notas) / len(notas), 2)
        return notas, media

    def formatar_resultado(nome, notas, media):
        notas_formatadas = [int(nota) if nota.is_integer() else nota for nota in notas]
        return f"Nome: {nome} Notas: {notas_formatadas} Média: {media}"

    resultados = [
        (
            linha[0],  
            calcular_media_maiores_notas(list(map(float, linha[1:]))),  
        )
        for linha in dados
    ]
    
    resultados_ordenados = sorted(resultados, key=lambda x: x[0])
    
    for nome, (notas, media) in resultados_ordenados:
        print(formatar_resultado(nome, notas, media))


processar_estudantes('estudantes.csv')
