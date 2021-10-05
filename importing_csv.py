# import csv

# arquivo = csv.reader(open('vendas.csv'), delimiter=';')

# for [codigo, qtde, pccompra, pcvenda] in arquivo:
#     print('{} - {} - {} - {}'.format(codigo, qtde, pccompra, pcvenda))

import sqlite3, csv

connection = sqlite3.connect('loja.db')
cur = connection.cursor()

try:
    cur.execute("""
        CREATE TABLE vendas (
            codigo INTEGER,
            qtde INTEGER,
            pccompra FLOAT,
            pcvenda FLOAT
        )
    """)
except:
    pass

reader = csv.reader(open('vendas.csv'), delimiter=';')

for [codigo, qtde, pccompra, pcvenda] in reader:
    count = 0
    cur.execute('INSERT INTO vendas VALUES (?,?,?,?)', (codigo, qtde, pccompra, pcvenda))

    count += 1
connection.commit()
connection.close()

print('\n{} Dados importados com sucesso!'.format(count))