#  Quarta etapa do Desafio Fimes e séries 

## Modelagem e Processamento de Dados - Camada Refined
A **Camada Refined** de um Data Lake é a camada onde os dados estão preparados para análise e geração de insights. Os dados dessa camada têm origem na **Camada Trusted**. Aplicaremos conceitos de **modelagem multidimensional**, estruturando os dados em um **Esquema Estrela (Star Schema)** para otimizar consultas analíticas.

## Objetivos

1. **Modelagem de Dados:**
   - Estruturar os dados seguindo a abordagem de **modelagem multidimensional** (Esquema Estrela).
   - Criar **tabelas** e, se necessário, **views** no **AWS Glue Data Catalog**, baseadas nos dados oriundos da Camada Trusted.
   - Disponibilizar os dados modelados para ferramentas de visualização, no caso, o **AWS Quicksight**.

2. **Processamento da Camada Refined:**
   - Usar **Apache Spark** para processar e transformar os dados da **Camada Trusted** de acordo com o modelo definido (Star Schema).
   - Armazenar os dados processados e refinados na **Camada Refined**.
   - Garantir que os dados estejam prontos para consultas e análises avançadas.

## Etapas

1. **Modelar e visualizar os dados**
   - Utilizar uma ferramenta para modelar e criar o diagrama no formato **Star Schema**
   - Foi utilizado o **Power Bi**. Outras opções são: **Lucidchart**, **dbdiagram.io**, **Draw.io**, etc.
     
2. **Modelagem no AWS Glue Data Catalog e Criação da camada Refined:**
   - Utilizar o AWS Glue para:
     - Transformação dos dados usando **Apache Spark**, com origem na Camada Trusted.
     - Organizar os dados para permitir análises multi-dimensionais no **Quicksight**.
     - Armazenamento dos dados refinados na Camada Refined para análises.
  
   
## Execução das Etapas

