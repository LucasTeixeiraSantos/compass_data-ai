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