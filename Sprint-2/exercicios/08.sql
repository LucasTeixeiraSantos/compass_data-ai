/* E08: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd. */ 

SELECT v.cdvdd, v.nmvdd
FROM tbvendedor v
JOIN tbvendas ven ON v.cdvdd = ven.cdvdd
WHERE ven.status = 'Concluído'
GROUP BY v.cdvdd, v.nmvdd
ORDER BY COUNT(ven.cdven) DESC
LIMIT 1;
