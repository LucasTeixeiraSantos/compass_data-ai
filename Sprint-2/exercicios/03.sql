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