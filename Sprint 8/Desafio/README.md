# Terceira etapa do Desafio Filmes e Séries

# Processamento da Camada Trusted
  - <b> Integração de Dados: </b> Utilizamos o Apache Spark por meio do serviço AWS Glue para realizar a integração dos dados de múltiplas fontes da camada Raw. Durante esse processo, os dados passam por uma série de transformações, como limpeza, padronização e junção entre diferentes datasets, assegurando que estejam prontos para serem consumidos de forma confiável.
  - <b> Qualidade e Limpeza: </b> Todos os dados na camada Trusted são tratados para eliminar inconsistências, remover valores nulos e garantir que cada campo esteja no tipo correto. 
  - <b> Armazenamento Eficiente: </b> Os dados são salvos em formato Parquet, um formato colunar otimizado para armazenamento e processamento em grande escala. O Parquet oferece compressão eficiente e leitura seletiva de colunas, o que resulta em melhor desempenho em consultas.

# Questões
  - Quais são os filmes com melhor avaliação do Studio Ghibli?
  - Quais são os filmes com melhor avaliação do Studio Ghibli por década?
  - Quais são os filmes mais rentáveis do Studio Ghibli?
  - Qual a tendência de orçamento e retorno ao longo dos anos?
  - Existe correlação entre a avaliação e a rentabilidade dos filmes?

# Motivadores das API's
## TMDB
  - Dados base de onde extraímos as seguintes informações dos filmes do Studio Ghibli:
    
    - id_tmdb
    - id_imdb
    - title_original
    - title
    - release_date
    - runtime
    - overview
    - tagline
    - vote_count_tmdb
    - vote_average_tmdb
    - budget
    - revenue
    - genres
    - path_backdrop
    - path_poster
   
## IMDB
  - Dados complementares de onde extraímos, principalmente, informações dos artistas envolvidos nos filmes do Studio Ghibli.
    
    - artist_death_year
    - artist_birth_year
    - artist_gender
    - artist_name
    - vote_average_imdb
    - vote_count_imdb
    - artist_character
    - artist_profession


# Explicação do Script AWS Glue - Tratamento e Transformação de Dados

## 1. Importação de Bibliotecas

```python
import sys
import boto3
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import trim, col, when, to_date, lower, lit
from pyspark.sql.types import StringType
```
Neste trecho, importamos as bibliotecas necessárias, incluindo `boto3` para acessar o **S3**, funções do **PySpark** e utilitários do **AWS Glue**.

## 2. Inicialização do Glue e Spark

```python
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)
```

Aqui inicializamos o contexto do **Glue** e do **Spark**. O contexto **Glue** permite acessar os recursos do AWS Glue, enquanto o **Spark** gerencia as operações de transformação dos dados. O objeto `job` é criado para gerenciar o estado do job Glue.

## 3. Definição dos Caminhos S3

```python
RAW_JSON_PATH = "s3://data-lake-lucas-ts/Raw/TMDB/JSON/"
RAW_CSV_PATH = "s3://data-lake-lucas-ts/Raw/Local/CSV/Movies/"
TRUSTED_OUTPUT_PATH = "s3://data-lake-lucas-ts/Trusted/PARQUET/"
```

Aqui definimos as variáveis que apontam para os diretórios S3 contendo os dados brutos (Raw) e onde os dados transformados serão salvos (Trusted).

## 4. Função para Listar Arquivos no S3

```python
def list_s3_files(bucket_prefix):
    s3_client = boto3.client('s3')
    bucket = bucket_prefix.split('/')[2]
    prefix = '/'.join(bucket_prefix.split('/')[3:])
    
    result = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return [
        f"s3://{bucket}/{obj['Key']}" 
        for obj in result.get('Contents', []) 
        if obj['Key'].endswith(('json', 'csv'))
    ]
```

Esta função usa o cliente **Boto3** para listar os arquivos dentro de um bucket S3. Apenas os arquivos com extensão `.json` e `.csv` são retornados.

## 5. Função para Ler e Unir Arquivos

```python
def read_and_union_files(file_paths, file_type):
    union_df = None
    for file in file_paths:
        df = spark.read.json(file) if file_type == 'json' else spark.read.csv(file, sep='|', header=True, inferSchema=True)
        union_df = df if union_df is None else union_df.union(df)
    return union_df
```

