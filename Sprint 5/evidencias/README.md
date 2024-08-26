1. Procure um arquivo CSV ou JSON no portal de dados públicos do Governo Brasileiro:

[Grandes Números do Imposto de Renda da Pessoa Física](https://dados.gov.br/dados/conjuntos-dados/grandes-nmeros-do-imposto-de-renda-da-pessoa-fsica)
![image](https://github.com/user-attachments/assets/fb48ab31-2c83-4b50-a210-ec41209c5efe)

2. Analise o conjunto de dados escolhido em um editor de sua preferência:

![image](https://github.com/user-attachments/assets/3cb52018-d4c2-49fc-b6f9-fe8f59f2ba70)

3. Carregue o arquivo para um bucket novo:

![image](https://github.com/user-attachments/assets/ad4162ff-8717-4e6c-8fbe-654543fc7f12)

4. Utilize o S3 pelo console ou pelo Boto3:
   - Foi escolhido o Boto3.

6. Através da função S3 Select, crie pelo menos uma consulta nos seus arquivos que utilize:
   - Query completa: <br>
   ![image](https://github.com/user-attachments/assets/e42887b3-dbdd-42d0-bcc0-5232a7d0fa38)

   - Uma cláusula que filtra dados usando ao menos dois operadores lógicos: <br>
   ![image](https://github.com/user-attachments/assets/48f2cb45-b4b2-44eb-8f5d-c24427a11d5d)

   - Duas funções de Agregação: <br>
   ![image](https://github.com/user-attachments/assets/436a77d1-624e-4237-94c8-96c0d1c9dc77)

   - Uma função Condicional: <br>
   ![image](https://github.com/user-attachments/assets/3f945a21-d06b-429b-9824-71665b1e7e17)

   - Uma função de Conversão: <br>
   ![image](https://github.com/user-attachments/assets/7029d8d9-9dad-4a18-b674-71565be6647e)
     
   - Uma função de Data: <br>
   ![image](https://github.com/user-attachments/assets/c7968c3f-573c-4a40-9b2a-fca064feb10c)

   - Uma função de String: <br>
   ![image](https://github.com/user-attachments/assets/2c0f9a00-13ae-45aa-a922-26388e3edd42)
