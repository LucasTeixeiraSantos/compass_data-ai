import boto3


def carregar_sql(arquivo_sql):
    with open(arquivo_sql, 'r') as arquivo:
        return arquivo.read()

query = carregar_sql('Sprint 5/desafio/consulta.sql')

s3_client = boto3.client('s3')


response = s3_client.select_object_content(
    Bucket='pb-sprint05-lts',
    Key='arquivo_tratado.csv',
    ExpressionType='SQL',
    Expression=query,
    InputSerialization={'CSV': {'FileHeaderInfo': 'USE', 'FieldDelimiter': ';'}},
    OutputSerialization={'CSV': {}},
)

for event in response['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode('utf-8'))