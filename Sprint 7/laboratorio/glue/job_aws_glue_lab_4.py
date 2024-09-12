import sys
from awsglue.transforms import * # type: ignore
from awsglue.utils import getResolvedOptions # type: ignore
from pyspark.context import SparkContext # type: ignore
from awsglue.context import GlueContext # type: ignore
from awsglue.job import Job # type: ignore
from pyspark.sql.functions import col, upper, sum # type: ignore

## @params: [JOB_NAME, S3_INPUT_PATH, S3_OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos no S3
input_path = args['S3_INPUT_PATH']
output_path = args['S3_OUTPUT_PATH']

# 1 - Leitura do arquivo CSV no S3
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [input_path]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

df_spark = df.toDF()

# 2 - Imprimir o schema do DataFrame
df_spark.printSchema()

# 3 - Alterar a caixa dos valores da coluna 'nome' para MAIÚSCULO
df_upper = df_spark.withColumn("nome", upper(col("nome")))

# Verificar a transformação
df_upper.show()

# 4 - Contar o número de linhas no DataFrame
num_lines = df_upper.count()
print(f"4 - Number of lines in DataFrame: {num_lines}")

# 5 - Agrupar os dados pelas colunas ano e sexo e contar o número de nomes em cada grupo
df_grouped = df_upper.groupBy("ano", "sexo").count()
df_sorted = df_grouped.orderBy(col("ano").desc())
df_sorted.show()

# 6 - Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
df_fem = df_upper.filter(col("sexo") == "F")
df_fem_most_used = df_fem.orderBy(col("total").desc()).limit(1)
df_fem_most_used.show()

# 7 - Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
df_male = df_upper.filter(col("sexo") == "M")
df_male_most_used = df_male.orderBy(col("total").desc()).limit(1)
df_male_most_used.show()

# 8 - Agrupar pelos anos e somar o total de registros para cada ano
df_total_by_year = df_upper.groupBy("ano").agg(sum("total").alias("total_registros"))
df_sorted_year = df_total_by_year.orderBy("ano")
df_top_10 = df_sorted_year.limit(10)
df_top_10.show()

# 9. Escrever o DataFrame no S3 em formato JSON, particionado por sexo e ano
df_upper.write.mode("overwrite")\
    .partitionBy("sexo", "ano")\
    .json(output_path)

job.commit()
print("Job ended successfully!")
