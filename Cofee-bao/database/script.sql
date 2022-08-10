
create database cafeteria;
use cafeteria;


create table produto (
	cod int auto_increment,
    nome varchar(40),
    empr varchar(40),
    quan int,
    primary key(cod)

);




create table fabricante(
	id int auto_increment,
    nomeFabri varchar(40),
    primary key (id)
    );
    
    
create table compra(
	cod int auto_increment,
    history_code int,
    primary key(cod)
);




select * from produto;
select * from fabricante;
select * from compra;
