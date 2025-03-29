-- 3.4
-- Demonstrações contábeis

\copy despesas_trimestrais FROM 'data/1T2023.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/2t2023.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/3T2023.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/4T2023.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/1T2024.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/2T2024.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/3T2024.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';
\copy despesas_trimestrais FROM 'data/4T2024.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';

-- Relatório
\copy relatorio_cadop FROM 'data/Relatorio_cadop.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF8';