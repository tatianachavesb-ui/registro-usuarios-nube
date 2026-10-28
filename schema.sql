CREATE DATABASE IF NOT EXISTS ingenieria_web CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE ingenieria_web;

CREATE TABLE IF NOT EXISTS usuario (
    cedula VARCHAR(15)  NOT NULL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
