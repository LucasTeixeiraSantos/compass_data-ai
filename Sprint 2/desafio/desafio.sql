CREATE TABLE clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE combustiveis (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE carros (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idcombustivel INT,
    FOREIGN KEY (idcombustivel) REFERENCES combustiveis(idcombustivel)
);

CREATE TABLE vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE locacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    kmCarro INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES vendedores(idVendedor)
);

INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente FROM tb_locacao;

INSERT INTO combustiveis (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel FROM tb_locacao;

INSERT INTO carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel FROM tb_locacao;

INSERT INTO vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM tb_locacao;

INSERT INTO locacoes (idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor FROM tb_locacao;