1. **Modelar e visualizar os dados** **(Power BI)
   - Importe as tabelas.
   - Crie a Tabela Fato e as tabelas Dimensões. <br>
   ![image](https://github.com/user-attachments/assets/0a5cbe84-add0-4677-a589-7a68b84d3474)
   - Na lateral esquerda, clique no ícone a seguir para acessar o **Model View**. <br>
   ![image](https://github.com/user-attachments/assets/f22242e3-016e-48c1-8b1b-3089c78c7e88)
   - Visualize o diagrama. <br>
   ![image](https://github.com/user-attachments/assets/fd81f1c0-b0b8-47df-91b4-9c7a6b38ef5a)

2.  **Modelagem no AWS Glue Data Catalog e Criação da camada Refined:**
    - Acesse o **console** da AWS.
    - Acesse o serviço **AWS Glue**. <br>
     ![image](https://github.com/user-attachments/assets/f7a97ad1-40bf-4b1e-a45e-6dc18f5cd314)
    - No canto direito, acesse a opção **Author and edit ETL jobs**. <br>
     ![image](https://github.com/user-attachments/assets/d4500a84-98fb-4f5c-9e1b-08a1c80ee473)
    - **Alternativa a última etapa**: Na barra lateral esquerda, acesse **ETL jobs**. <br>
    ![image](https://github.com/user-attachments/assets/fbd42765-ed13-4a4f-a3b4-28666ce3809c)
    - No canto direito, clique em **Script editor**. <br>
     ![image](https://github.com/user-attachments/assets/846c8e25-6ebe-4280-a29f-1f3f36301a36)
    - Utilize as configurações a seguir e clique em **Create script**. <br>
     ![image](https://github.com/user-attachments/assets/e24ace14-4cd0-4ecd-a35a-c9b82b453755)
    - Clique em **Job details**. <br>
     ![image](https://github.com/user-attachments/assets/15e44e7c-a6cf-452f-bcfa-97bed700abf3)
    - Altere as seguintes configurações:
       - **Name:** Escolha um nome para o Job. <br>
        ![image](https://github.com/user-attachments/assets/040bfbc6-6226-4dc6-8389-f475318d49de)
       - **IAM Role:** Escolha uma role com permissão para o Glue, S3 e Cloudwatch. <br>
       ![image](https://github.com/user-attachments/assets/eac1db18-1441-4b85-b720-dcb260a64211)
       - **Requested number of workers**: Coloque 2 (o menor número de workers permitido). <br>
       ![image](https://github.com/user-attachments/assets/6815acd3-5ed8-4a85-9e41-f059993413b8)
       - **Job timeout (minutes)**: Coloque 5. <br>
        ![image](https://github.com/user-attachments/assets/d53a8bdd-5284-4b34-9a82-0c196e10c932)
    - No canto superior direito, clique em **Save**. <br>
    ![image](https://github.com/user-attachments/assets/16259311-43fc-4ef1-8088-192fed8ea335)
     Volte para a sessão **Script**, ao lado de **Job details**. <br>
    ![image](https://github.com/user-attachments/assets/514cacb2-f5a8-4a57-ad9a-882a4a0a19e3)
    - Abra o arquivo **refined_glue_job.py**.
    - Copie e cole no **Job** do Glue. <br> 
     ![image](https://github.com/user-attachments/assets/a8796fdc-faf5-41c6-af60-82f69cd014f5)
    - No canto superior direito, clique em **Run**. <br>
     ![image](https://github.com/user-attachments/assets/925ff091-56fc-4d57-8e18-e866dabed3c7)
    - Ao lado do **Job details**, clique em **Runs** <br>
     ![image](https://github.com/user-attachments/assets/d06c0624-5bfa-49f2-b457-4f68a9745f05)
    - O Job vai estar como **Running**, aguarde ele concluir. <br>
     ![image](https://github.com/user-attachments/assets/e34d4a6a-61e5-4da7-b449-a6aa07c85c66) <br>
     ![image](https://github.com/user-attachments/assets/7bae47d8-63b8-43d4-b46c-f5e8e3e19e48)
    - Acesse o **Amazon Athena**. <br>
    ![image](https://github.com/user-attachments/assets/fcb858df-dad0-4e7a-9639-75ac804a1d86)
    - Rode o seguinte script para criar o database.
    ```sql
    CREATE DATABASE IF NOT EXISTS datalake_pb_lucas;
    ```
    - Rode o seguinte script para criar a tabela **dim_artist**.
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS datalake_pb_lucas.dim_artist (
      artist_name STRING,
      artist_gender STRING,
      artist_birth_year INT,
      artist_death_year INT,
      artist_profession STRING,
      id_artist_name BIGINT
    )
    STORED AS PARQUET
    LOCATION 's3://data-lake-lucas-ts/Refined/PARQUET/dim_artist/'
    TBLPROPERTIES ('parquet.compress'='SNAPPY');
    ```
    - Rode o seguinte script para criar a tabela **dim_calendar**.
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS datalake_pb_lucas.dim_calendar (
      date DATE,
      year INT,
      month INT,
      day INT
    )
    STORED AS PARQUET
    LOCATION 's3://data-lake-lucas-ts/Refined/PARQUET/dim_calendar/'
    TBLPROPERTIES ('parquet.compress'='SNAPPY');
    ```
    - Rode o seguinte script para criar a tabela **dim_character**.
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS datalake_pb_lucas.dim_character (
      artist_character STRING,
      id_character BIGINT
    )
    STORED AS PARQUET
    LOCATION 's3://data-lake-lucas-ts/Refined/PARQUET/dim_character/'
    TBLPROPERTIES ('parquet.compress'='SNAPPY');
    ```
    - Rode o seguinte script para criar a tabela **dim_movie**.
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS datalake_pb_lucas.dim_movie (
      title STRING,
      path_backdrop STRING,
      title_original STRING,
      overview STRING,
      path_poster STRING,
      tagline STRING,
      id_movie BIGINT
    )
    STORED AS PARQUET
    LOCATION 's3://data-lake-lucas-ts/Refined/PARQUET/dim_movie/'
    TBLPROPERTIES ('parquet.compress'='SNAPPY');
    ```
    - Rode o seguinte script para criar a tabela **fact_movies**.
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS datalake_pb_lucas.fact_movies (
      id_tmdb STRING,
      id_imdb STRING,
      vote_average_imdb DOUBLE,
      vote_count_imdb INT,
      release_date DATE,
      revenue BIGINT,
      runtime INT,
      vote_average_tmdb DOUBLE,
      vote_count_tmdb INT,
      budget BIGINT,
      id_movie BIGINT,
      id_artist_name BIGINT,
      id_character BIGINT
    )
    STORED AS PARQUET
    LOCATION 's3://data-lake-lucas-ts/Refined/PARQUET/fact_movies/'
    TBLPROPERTIES ('parquet.compress'='SNAPPY');
    ```
  - No canto esquerdo, em **Tables**, visualize as tabelas criadas. <br>
  ![image](https://github.com/user-attachments/assets/320c65a1-3c1a-4ad5-8e1f-8a0a47f67df0) <br>
  ![image](https://github.com/user-attachments/assets/0a9ed8f8-7a89-4acd-b271-8f7213aed6a5) <br>
  ![image](https://github.com/user-attachments/assets/44a4e8f9-bf93-4801-bd58-4dfbeaad7eb2) <br>
  ![image](https://github.com/user-attachments/assets/2fd3547c-0106-4a90-986a-9bceaced3ea3) <br> 
  ![image](https://github.com/user-attachments/assets/98c73ed2-ecee-400f-92c3-00a55dbfa312) <br> 


  


    
    

    















    



    


