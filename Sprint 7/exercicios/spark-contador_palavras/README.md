dockerbuild -t spark-notebook .
docker run -it -p 8888:8888 spark-notebook

abra outro cmd
docker ps
docker exec -it <container-id> bash
wget -O <README.md> <raw-readme-link>
pyspark
rdd = sc.textFile("/home/jovyan/exercise/README.md")
words = rdd.flatMap(lambda line: line.split(" "))
word_pairs = words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)
sorted_word_counts.collect()
