-- Criação do banco de dados em MySQL.

CREATE DATABASE cadastro_db;

USE cadastro_db;

CREATE TABLE cadastros_clientes (
    ID int auto_increment primary key,
    email varchar(100) not null unique,
    senha varchar(50) not null
);