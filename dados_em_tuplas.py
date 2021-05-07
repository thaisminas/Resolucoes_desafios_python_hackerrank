import sqlite3

# conectando ....
conn = sqlite3.connect('clientes.db')

# Definindo um cursor
cursor = conn.cursor()

# criando uma lista de dados

lista = [('Thais', 26,'44444444444', 'thaisminas@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2021-05-06'),
('Carla', 20,'44444444444', 'carla@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2021-05-06'),
('Marta', 23,'44444444444', 'marta@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2021-05-06')]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)

conn.commit()

print('Dados Inseridos com sucesso.')

conn.close()