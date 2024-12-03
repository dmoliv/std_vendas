CREATE TABLE regiao(
	cod_regiao INT,
	nome_regiao VARCHAR(20),
    CONSTRAINT pk_cod_reg PRIMARY KEY(cod_regiao));


create table clientes (
    cod_cliente int, 
    nom_cliente varchar(50), 
    cod_regiao int, 
    cpf char(11), 
    sexo char(1),
    CONSTRAINT pk_cod_cli PRIMARY KEY(cod_cliente),
    CONSTRAINT fk_cli_reg FOREIGN KEY (cod_regiao) REFERENCES regiao (cod_regiao)
    );


create table produtos (
	cod_produto char(5),
    desc_produto varchar(200),
    preco decimal(10,2),
    CONSTRAINT pk_cod_prod PRIMARY KEY(cod_produto)
    );

create table vendas (
	num_transac serial, 
    data date, 
    cod_cliente int, 
    cod_produto char(5), 
    quantidade int,
    CONSTRAINT pk_cod_trans PRIMARY KEY(num_transac),
    CONSTRAINT fk_vd_cli FOREIGN KEY (cod_cliente) REFERENCES clientes (cod_cliente),
    CONSTRAINT fk_vd_prod FOREIGN KEY (cod_produto) REFERENCES produtos (cod_produto)
    );