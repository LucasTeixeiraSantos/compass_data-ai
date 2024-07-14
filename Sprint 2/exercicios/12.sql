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
