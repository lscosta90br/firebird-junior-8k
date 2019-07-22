import fdb

con = fdb.connect(
    dsn='localhost:c:\data\Millennium.fdb',
    user='sysdba', password='masterkey',
    # dialect=1, # necessary for all dialect 1 databases
    # charset='UTF8' # specify a character set for the connection
    )

import fdb

con = fdb.connect(dsn='c:\data\Millennium.fdb', user='sysdba', password='masterkey')

cur = con.cursor()
SELECT = "select cargo, cod_cargo, descricao from cargos"

cur.execute(SELECT)
# print (cur.fetchall())

for (cargo, cod_cargo, descricao) in cur:
    print(f"Seu código do cargo é: {cod_cargo} e sua descricao é: {descricao}")



