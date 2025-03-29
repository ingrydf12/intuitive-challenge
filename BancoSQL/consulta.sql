-- 3.5
-- Maiores despesas no trimestre
SELECT 
    reg_ans,
    descricao,
    SUM(REPLACE(vl_saldo_inicial, ',', '.')::NUMERIC) AS total_despesa
FROM despesas_trimestrais
WHERE TRIM(descricao) ILIKE '%SINISTROS CONHECIDOS OU AVISADOS%'
  AND TRIM(descricao) ILIKE '%MEDICO HOSPITALAR%'
  AND data >= '2024-10-01'
GROUP BY reg_ans, descricao
ORDER BY total_despesa DESC
LIMIT 10;

-- Maiores despesas no último ano
SELECT 
    reg_ans,
    descricao,
    SUM(REPLACE(vl_saldo_inicial, ',', '.')::NUMERIC) AS total_despesa
FROM despesas_trimestrais
WHERE TRIM(descricao) ILIKE '%SINISTROS CONHECIDOS OU AVISADOS%'
  AND TRIM(descricao) ILIKE '%MEDICO HOSPITALAR%'
  AND data >= '2024-01-01'
GROUP BY reg_ans, descricao
ORDER BY total_despesa DESC
LIMIT 10;