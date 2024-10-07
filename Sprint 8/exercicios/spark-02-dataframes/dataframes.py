#!pip install pyspark

from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when, element_at, array, lit, expr

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("/content/nomes_aleatorios.txt")

df_nomes.show(5)

df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show()

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Medio")
    .otherwise("Superior")
)

df_nomes.show()

paises_america_do_sul = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador",
    "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    element_at(
        array([lit(pais) for pais in paises_america_do_sul]),
        (rand() * 13).cast("int") + 1
    )
)

df_nomes.show()

df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (rand() * (2010 - 1945) + 1945).cast("int")
)

df_nomes.show()

df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000).select("Nomes")

df_select.show(10)

df_nomes.createOrReplaceTempView("nomes_view")

df_select_sql = spark.sql("""
    SELECT Nomes
    FROM nomes_view
    WHERE AnoNascimento >= 2000
""")

df_select_sql.show(10)

millennials_count = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()

print(millennials_count)

millennials_count_sql = spark.sql("""
    SELECT COUNT(*) AS millennials_count
    FROM nomes_view
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""").collect()[0]['millennials_count']

print(millennials_count)

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

df_count_per_generation.show(truncate=False)





