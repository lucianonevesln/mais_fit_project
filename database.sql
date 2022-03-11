-- Criando database
create database frameworks_full_stack;

use frameworks_full_stack;

-- Criando tabelas
create table sabores (
   id int auto_increment,
   nome varchar(100) not null,
   descricao varchar(500) not null,
   valor decimal(5,2) not null,
   link varchar(500) not null,
   ativo char(3) not null,
   check (ativo = 'SIM' or ativo = 'NÃO'),
   primary key (id)
);

-- Insercao de dados no database
insert into sabores (nome, descricao, valor, link, ativo)  values ('Pernil com purê de couve-flor e legumes', 'Pernil com purê de couve-flor e legumes', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Escondidinho de batata doce com frango desfiado.', 'Escondidinho de batata doce com frango desfiado.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Frango em pedaços e legumes ao vapor.', 'Frango em pedaços e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Panqueca integral de frango ao molho sugo e legumes ao vapor.', 'Panqueca integral de frango ao molho sugo e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Strogonoff de frango light com arroz integral e legumes ao vapor.', 'Strogonoff de frango light com arroz integral e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Cação ao molho de leite de coco, arroz integral e legumes.', 'Cação ao molho de leite de coco, arroz integral e legumes.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Filé de Tilápia grelhada com purê de abóbora e legumes', 'Filé de Tilápia grelhada com purê de abóbora e legumes', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Lasanha de berinjela com frango desfiado.', 'Lasanha de berinjela com frango desfiado.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Arroz de forno integral à grega de frango, peito de frango e mozarela.', 'Arroz de forno integral à grega de frango, peito de frango e mozarela.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Escondidinho de abóbora com frango desfiado.', 'Escondidinho de abóbora com frango desfiado.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Carne em pedaços e legumes ao vapor.', 'Carne em pedaços e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Arroz de forno integral à grega de carne, peito de frango e mozarela.', 'Arroz de forno integral à grega de carne, peito de frango e mozarela.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Escondidinho de mandioquinha de carne moída.', 'Escondidinho de mandioquinha de carne moída.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Lasanha de berinjela com carne moída.', 'Lasanha de berinjela com carne moída.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Nhoque de batata doce c/ almôndegas ao molho e legumes.', 'Nhoque de batata doce c/ almôndegas ao molho e legumes.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Escondidinho de batata doce com carne moída.', 'Escondidinho de batata doce com carne moída.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Panqueca integral de carne moída ao molho sugo e legumes ao vapor.', 'Panqueca integral de carne moída ao molho sugo e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Quibe assado recheado de queijo.', 'Quibe assado recheado de queijo.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Strogonoff de carne light com arroz integral e legumes ao vapor.', 'Strogonoff de carne light com arroz integral e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Macarrão integral à bolonhesa carne moída e legumes ao vapor.', 'Macarrão integral à bolonhesa carne moída e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Panqueca integral de queijo branco ao molho sugo e legumes ao vapor.', 'Panqueca integral de queijo branco ao molho sugo e legumes ao vapor.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Couve-flor ao molho branco e mozarela com arroz integral.', 'Couve-flor ao molho branco e mozarela com arroz integral.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Strogonoff de legumes c/ palmito e champignon e arroz integral', 'Strogonoff de legumes c/ palmito e champignon e arroz integral', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Lasanha de berinjela 2 queijos.', 'Lasanha de berinjela 2 queijos.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Torta integral de queijo branco e legumes.', 'Torta integral de queijo branco e legumes.', 17.00, 'www.maisfit.com.br', 'SIM');
insert into sabores (nome, descricao, valor, link, ativo)  values ('Charuto de Ricota com arroz integral ao molho sugo.', 'Charuto de Ricota com arroz integral ao molho sugo.', 17.00, 'www.maisfit.com.br', 'SIM');
