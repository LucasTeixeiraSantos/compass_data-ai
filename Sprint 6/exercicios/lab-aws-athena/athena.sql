-- Crie o banco de dados

CREATE DATABASE meubanco

-- Crie a tabela

CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes_csv (
    nome STRING,
    sexo STRING,
    total INT,
    ano INT
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
    )
LOCATION 's3://bucket-lab-lts/dados/'


-- Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

WITH DecadeSummary AS (
    SELECT 
        nome,
        CAST(ano / 10 AS INT) * 10 AS decada,
        SUM(total) AS total_nome
    FROM 
        meubanco.nomes_csv
    WHERE 
        ano >= 1950
    GROUP BY 
        nome, 
        CAST(ano / 10 AS INT) * 10
),
RankedNames AS (
    SELECT 
        decada,
        nome,
        total_nome,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total_nome DESC) AS rank
    FROM 
        DecadeSummary
)
SELECT 
    decada,
    nome,
    total_nome
FROM 
    RankedNames
WHERE 
    rank <= 3
ORDER BY 
    decada, 
    rank;
