# Quinta Etapa do Desafio Filmes e Séries

## Consumo dos Dados - Visualização e Insights

Na **Quinta Etapa** e última etapa do Desafio Filmes e Séries, nosso objetivo é **extrair insights dos dados refinados** e **apresentá-los de forma visual e interativa** usando a ferramenta de visualização **AWS QuickSight**. Até este ponto, todas as atividades envolveram ingestão, armazenamento e processamento de dados no data lake. Agora, avançamos para a camada final: **consumir e analisar os dados para gerar insights** valiosos.

## Objetivos

1. **Criação de uma Análise no AWS QuickSight:**
   - Utilizar as tabelas da **Camada Refined** como **única fonte de dados** para o QuickSight.
   - Conectar ao **AWS Athena** como fonte de dados para o QuickSight, facilitando o acesso às tabelas na Camada Refined.

2. **Exploração de Visualizações e criação do Dashboard:**
   - Explorar os diferentes tipos de visualizações oferecidos pelo QuickSight, como gráficos de linha, gráficos de barras, tabelas dinâmicas, heatmaps, entre outros.
   - Estruturar uma **narrativa** clara e objetiva a partir dos dados, com foco em fornecer insights relevantes e facilmente compreensíveis.
   - Publicar o Dashboard.

## Execução

