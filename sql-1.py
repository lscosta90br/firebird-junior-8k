import fdb

con = fdb.connect(
    dsn='localhost:c:\data\Millennium.fdb',
    user='sysdba', password='masterkey',
    # dialect=1, # necessary for all dialect 1 databases
    # charset='UTF8' # specify a character set for the connection
    )

# con = fdb.connect(dsn='/temp/test.db', user='sysdba', password='masterkey')

# Create a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("SELECT r.CARGO, r.COD_CARGO, r.DESCRICAO, r.VENDEDOR, r.GERENTE, r.SUPERVISOR, r.OPERADOR_CAIXA, r.COMPRADOR, r.ESTILISTA, r.MODELISTA, r.CONTATO_GERADOR, r.MOTORISTA FROM CARGOS r")

# Retrieve all rows as a sequence and print that sequence:
print (cur.fetchall())