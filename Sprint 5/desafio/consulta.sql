SELECT
    min(cast("Quantidade de Declarantes" as int)) AS min_declarantes,
    max(cast("Quantidade de Declarantes" as int)) AS max_declarantes,
    CASE 
        WHEN min(cast("Quantidade de Declarantes" as int)) < 10000 THEN 'Low'
        ELSE 'High'
    END AS "Income_Category",
    UTCNOW(),
    CHAR_LENGTH('Quantidade de Declarantes')
FROM S3Object
WHERE
    "Quantidade de Declarantes" > '0'
    OR "Quantidade de Declarantes" < '100000'
    AND "Quantidade de Declarantes" IS NOT NULL