###  1. **Criação de um Dashboard no AWS QuickSight:**
   - Acesse o **Console** da **AWS**.
   - Na barra de pesquisa, digite **"QuickSight"** e abra-o. <br>
   ![image](https://github.com/user-attachments/assets/6c8fcb6b-fcbc-4cf3-ae72-132cc46c383a)
   - Caso não possua, crie uma conta no QuickSight.
   - Na página inicial do **QuickSight**, clique em **"Datasets"** na aba lateral esquerda. <br>
   ![image](https://github.com/user-attachments/assets/5b308681-b10b-4f38-b693-0a8afe616443)
   - No canto superior direito, clique em **"New dataset"**. <br>
   ![image](https://github.com/user-attachments/assets/83346ded-057a-42e9-9b2f-ff3d78244f9c)
   - Em **"FROM NEW DATA SOURCES"**, selecione o **"Athena"**. <br>
   ![image](https://github.com/user-attachments/assets/c5686758-a9ef-47e9-8542-35023e7186e4)
   - Em **"Data source name"**, escolha um nome para o Data Source.
   - Em **"Athena workgroup"**, escolha o seu Workgroup. <br>
   - Clique em **"Create data source** <br>
   ![image](https://github.com/user-attachments/assets/1add51dc-05c7-42b9-862b-e60cfd70fe68)
   - Clique em **"Use custom SQL"**.
   - Insira a seguinte query:
   ```SQL
   SELECT 
    movie.id AS movie_id,
    movie.id_imdb,
    movie.title,
    movie.title_original,
    movie.tagline,
    movie.overview,
    movie.runtime AS movie_runtime,
    movie.poster,
    movie.backdrop_1,
    movie.backdrop_2,
    movie.backdrop_3,
    facts.rating_imdb,
    facts.rating_tmdb,
    facts.release,
    facts.budget,
    facts.gross_worldwide,
    facts.revenue,
    facts.runtime AS fact_runtime,
    review.content AS review_content,
    review.sentiment_label AS review_sentiment
FROM 
    datalake_pb_lucas.d_movie movie
JOIN 
    datalake_pb_lucas.f_movies facts ON movie.id = facts.id
LEFT JOIN 
    datalake_pb_lucas.review review ON movie.id_imdb = review.id_imdb;
   ```
   - Clique em **"Confirm Query"**. <br>
   ![image](https://github.com/user-attachments/assets/fb5f7db8-396b-4c4d-96cd-7a01d174b837)
   - Clique em **"Edit/Preview Data"**. <br>
   ![image](https://github.com/user-attachments/assets/6812bdef-7cad-4ba9-8f07-129e3ffae9dc)
   - No canto esquerdo, em **"Fields"**, clique nos **"3 pontinhos"** nos campos que deseja remover ou alterar o nome. 
   - Antes: <br>
   ![image](https://github.com/user-attachments/assets/150038d8-5c29-4780-8200-700884e3262e)
   - Depois: <br> 
   ![image](https://github.com/user-attachments/assets/f5096915-8468-4e0c-a77e-e366db246a9b)
   - No canto superior direito, clique em **"SAVE & PUBLISH"**. <br> 
   ![image](https://github.com/user-attachments/assets/dd4c9709-f669-44b0-83fa-18bc32226c43)
   - Volte para a página inicial do **QuickSight**, acesse a página **Analyses** no canto esquerdo e clique na sua análise.
   - Criamos a análise!

   ### 2. **Exploração de Visualizações e criação do Dashboard:**
   - Primeiramente, vamos criar um Layout para utilizar como base visual na Análise, utilizei o Figma. 
   - Página 1, **"Analysis"**: <br>
   ![image](https://github.com/user-attachments/assets/75a79d70-5ce1-4bef-9629-d5e63658b77f)
   - Página 2, **"Movie Details"**: <br>
   ![image](https://github.com/user-attachments/assets/60c565e8-a5e9-4ea8-b1aa-57832f53f30e)
   
   - Visual: **Background Image - Analysis (Custom Visual Content)**. <br>
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Custom visual content**. <br>
     ![image](https://github.com/user-attachments/assets/9ac660e6-6bda-41e5-9035-88f3062eaeb4)
     - Clique em **Customize visual**. <br>
     - ![image](https://github.com/user-attachments/assets/6124eb68-3ee6-4c9b-a245-ab7a103d5c46)
     - Em Display Settings, remova Background, Border e Selection. <br>
     ![image](https://github.com/user-attachments/assets/b753ee0b-c1fb-45ac-89d8-841648475544)
     - Em **Custom Content**, cole a URL da imagem de background da página Analysis. 
     - Clique em **Show as image**.
     - Selecione **Scale to visual**.
     - Altere a altura e largura para a máxima permitida. <br>
     ![image](https://github.com/user-attachments/assets/b9b32759-1a2f-468e-8ba3-08fde97857ee)
      
     - Visual: **Number of Studio Ghibli Movies (KPI)**. <br>
       - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
       ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
       - Selecione o **Key Performance Indicator**. <br>
       ![image](https://github.com/user-attachments/assets/efe66c94-6caa-4e28-bffd-be33364cc4ba)
       - No canto esquerdo, altere o campo "Title" para medida e adicione-o ao Visual. <br> 
       - No visual, clique nos 3 pontos ao lado do Title, e selecione **Agregate: Count Distinct**. <br>
       ![image](https://github.com/user-attachments/assets/24d6961a-2007-462d-b9b9-d60ac141bf1f)
       - No canto direito, em **Properties**, clique em **Display Settings** e esconda o **Title**, **Subtitle**, **Background**, **Border** e **Selection**.
       - Arraste o card para local correto e dimensione-o para ajustar o tamanho do texto (Você pode utilizar as setas do teclado para uma maior precisão. <br>
       ![image](https://github.com/user-attachments/assets/97a2edd5-406d-4c5c-a283-627b1c27f3ca)

          
   - Visual: **Total Profit (KPI)**.
     - Repita os passos do **Visual: Number of Studio Ghibli Movies (KPI)**, alterando o seguinte:
     - Utilize o campo **Profit**, e a agregação **Sum**. <br> 
     ![image](https://github.com/user-attachments/assets/6889e9cd-9c29-4bab-a606-607c6a6e3dc5)

   
   - Visual: **Sentiment Analysis from IMDB Reviews (Donut Chart)**.
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Donut chart**. <br>
     ![image](https://github.com/user-attachments/assets/258fd538-6ae8-41f8-88ce-5dca79c6bbab)
     - Utilize o campo dimensão **Sentiment**.
     - Em **Format visual**, expanda **Data labels**.
       - Clique em mostrar **Metric**.
       - Em **Metic label style**, selecione **Percent only**.
       - Em **Text**, selecione **Extra large**.
     - Em **Format visual**, desmarque **Legend**.
     - Assim como nos passos anteriores, remova títulos, subtítulos, background, borda e seleção.
     - Redimensione e coloque-o no local correto. <br>
     ![image](https://github.com/user-attachments/assets/9e84c5fe-2cc6-4a6e-bee1-2aef8c7f53bd)

     
   - Visual: **Movie Profit by Year (Line Chart)**.
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Line Chart**. <br>
     ![image](https://github.com/user-attachments/assets/e296938a-7906-470c-9089-d447114e933a)
     - Em **X AXIS**, selecione o campo dimensão **Release**.
     - Em **VALUE**, selecione o campo medida **Profit** com agregação **Sum**.
     - Em **COLOR**, selecione o campo dimensão **Title**.
     - Assim como nos passos anteriores, remova títulos, subtítulos, background, borda e seleção. <br>
     - Altere o título de **Y-axis** para **Profit**.
     - Altere o título de **Y-axis** para **Year**.
     - Ordene por **Release** em ordem crescente.
     - Redimensione e coloque-o no local correto.
     ![image](https://github.com/user-attachments/assets/314792f1-6325-4ebd-aa19-61eb102f6bf6)
     

   - Visual: **Movies Table (Table)**.
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Table**. <br>
     ![image](https://github.com/user-attachments/assets/74ab0a39-f165-4376-9885-82911cfb66cb)
     - Em **GROUP BY**, adicione a dimensão **Title**.
     - Em **GROUP BY**, adicione a dimensão **Genres**.
     - Em **VALUE**, adicione a medida **Release Year** com agregação **Min**.
     - Em **VALUE**, adicione a medida *Rating** com agregação **Min**.
     - Em **VALUE**, adicione a medida **Runtime (Minutes)** com agregação **Min**.
     - Em **VALUE**, adicione a medida **Profit** com agregação **Sum**.
     - Assim como nos passos anteriores, remova títulos, subtítulos, background, borda e seleção. Tanto da tabela quanto das células. <br>
     ![image](https://github.com/user-attachments/assets/e8f9c18c-c855-491e-b4ba-b05e098dce91)

### Crie uma nova página chamada **Movie Details**
   - No topo, ao lado da página **Analysis**, clique no símbolo de **" + "**.
   - Crie uma **Interactive sheet** com **layout** **Free-form**.
   - Clique no nome da página criada para alterá-la, digite **"Movie Details"**. <br>
   ![image](https://github.com/user-attachments/assets/347fa8ec-379f-4414-a81e-cc0fcf935419)
   - No canto superior em **Data**, clique em **Add Parameter**.
   - ![image](https://github.com/user-attachments/assets/b7f96d1d-969e-4720-b5df-0e6fb904761c)
   - Em **Name**, digite **pTitle**.
   - Clique em **Create**.
   - No canto superior, clique no ícone dos parâmetros a seguir. <br>
   ![image](https://github.com/user-attachments/assets/a1e9e3a2-f7ab-43fc-b6e9-9bc156463a6f)
   - No parâmetro pTitle, clique nos 3 pontinhos e selecione **Add control**.
   - Em **Name**, digite **Title Control**.
   - Em **Style**, selecione **List**.
   - Em **Values**, selecione **Link to a dataset field**.
   - Em **Dataset**, selecione **Studio Ghibli Movies**.
   - Em **Field**, selecione **Title**.
   - Marque a opção **Hide Select all option...**.
   - Clique em **Add**.
   ![image](https://github.com/user-attachments/assets/f0991daa-12d7-4626-9876-4ee73935ad14)


   - No topo, em **Controls**, clique nos 3 pontinhos do **Title Control**.
   - Selecione **Move inside this sheet**.
   - Arraste-o para o local desejado. <br> 
   ![image](https://github.com/user-attachments/assets/da56bab7-545f-48f6-aaa1-42e4ea65bc19) <br>


   - Visual: **Movie Poster Image (Table)**.
     - Crie um campo calculado chamado **ImageURL**.
     - Utilize o seguinte código:
     ```QuickSight
     ifelse(
        title = ${pTitle}, 
        concat('https://image.tmdb.org/t/p/w500/', poster, '.jpg'), 
        NULL
     )
     ```
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Table**. <br>
     ![image](https://github.com/user-attachments/assets/74ab0a39-f165-4376-9885-82911cfb66cb)
     - Em **GROUP BY**, coloque a dimensão **ImageURL**.
     - Em **Properties**, expanda o campo **Field styling**.
       - Marque a opção **Show URLs as images**.
       - Marque a opção **Fit to cell height**. <br>
     ![image](https://github.com/user-attachments/assets/2b7303cd-7a23-4aa4-91ca-e04b2a235db8)
     - Assim como nos passos anteriores, remova títulos, subtítulos, background, borda e seleção. Tanto da tabela quanto das células. 
     - Redimensione a tabela e a célula para o tamanho desejado e coloque-a no espaço correto. <br>
     ![image](https://github.com/user-attachments/assets/e5e7cad6-1d51-46fe-a755-2841b870ffd6) <br>



     - Visual: **Movie Background Image (Table)**.
     - Seguindo os passos do parâmetro **pTitle**, crie um novo parâmetro chamado **pSelectBackdrop**, mas altere o seguinte:
     - Em **Static default value**, digite 1.
     - Crie um novo controler seguinte os passos do **Title Control**, mas altere o seguinte:
     - Em **Control options**, selecione **Specific values**.
     - Em ** Define specific values, digite o seguinte:
     ```text
     1
     2
     3
     ```
     - Marque a opção **Hide searcj bar when control is on sheet**.
     - Marque a opção **Hide Select all option...**.
     - Crie um campo calculado chamado **Backdrop URL**.
     - Utilize o seguinte código:
     ```QuickSight
     ifelse(
        ${pSelectBackdrop}="1", 
        concat('https://image.tmdb.org/t/p/original/', {backdrop_1}, '.jpg'),
        ${pSelectBackdrop}="2",
        concat('https://image.tmdb.org/t/p/original/', {backdrop_2}, '.jpg'),
        ${pSelectBackdrop}="3", 
        concat('https://image.tmdb.org/t/p/original/', {backdrop_3}, '.jpg'),
        NULL
     )
     ```
     - Em **Visuals**, clique no botão ao lado de **"ADD"**. <br>
     ![image](https://github.com/user-attachments/assets/57d6c63c-327b-4fb6-959e-94b692c53e9a)
     - Selecione o **Table**. <br>
     ![image](https://github.com/user-attachments/assets/74ab0a39-f165-4376-9885-82911cfb66cb)
     - Em **GROUP BY**, coloque a dimensão **Backdrop URL**.
     - Em **Properties**, expanda o campo **Field styling**.
       - Marque a opção **SHow URLs as images**.
       - Marque a opção **Fit to cell height**. 
     ![image](https://github.com/user-attachments/assets/2b7303cd-7a23-4aa4-91ca-e04b2a235db8)
     - Assim como nos passos anteriores, remova títulos, subtítulos, background, borda e seleção. Tanto da tabela quanto das células. 
     - Redimensione a tabela e a célula para o tamanho desejado e coloque-a no espaço correto. <br>
     ![image](https://github.com/user-attachments/assets/bfbcb83a-ccb3-4e93-bc2e-6b5b151a168c) <br>

     - Siga os passos anteriores para adicionar o restante dos visuais. <br>

     - Volte a página **Analysis** e clique na tabela.
     - No canto direito, selecione **Interactions**.
     - Expanda o campo **Actions**.
     - Clique em **ADD ACTION**.
     - Em **Activation, selecione a opção **Select**.
     - Em **Action Type**, selecione **Navigation action**.
     - Em **Target sheet**, selecione **Movie Details**.
     - Em **Parameters**, clique em **" + "**.
     - Em **Select parameter**, selecione **pTitle**.
     - Em **Select value**, selectione **Field: Title**. <br>
    
     - Clique no canto superior direito em **Publish**.
     - Digite um nome para o Dashboard.
     - Clique em **Publish dashboard**.
     - Volte para a página inicial do Quicksight.
     - Clique em **Dashboards** e selecione o seu Dashboard. <br>
       
     ## Resultado Final

     ### Página **Analysis** <br>

      ![image](https://github.com/user-attachments/assets/262e5fc3-4ff2-4fd6-aec1-7226104974b9) <br>

     ### Página **Movie Details** <br>

      ![image](https://github.com/user-attachments/assets/b5e63e6e-22be-4e60-882a-a6063281de90)

     

    
   

     
     
   
