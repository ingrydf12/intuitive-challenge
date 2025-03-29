-- 3.3
-- Tabela para receber as operadoras do arquivo .csv (Relatorio_cadop)
CREATE TABLE IF NOT EXISTS operadoras_ativas (
    registro_ans INTEGER PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(200) NOT NULL,
    nome_fantasia VARCHAR(200),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep INTEGER,
    ddd INTEGER,
    telefone BIGINT,
    fax BIGINT,
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(200),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao SMALLINT,
    data_registro_ans DATE
);

-- Dados de demonstracoes_contabeis
CREATE TABLE IF NOT EXISTS despesas_trimestrais (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil BIGINT,
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);