import sqlite3

# conectando ....
conn = sqlite3.connect('clientes.db')

# Definindo um cursor
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Thais', 26, '00000000000', 'thais@email.com', '11-0000-4321', 'Betim', 'MG', '2021-05-06'),
('Daniel', 28, '00000000000', 'daniel@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2021-05-06'),
('Melissa', 18, '00000000000', 'melisa@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2021-05-06')
""")


# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
