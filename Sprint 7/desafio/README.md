# Desafio da Sprint 7

# Pergunta

# 1. Objetivo
O objetivo é praticar a combinação de conhecimentos vistos no programa, fazer um mix de tudo que já foi dito.

# 2. Entregáveis

- Todo o código, comentários, evidências e demais artefatos desenvolvidos para resolver o desafio devem estar comitados no Git de forma organizada.
- Arquivo Markdown com evidências imagens/prints de realização do desafio, bem como documentação de explicação de cada parte executada
  - Explicação dos motivadores de cada API.
  - Explicitar suas questões que serão respondidas na última etapa do desafio.
- Código desenvolvido com devidos comentários.
  - Arquivo contendo código Python no formato .PY representando a Lambda.

# 3. Preparação

- Antes de começar certifique-se que possui o entendimento completo do Desafio de Filmes e Series.

# 4. Desafio
O Desafio de Filmes e séries está dividido em 5 entregas. Nesta etapa será realizada a entrega 2. Os detalhes do Desafio completo estão na Sprint 6.

## 4.1. Entrega 2 
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

## Passo 3: Criar a Layer na AWS Lambda

1. **Criar a Layer no AWS Lambda:**
   - Acesse o Console de Gerenciamento da AWS e vá para o serviço **Lambda**.
   - No painel esquerdo, clique em **Layers**.
   - Clique no botão **Create layer**.
   - Dê um nome à sua Layer, adicione uma descrição e faça o upload do arquivo `lambda_layer.zip` que você criou.
   - Selecione a versão do Python (3.9) e clique em **Create**.

## Passo 4: Criar a Função Lambda

   - Acesse o Console de Gerenciamento da AWS e vá para o serviço **Lambda**.
   - No painel esquerdo, clique em **Functions**.
   - Clique em **Create function**.
   - Em **Function name**, escolha um nome para a sua função.
   - Em **Runetime**, selecione **Python 3.9**
   - Abaixo, clique em **Create function**.

## Passo 5: Adicionar a layer à função Lambda

   - Vá para a sua função Lambda criada no passo 4.
   - Clique no nome da função criada no passo 4.
   - No painel da função, role para baixo até a seção **Layers**.
   - Clique em **Add a layer**, clique em **Custom Layers** e em **Choose**, selecione a Layer que você criou.
   - Clique em **Add**.

## Passo 6: Copie o código Python para a Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para abaixo até a seção **Code**.
   - Clique na aba **lambda_function**
   - Copie o conteúdo do arquivo **lambda.py** que se encontra na pasta deste **README.md**.
   - Apague o conteúdo da aba **lambda_function** e cole o conteúdo do arquivo **lambda.py**.
   - Clique no botão **Deploy**.

## Passo 7: Crie um evento de Teste para a Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo até a seção **Code**. 
   - Clique no botão **Test** em azul.
   - Clique no botão **Save** em laranja.

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
    
## Passo 9: Alterar o timeout e a Memória da Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo e clique na seção **Configurations**
   - No painel esquerdo, clique em **General configuration**.
   - Clique em **edit**.
   - Em **Memory**, altere para **256**MB.
   - Em **Timeout**, altere para **2**min e **0** sec.
   - Clique em **Save**.

## Passo 10: Execute a função Lambda
   - Vá para a sua função Lambda.
   - No painel da função, role para baixo até a seção **Code**.
   - Clique em **Test**.
   - Aguarde o resultado da Lambda.

## 
