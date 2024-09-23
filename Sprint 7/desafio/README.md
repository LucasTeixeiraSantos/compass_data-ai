# Desafio
O Desafio de Filmes e séries está dividido em 5 entregas. Nesta etapa será realizada a entrega 2. Os detalhes do Desafio completo estão na Sprint 6.

## Entrega 2 
<b> Ingestão de API: </b> Nesta etapa do desafio iremos capturar dados do TMDB via AWS Lambda realizando chamadas de API. Os dados coletados devem ser persistidos em Amazon S3, camada RAW Zone, mantendo o formato da origem (JSON) e, se possíve, agrupando-os em arquivos com, no máximo, 100 registros cada arquivo. O objetivo desta etapa é complementar os dados dos Filmes e Series, carregados na Etapa 1, com dados oriundos TMDB e, opcionalmente, de outra API de sua escolha.
Abaixo uma imagem demonstrando qual é o escopo da parte 2 do Desafio.

Em sua conta AWS, no serviço AWS Lambda, realize as seguintes atividades:
- 1) Se necessário, criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados.
- 2) Implementar o código Python em AWS Lambda para consumo de dados do TMDB.
- 3) Se está utilizando TMDB, buscar pela API os dados que complemente a análise. Se achar importante, agrupar os retornos da API em arquivo JSON com, no máximo, 100 registros cada.
- 4) Utilize a lib boto3 para gravar os dados no AWS S3. <br>
  Considere o padrão: <br>
  ```
  S3:\\<nome_do_bucket>\<camada_de_armazenamento>\<origem_do_dado>\<formato_do_dado>\<especificação_do_dado>\<data_de_processamento_separada_por_ano\mes\dia>\<arquivo>
  ```
# Passos para a execução do Desafio (Windows)

## Passo 1: Instalar o Python 3.9