Esta função recebe uma lista de caminhos de arquivos e o tipo (JSON ou CSV). Os arquivos são lidos e unidos em um único DataFrame. Para CSV, os parâmetros `sep`, `header`, e `inferSchema` são definidos para garantir a leitura correta.

## 6. Função para Limpar Dados

```python
def clean_dataframe(df):
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
    return df
```

A função `clean_dataframe` percorre as colunas do DataFrame e remove os espaços em branco nas colunas do tipo **String**.

## 7. Função para Substituir Valores Nulos

```python
def replace_nulls(df):
    for column in df.columns:
        df = df.withColumn(
            column, 
            when((col(column) == r"\N") | (col(column) == ""), None).otherwise(col(column))
        )
    return df
```

Esta função substitui valores nulos (`\N` ou strings vazias) por **null** em cada coluna do DataFrame.

## 8. Leitura e Limpeza de Arquivos

```python
json_files = list_s3_files(RAW_JSON_PATH)
csv_files = list_s3_files(RAW_CSV_PATH)

movies_details_df = read_and_union_files(json_files, 'json')
movies_csv_df = read_and_union_files(csv_files, 'csv')

movies_details_df = clean_dataframe(movies_details_df)
movies_csv_df = clean_dataframe(movies_csv_df)
```

Neste ponto, os arquivos JSON e CSV são listados, lidos, unidos e limpos usando as funções definidas anteriormente.

## 9. Transformações e Join dos Dados

```python
movies_csv_df = movies_csv_df.withColumnRenamed("id", "imdb_id")

result_df = movies_details_df.join(movies_csv_df, on='imdb_id', how='left')
```

Aqui, a coluna `id` do CSV é renomeada para `imdb_id` e depois é feita a junção dos dados entre JSON e CSV.

## 10. Seleção e Transformação de Colunas

```python
result_df = result_df.select(
    col('anoFalecimento').cast('int').alias('artist_death_year'),
    col('anoNascimento').cast('int').alias('artist_birth_year'),
    col('backdrop_path').cast('string').alias('path_backdrop'),
    lower(col('generoArtista')).cast('string').alias('artist_gender'),
    col('id').cast('string').alias('id_tmdb'),
    col('imdb_id').cast('string').alias('id_imdb'),
    col('nomeArtista').cast('string').alias('artist_name'),
    col('notaMedia').cast('double').alias('vote_average_imdb'),
    col('numeroVotos').cast('int').alias('vote_count_imdb'),
    col('original_title').cast('string').alias('title_original'),
    col('overview').cast('string').alias('overview'),
    col('personagem').cast('string').alias('artist_character'),
    col('poster_path').cast('string').alias('path_poster'),
    col('profissao').cast('string').alias('artist_profession'),
    to_date(col('release_date'), 'yyyy-MM-dd').alias('release_date'),
    col('revenue').cast('bigint').alias('revenue'),
    col('runtime').cast('int').alias('runtime'),
    col('tagline').cast('string').alias('tagline'),
    col('title').cast('string').alias('title'),
    col('vote_average').cast('double').alias('vote_average_tmdb'),
    col('vote_count').cast('int').alias('vote_count_tmdb'),
    col('budget').cast('bigint').alias('budget')
)
```

As colunas relevantes são selecionadas e convertidas para os tipos de dados corretos usando a função **cast**.

## 11. Substituição de Valores Nulos e Ordenação

```python
result_df = replace_nulls(result_df)

result_df = result_df.orderBy(col('vote_count_tmdb').desc())
```

Substituímos os valores nulos e ordenamos o DataFrame pela contagem de votos no **TMDB**.

## 12. Adição de Colunas de Partição

```python
current_date = datetime.now()
result_df = result_df.withColumn("year", lit(current_date.year)).withColumn("month", lit(current_date.month)).withColumn("day", lit(current_date.day))
```

Colunas de partição `year`, `month`, e `day` são adicionadas com a data atual.

## 13. Salvamento do DataFrame no S3

```python
result_df.write.mode("overwrite").partitionBy("year", "month", "day").parquet(TRUSTED_OUTPUT_PATH)
```

Os dados transformados são salvos no **S3** no formato **Parquet**, particionados por ano, mês e dia.

## 14. Commit do Job

```python
job.commit()
```

Por fim, o job do Glue é finalizado com o comando `job.commit()`.

