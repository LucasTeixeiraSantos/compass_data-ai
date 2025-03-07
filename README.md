# Projeto de Estágio em Dados - Compass Data & AI

## **Visão Geral**  
Repositório contendo o projeto desenvolvido durante o programa de Estágio em Dados da Compass Data & AI. O objetivo principal é construir um pipeline completo de dados na AWS para análise de filmes e séries, abrangendo desde ingestão e processamento até visualização de dados.

---
## **Dashboard Final**
 
 ![Análise Geral](Sprint%2010/evidencias/41-quicksight-analysis-sheet-analysis.png)
 ![Detalhes do Filme](Sprint%2010/evidencias/42-quicksight-analysis-sheet-movie-details.png)

---

## Estrutura do Projeto (10 Sprints)

### Sprint 1: Linux & Git
- Fundamentos de linha de comando e controle de versão

### Sprint 2: SQL 
- Manipulação de dados com consultas SQL

### Sprint 3: Python
- Automação e análise de dados

### Sprint 4: Docker
- Containerização de aplicações

### Sprint 5: AWS Essentials
- Configuração S3 e integração com boto3

### Sprint 6: Upload Inicial
- Carregamento de dados brutos no S3

### Sprint 7: Ingestão via API
- Coleta de dados do TMDB e armazenamento

### Sprint 8: Processamento (Trusted)
- Transformação de dados com AWS Glue/PySpark
- Conversão para formato Parquet

### Sprint 9: Modelagem (Refined)
- Implementação de Star Schema
- Otimização para consultas analíticas

### Sprint 10: Visualização
- Criação de dashboards interativos no QuickSight
- Geração de insights estratégicos
---

## Tecnologias & Ferramentas

### Fundamentos
- **Linux**: Manipulação de arquivos e diretórios
- **Git & GitHub**: Versionamento e colaboração
- **SQL**: Consultas e manipulação de dados
- **Python**: Automação e processamento de dados
- **Docker**: Containerização de aplicações

### ☁️ AWS Stack
| Serviço           | Função                                                                |
|-------------------|-----------------------------------------------------------------------|
| **S3**                | Armazenamento de dados (raw/trusted/refined)                          |
| **Lambda**            | Ingestão de dados via API (serverless)                                |
| **Glue**              | Processamento ETL com PySpark                                         |
| **Athena**            | Consulta direta de dados no S3 via SQL                                |
| **QuickSight**        | Visualização de dados e dashboards                                    |
| **Boto3**             | Integração Python com serviços AWS                                    |


### Outras Ferramentas
- **PySpark**: Processamento em larga escala
- **Parquet**: Formato otimizado para Big Data
- **API TMDB**: Coleta de dados de filmes/séries
- **Star Schema**: Modelagem dimensional para análise


