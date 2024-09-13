# Pergunta?
## Qual a melhor série, Game of Thrones ou House of The Dragon?

# Instruções para Executar o Desafio no Windows

## 1. Edite o arquivo de credenciais da AWS
Abra o arquivo de credenciais da AWS para edição: <br>
(Altere o {seu_usuario} para o seu usuário do Windows)

```bash
notepad C:\Users\{seu_usuario}\.aws\credentials
```

Edite o arquivo com as suas credenciais da AWS: "AWS access key ID", "AWS secret access key" e "AWS session token" <br>
Ex:

```bash
[default]
aws_access_key_id=xxx
aws_secret_access_key=yyy
aws_session_token=zzz
```

## 2. Crie a imagem Docker

Para criar a imagem, utilize o seguinte comando na pasta do Dockerfile:
Ex:
```bash
docker build -t s3-uploader .	
```
## 3. Execute o container Docker

Em seguida, utilize o seguinte comando para executar o container:
```bash
docker run --rm -v "C:/Users/{seu_usuario}/{local_do_arquivo}/compass_data-ai/Sprint 6/desafio/data":/app/data -v "C:/Users/{seu_usuario}/.aws":/root/.aws s3-uploader
```

## 4. Visualize os resultados

Deverá aparecer uma barra com o Status do Upload de cada arquivo CSV e, após completar, o caminho no qual ele se encontra na AWS. Como por exemplo: <br>

![image](https://github.com/user-attachments/assets/54316699-8564-40be-87b3-3abb42884022)