1. **Baixar o Instalador do Python 3.9:**
   - Acesse o site oficial do Python: [python.org](https://www.python.org/downloads/release/python-390/)
   - Clique no link para Windows e baixe o instalador correspondente (ex: `python-3.9.x-amd64.exe`).

2. **Instalar o Python:**
   - Execute o instalador baixado.
   - Marque a opção **"Add Python 3.9 to PATH"**.
   - Clique em **"Install Now"** e siga as instruções para concluir a instalação.

3. **Verificar a Instalação:**
   - Abra o Prompt de Comando (`cmd`).
   - Digite o seguinte comando e pressione Enter:
     ```bash
     python --version
     ```
   - Você deve ver uma saída semelhante a `Python 3.9.x`.

## Passo 2: Criar a estrutura da Layer para AWS Lambda
### PS: Se preferir, você pode baixar o zip da layer e pular para o passo 3:
[lambda_layer.zip](https://github.com/user-attachments/files/17101895/lambda_layer.zip)


1. **Criar a Estrutura de Diretórios:**
   - Crie uma pasta para sua Layer. Por exemplo, `C:\aws_lambda_layer`.
   - Dentro desta pasta, crie uma subpasta chamada `python`:
     ```bash
     mkdir C:\aws_lambda_layer\python
     ```

2. **Instalar as Dependências:**
   - Abra o Prompt de Comando e navegue até a pasta `python`:
     ```bash
     cd C:\aws_lambda_layer\python
     ```
   - Use o `pip` para instalar as dependências que você deseja incluir na Layer. (boto3 e aiohttp):
     ```bash
     pip install boto3 aiohttp -t .
     ```

3. **Empacotar a Layer:**
   - Volte para a pasta `aws_lambda_layer`:
     ```bash
     cd ..
     ```
   - Compacte a pasta `python` em um arquivo ZIP:
     ```bash
     powershell Compress-Archive -Path python -DestinationPath lambda_layer.zip
     ```

     ![01-layer_zip](https://github.com/user-attachments/assets/75af649f-2487-4cdc-ab1e-f1ddb47c8559)


## Passo 3: Criar a Layer na AWS Lambda

1. **Criar a Layer no AWS Lambda:**
   - Acesse o Console de Gerenciamento da AWS e vá para o serviço **Lambda**.
   - No painel esquerdo, clique em **Layers**.
   - Clique no botão **Create layer**.
   - Dê um nome à sua Layer, adicione uma descrição e faça o upload do arquivo `lambda_layer.zip` que você criou.
   - Selecione a versão do Python (3.9) e clique em **Create**.


![02-lambda_layer](https://github.com/user-attachments/assets/901e3c2a-e265-4f34-a03b-a1f54675f528)


## Passo 4: Criar a Função Lambda

   - Acesse o Console de Gerenciamento da AWS e vá para o serviço **Lambda**.
   - No painel esquerdo, clique em **Functions**.
   - Clique em **Create function**.
   - Em **Function name**, escolha um nome para a sua função.
   - Em **Runetime**, selecione **Python 3.9**
   - Abaixo, clique em **Create function**.
   - 
![03-lambda_function](https://github.com/user-attachments/assets/2e884653-abd0-460f-a11a-d7183567d60d)

## Passo 5: Adicionar a layer à função Lambda

   - Vá para a sua função Lambda criada no passo 4.
   - Clique no nome da função criada no passo 4.
   - No painel da função, role para baixo até a seção **Layers**.
   - Clique em **Add a layer**, clique em **Custom Layers** e em **Choose**, selecione a Layer que você criou.
   - Clique em **Add**.
     
![04-function_with_layer](https://github.com/user-attachments/assets/a45cb386-d181-4654-8b12-fe561ac2cb24)

## Passo 6: Copie o código Python para a Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para abaixo até a seção **Code**.
   - Clique na aba **lambda_function**
   - Copie o conteúdo do arquivo **lambda.py** que se encontra na pasta deste **README.md**.
   - Apague o conteúdo da aba **lambda_function** e cole o conteúdo do arquivo **lambda.py**.
   - Clique no botão **Deploy**.

![05-function_with_code](https://github.com/user-attachments/assets/20c191b2-6971-4059-b0f6-89ff43da85b7)

## Passo 7: Crie um evento de Teste para a Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo até a seção **Code**. 
   - Clique no botão **Test**.
   - Clique no botão **Save**.

## Passo 8: Configure as variáveis de ambiente
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo e clique na seção **Configuration**
   - No painel esquerdo, clique em *Environment Variables** 
   - Clique em **Edit**
   - Clique em **Add environment variables**.
   - Adicione as seguintes variáveis de ambiente e seu respectivo **Value**:
     - TMDB_API_KEY (Sua chave de API do TMDB)
     - S3_BUCKET (O nome do seu Bucket no S3.
     - TMDB_TYPE (Filmes ou séries, digite **movies**)
     - GENRE_ID (O id do gênero, digite **16** para consultar os filmes de animação.
  - Clique em **Save**.

![06-function_environment_variables](https://github.com/user-attachments/assets/756ff5b0-3fdf-4e1a-8f77-d25f41d80d12)

    
## Passo 9: Alterar o timeout e a Memória da Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo e clique na seção **Configurations**
   - No painel esquerdo, clique em **General configuration**.
   - Clique em **edit**.
   - Em **Memory**, altere para **256**MB.
   - Em **Timeout**, altere para **2**min e **0** sec.
   - Clique em **Save**.
     
![07-function_memory_ _timeout](https://github.com/user-attachments/assets/602a0575-d0cf-4ba0-ac27-50474f88ba87)

## Passo 10: Execute a função Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo até a seção **Code**.
   - Clique em **Test**.
   - Aguarde o resultado da Lambda.

![08-lambda_results](https://github.com/user-attachments/assets/e6615a69-dc0c-49d1-8123-6f97b5fa78b0)

## Passo 11: Verifique o resultado
   - Acesse o Console de Gerenciamento da AWS e vá para o serviço **S3**.
   - No painel esquerdo, clique em **Buckets**.
   - Clique no nome do seu bucket.
   - Siga até o caminho definido na função.

![09-bucket_s3_lambda_files](https://github.com/user-attachments/assets/3e6bb6e6-b9eb-4a69-95ae-3ba73fb67a1c)

     ![08-bucket_s3_lambda_files](https://github.com/user-attachments/assets/7b12fc1b-cfe2-4966-9105-eb2c1fc3351e)

