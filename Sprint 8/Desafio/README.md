# Terceira etapa do Desafio Filmes e Séries

# Entregáveis
  - Todo o código, comentários, evidências e demais artefatos desenvolvidos para resolver o desafio, de forma organizada.
  - Arquivo Markdown com evidências da realização do desafio, bem como documentação de explicação de cada parte executada.
    - Explicação dos motivadores de cada API.
    - Explicitar suas questões que serão respondidas na última etapa do desafio.
  - Código desenvolvido com devidos comentários
    - Arquivo contendo código Python no formato .PY representando código AWS Glue para JSON e CSV.

# Processamento Camada Trusted
  - A camada Trusted é resultado da integração das diversas fontes de origem, que encontram-se na camada Raw. É aquela em que os dados encontram-se limpos e são confiáveis.
  - Utilizando o Apache Spark, através do serviço AWS Glue, integramos os dados existentes na camada Raw para a Trusted.
  - Utilizamos o formato Parquet pois otimiza o armazenamento e melhora o desempenho das consultas, é um formato colunar e altamente eficiente em compressão e leitura seletiva de dados.

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
  - Dados complementares de onde extraímos, principalmente, informações dos atores envolvidos nos filmes do Studio Ghibli.
    
    - artist_death_year
    - artist_birth_year
    - artist_gender
    - artist_name
    - vote_average_imdb
    - vote_count_imdb
    - artist_character
    - artist_profession

# Explicação do Processamento Camada Trusted


    
