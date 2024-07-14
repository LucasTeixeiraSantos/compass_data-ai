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
