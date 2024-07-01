# Evidências / Etapas para execução

![image](https://github.com/LucasTeixeiraSantos/compass_data-ai/assets/134326998/2b7541fa-8db2-4067-99e8-74d59f1cad43)

## Etapa 1: Preparar o ambiente

1 - Certifique-se de que todos os comandos necessários estão instalados:
        cp, mv, awk, sort, uniq, wc, head, zip para o primeiro script.
        cat para o segundo script.
```bash
sudo apt update
sudo apt install -y coreutils gawk zip
```
Se preferir, você pode utilizar o script "instalar_dependencias.sh".
```bash
chmod +x instalar_dependencias.sh
./instalar_dependencias.sh
```
2 - Execute o script de processamento de vendas:

Esse script deve ser executado sempre que você tiver um novo arquivo CSV de vendas para processar. Ele fará backup dos dados, gerará relatórios e comprimirá os arquivos. Caso você queira executar testes com o script utilizando datas e arquivos CSV diversos, utilize o comando "date --set", por exemplo: sudo date --set="2024-06-27 20:27:09"

```bash
chmod +x processamento_de_vendas.sh
./processamento_de_vendas.sh
```

![image](https://github.com/LucasTeixeiraSantos/compass_data-ai/assets/134326998/2c2de034-e940-448a-9891-b12948ab29a4)

3 - Execute o script de consolidação de relatórios:

Esse script deve ser executado após ter vários relatórios gerados pelo script de processamento de vendas. Ele consolidará todos os relatórios individuais em um relatório final.

```bash
chmod +x consolidador_de_processamento_de_vendas.sh
./consolidador_de_processamento_de_vendas.sh
```

![image](https://github.com/LucasTeixeiraSantos/compass_data-ai/assets/134326998/93521074-aa82-4a4e-a7cf-379959e9fde7)

4 - Entre no diretório vendas/backup

```bash
cd vendas/backup
```
![image](https://github.com/LucasTeixeiraSantos/compass_data-ai/assets/134326998/706ba969-f650-4f49-ba7c-86564a9ec307)

5 - Visualize o conteúdo do relatorio_final.txt utilizando o comando cat

```bash
cat relatorio_final.txt
```
![image](https://github.com/LucasTeixeiraSantos/compass_data-ai/assets/134326998/7c0739c3-5d35-47d8-80a3-e6d2398b9015)
