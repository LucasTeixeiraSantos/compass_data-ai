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
