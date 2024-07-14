/* E01: Apresente a query para listar todos os livros publicados após 2014. 
Ordenar pela coluna cod, em ordem crescente, as linhas.  
Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma */

SELECT *
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod ASC;

/* E02: Apresente a query para listar os 10 livros mais caros. 
Ordenar as linhas pela coluna valor, em ordem decrescente. 
Atenção às colunas esperadas no resultado final:  titulo, valor. */

SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;

/* E03:
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente. */

 SELECT
    count(livro.cod) AS quantidade,
    editora.nome,
    endereco.estado,
    endereco.cidade
FROM
    livro
JOIN
    editora ON livro.editora = editora.codeditora
JOIN
 endereco ON editora.endereco = endereco.codendereco
GROUP BY
    editora.nome, endereco.estado, endereco.cidade
ORDER BY
    quantidade DESC
codeditora	nome	endereco
LIMIT 5;

/* E04: Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
*/

SELECT 
    a.codautor, 
    a.nome, 
    a.nascimento, 
    COUNT(l.cod) AS quantidade
FROM 
    autor a
LEFT JOIN 
    livro l ON a.codautor = l.autor
GROUP BY 
    a.codautor, a.nome, a.nascimento
ORDER BY 
    nome ASC;


/*E05: Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente. 
Não podem haver nomes repetidos em seu retorno.
*/

SELECT DISTINCT A.nome
FROM AUTOR A
JOIN LIVRO L ON A.codAutor = L.autor
JOIN EDITORA E ON L.editora = E.codEditora
JOIN ENDERECO EN ON E.endereco = EN.codEndereco
WHERE EN.estado NOT IN ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
ORDER BY A.nome ASC;


/* E06: Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. */

SELECT
    autor.codautor,
    autor.nome,
    COUNT(livro.cod) AS quantidade_publicacoes
FROM
    autor
JOIN
    livro ON autor.codautor = livro.autor
GROUP BY
    autor.codautor, autor.nome
ORDER BY
    quantidade_publicacoes DESC
LIMIT 1;


/* E07: Apresente a query para listar o nome dos autores com nenhuma publicação. 
Apresentá-los em ordem crescente. */

SELECT
    autor.nome
FROM
    autor
WHERE
    autor.codautor NOT IN (SELECT DISTINCT autor FROM livro)
ORDER BY
    autor.nome ASC;


/* E08: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd. */ 

SELECT v.cdvdd, v.nmvdd
FROM tbvendedor v
JOIN tbvendas ven ON v.cdvdd = ven.cdvdd
WHERE ven.status = 'Concluído'
GROUP BY v.cdvdd, v.nmvdd
ORDER BY COUNT(ven.cdven) DESC
LIMIT 1;

/* E09: dApresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser cdpro e nmpro. */

SELECT ven.cdpro, ven.nmpro
FROM tbvendas ven
WHERE ven.status = 'Concluído'
    AND ven.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY cdpro, nmpro
LIMIT 1;

/* E10: A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. 
O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal. */

SELECT 
    v.nmvdd AS vendedor, 
    ROUND(SUM(ven.qtd * ven.vrunt), 2) AS valor_total_vendas, 
    ROUND(SUM(ven.qtd * ven.vrunt) * (v.perccomissao / 100.0), 2) AS comissao
FROM 
    tbvendas ven
JOIN 
    tbvendedor v ON ven.cdvdd = v.cdvdd
WHERE 
    ven.status = 'Concluído'
GROUP BY 
    v.nmvdd
ORDER BY 
    comissao DESC;


/* E11: Apresente a query para listar o código e nome cliente com maior gasto na loja. 
As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente. */ 

SELECT 
    ven.cdcli, 
    ven.nmcli, 
    ROUND(SUM(ven.qtd * ven.vrunt), 2) AS gasto
FROM 
    tbvendas ven
WHERE 
    ven.status = 'Concluído'
GROUP BY 
    ven.cdcli, ven.nmcli
ORDER BY 
    gasto DESC
LIMIT 1;


/* E12:Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído. */

WITH VendasPorVendedor AS (
    SELECT 
        ven.cdvdd, 
        SUM(ven.qtd * ven.vrunt) AS valor_total_vendas
    FROM 
        tbvendas ven
    WHERE 
        ven.status = 'Concluído'
    GROUP BY 
        ven.cdvdd
    HAVING 
        valor_total_vendas > 0
),
VendedorMenorVenda AS (
    SELECT 
        cdvdd, 
        valor_total_vendas
    FROM 
        VendasPorVendedor
    ORDER BY 
        valor_total_vendas ASC
    LIMIT 1
)
SELECT 
    d.cddep, 
    d.nmdep, 
    d.dtnasc, 
    vm.valor_total_vendas
FROM 
    tbdependente d
JOIN 
    VendedorMenorVenda vm ON d.cdvdd = vm.cdvdd;


/* E13:Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/

SELECT 
    ven.cdpro, 
    ven.nmcanalvendas, 
    ven.nmpro, 
    SUM(ven.qtd) AS quantidade_vendas
FROM 
    tbvendas ven
WHERE 
    ven.status = 'Concluído' 
    AND (ven.nmcanalvendas = 'Ecommerce' OR ven.nmcanalvendas = 'Matriz')
GROUP BY 
    ven.cdpro, ven.nmcanalvendas, ven.nmpro
ORDER BY 
    quantidade_vendas ASC
LIMIT 10;


/* E14: Apresente a query para listar o gasto médio por estado da federação. 
As colunas presentes no resultado devem ser estado e gastomedio. 
Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
Observação: Apenas vendas com status concluído. */

SELECT 
    ven.estado, 
    ROUND(AVG(ven.qtd * ven.vrunt), 2) AS gastomedio
FROM 
    tbvendas ven
WHERE 
    ven.status = 'Concluído'
GROUP BY 
    ven.estado
ORDER BY 
    gastomedio DESC;


/* E15: Apresente a query para listar os códigos das vendas identificadas como deletadas. 
Apresente o resultado em ordem crescente. */

SELECT 
    cdven
FROM 
    tbvendas
WHERE 
    deletado = 1
ORDER BY 
    cdven ASC;


/* E16: Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
Considere arredondar o valor da coluna quantidade_media na quarta casa decimal.
Ordene os resultados pelo estado (1º) e nome do produto (2º).
Obs: Somente vendas concluídas.*/

SELECT 
    ven.estado, 
    ven.nmpro, 
    ROUND(AVG(ven.qtd), 4) AS quantidade_media
FROM 
    tbvendas ven
WHERE 
    ven.status = 'Concluído'
GROUP BY 
    ven.estado, ven.nmpro
ORDER BY 
    ven.estado, ven.nmpro;
