# Criar a imagem Docker
```bash
dockerbuild -t spark-notebook .
```
# Executar o container
```bash
docker run -it -p 8888:8888 spark-notebook
```
# Em outro terminal, lista os containers e copie o ID
```bash
docker ps
```

# Execute o bash dentro do container
```bash
docker exec -it <container-id> bash
```
# Faça o download do README.md
```bash
wget -O <README.md> <raw-readme-link>
```
#Inicialize o PySpark e execute os comandos 
```bash
# Inicializar o PysPark
pyspark
```

```bash
# Ler o arquivo README.md
rdd = sc.textFile("/home/jovyan/exercise/README.md")
```

```bash
# Dividir o texto em palavras
words = rdd.flatMap(lambda line: line.split(" "))
```

```bash
# Criar pares
word_pairs = words.map(lambda word: (word, 1))
```

```bash
# Contar as ocorrências de cada palavra
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)
```

```bash
# Ordenar as palavras por contagem em ordem decrescente
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)
```
# Coletar e exibir os resultados
sorted_word_counts.collect()


![image](https://github.com/user-attachments/assets/41b804ca-8b98-41bc-a741-cbf3a8d40af2)