# Criação de execução do Job no Glue

  ## 1. Criação do Script no AWS Glue:
  - 1.1 No console AWS, pesquise pelo serviço <b> AWS Glue </b> e selecione-o. <br>
    ![image](https://github.com/user-attachments/assets/51116ba3-caec-4cbf-be92-fde9ebc6bc07)

  - 1.2 Na aba lateral esquerda, clique em <b> ETL jobs </b>. <br>
    ![image](https://github.com/user-attachments/assets/daa8cd57-0485-40fd-9bf7-918ed347726c)

  - 1.3 Clique em <b> Script Editor </b>. <br>
    ![image](https://github.com/user-attachments/assets/f3b05962-eee3-448d-bd7e-a157ee72c89e)

  - 1.4 Clique em <b> Create Script </b>. <br>
    ![image](https://github.com/user-attachments/assets/3dcbdb55-3f63-402a-9a05-5700f01199c5)

  - 1.5 Na aba <b> Job details </b>, faça o seguinte:
    - Em <b> Name </b>, digite um nome para o seu job.
    - Em <b> IAM Role </b>, selecione uma role com permissões para o S3 e o Glue. 
    - Em <b> Requested number of workers </b>, altere para 2.
    - Em <b> Job timeout (minutes) </b>, altere para 5.
      
  - 1.6 No canto superior direito, clique em <b> Save </b>. <br>
    ![image](https://github.com/user-attachments/assets/747f2795-d6d0-4044-9ef2-8176faae2421)

## 2. Execução do script:
  - 2.1 Em seu script, clique em </b> Script <br>. <b>
    ![image](https://github.com/user-attachments/assets/b4adfe15-1bd4-4008-920f-83bdfbf56ded)
   
  - 2.2 Abra o arquivo <b> etl_trusted.py </b>, copie seu conteúdo e substitua o conteúdo presente no script. <b>
    ![image](https://github.com/user-attachments/assets/24219b6b-a095-4ab7-bc86-b38025d7c75b)

  - 2.3 No canto superior direito, clique em <b> Save </b>, aguarde um instante e clique em <b> Run </b>. <br>
    ![image](https://github.com/user-attachments/assets/6a438cfb-1281-4ac6-aae9-c42887346177)

  - 2.4 No seu script, clique em <b> Runs </b>. <br>
    ![image](https://github.com/user-attachments/assets/2609c080-2cd6-44bc-aeca-0aba50d58390)

  - 2.5 Aguarde o Status da execução estar como <b> Succeeded </b>.  <br>
    ![image](https://github.com/user-attachments/assets/80780fcb-0897-4c25-a6a4-2c2071ceb7b6)

## 3. Visualização dos dados no Athena
  
  ### 3.1 No Query Editor do Amazon Athena, rode a seguinte query para criar a tabela:
```SQL
CREATE EXTERNAL TABLE IF NOT EXISTS default.table_test (
    artist_death_year INT,
    artist_birth_year INT,
    path_backdrop STRING,
    artist_gender STRING,
    id_tmdb STRING,
    id_imdb STRING,
    artist_name STRING,
    vote_average_imdb DOUBLE,
    vote_count_imdb INT,
    title_original STRING,
    overview STRING,
    artist_character STRING,
    path_poster STRING,
    artist_profession STRING,
    release_date DATE,
    revenue BIGINT,
    runtime INT,
    tagline STRING,
    title STRING,
    vote_average_tmdb DOUBLE,
    vote_count_tmdb INT,
    budget BIGINT
)
PARTITIONED BY (year INT, month INT, day INT)
STORED AS PARQUET
LOCATION 's3://data-lake-lucas-ts/Trusted/PARQUET/'
TBLPROPERTIES ("parquet.compression"="SNAPPY");
```
![image](https://github.com/user-attachments/assets/a015ca12-ac06-4590-9b09-45278af23b47)

  ### 3.2 Utilize a seguinte query para que o Athena reconheça as partições:
```SQL
MSCK REPAIR TABLE default.table_test;
```
![image](https://github.com/user-attachments/assets/22ec51be-5ec7-42c0-9ff4-5b52457af001)

## 3.3 Utilize a seguinte query para visualizar os dados da tabela:
```SQL
SELECT * FROM "default"."table_test" limit 10;
```
![image](https://github.com/user-attachments/assets/38bc4a1d-0c52-40d5-bab1-ad9a9bebd375)
