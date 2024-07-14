/* E09: dApresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser cdpro e nmpro. */

SELECT ven.cdpro, ven.nmpro
FROM tbvendas ven
WHERE ven.status = 'Concluído'
    AND ven.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY cdpro, nmpro
LIMIT 1;
