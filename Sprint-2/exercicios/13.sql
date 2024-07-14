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
