# OBS: O exercício foi executado no Google Colab

# Etapa 0

```py
!pip install pyspark
```

# Etapa 1

```py
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when, element_at, array, lit, expr
```
```py
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()
```
```py
df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")
```
```py
df_nomes.show(5)
```
![image](https://github.com/user-attachments/assets/00e226ea-3659-441a-8826-95878c5ad78d)

# Etapa 2

```py
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show()
```
![image](https://github.com/user-attachments/assets/6b4009ba-4cbb-4228-9bd6-b2e8fc558f1c)

# Etapa 3

```py
df_nomes = df_nomes.withColumn(
    "Escolaridade", 
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Medio")
    .otherwise("Superior")
)
df_nomes.show()
```
![image](https://github.com/user-attachments/assets/24273480-13a6-4207-b9d4-7a974a580142)

# Etapa 4

```py
paises_america_do_sul = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", 
    "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"
]
```
```py
df_nomes = df_nomes.withColumn(
    "Pais", 
    element_at(
        array([lit(pais) for pais in paises_america_do_sul]), 
        (rand() * 13).cast("int") + 1
    )
)
df_nomes.show()
```
![image](https://github.com/user-attachments/assets/138d6eee-d7c1-4767-ac56-7428c0203daf)

# Etapa 5

```py
df_nomes = df_nomes.withColumn(
    "AnoNascimento", 
    (rand() * (2010 - 1945) + 1945).cast("int")
)
df_nomes.show()
```
![image](https://github.com/user-attachments/assets/52a87829-2366-4803-b989-c990e93fcc26)

# Etapa 6

```py
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000).select("Nomes")
```
```py
df_select.show(10)
```
![image](https://github.com/user-attachments/assets/d861645c-3a4f-41d5-b2bf-265067b33848)

# Etapa 7

```py
df_nomes.createOrReplaceTempView("nomes_view")
```
```py
df_select_sql = spark.sql("""
    SELECT Nomes
    FROM nomes_view
    WHERE AnoNascimento >= 2000
""")
```
```py
df_select_sql.show(10)
```
![image](https://github.com/user-attachments/assets/ea70cc21-5bd2-4ab6-8da3-60e50b2ce0e4)

# Etapa 8

```py
millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()
print(millennials_count)
```
![image](https://github.com/user-attachments/assets/2c52714f-ab70-4c3f-9378-ba9cae778608)

# Etapa 9

```py
millennials_count_sql = spark.sql("""
    SELECT COUNT(*) AS millennials_count
    FROM nomes_view
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""").collect()[0]['millennials_count']
print(millennials_count_sql)
```
![image](https://github.com/user-attachments/assets/7dc139b4-352c-49c1-9cd6-bf48f226ccd5)

# Etapa 10

```py
df_count_per_generation = spark.sql("""
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
            ELSE 'Outra Geracao'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM nomes_view
    WHERE AnoNascimento BETWEEN 1944 AND 2015
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")
```
```py
df_count_per_generation.show(truncate=False)
```
![image](https://github.com/user-attachments/assets/28434c26-8dea-4ec2-becd-3aef36a10acd)
