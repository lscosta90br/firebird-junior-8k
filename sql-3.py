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
"""
 SELECT = "SELECT MV.DATA_INICIO,MV.DATA_PREVISTO,MV.OFICINA,F.FORNECEDOR,F.OFICINA,F.COD_FORNECEDOR, F.NOME,F.FANTASIA, \
MV.PRODUTO AS PRODUTO_MV, P.PRODUTO AS PRODUTO_P ,P.COD_PRODUTO, P.DESCRICAO_SF,MV.COR AS COR_MV,C.COR AS COR_C,MV.TAMANHO, MV.QUANTIDADE, \
C.DESCRICAO, MV.FLAGOFICINA, MV.PARTE,MV.FASEI, MV.FILIAL, MV.ESTAMPA,MV.PRODUCAO,MV.SITUACAO,MV.SITUACAO,MV.DATA_REAL, MV.FASEF, MV.NUM_CONTROLE \
FROM MOVIMENTO_PRODUCAO  AS MV \
INNER JOIN PRODUTOS AS P ON MV.PRODUTO = P.PRODUTO \
INNER JOIN FORNECEDORES AS F ON MV.OFICINA = F.FORNECEDOR \
INNER JOIN CORES AS C on MV.COR = C.COR \
WHERE MV.FASEI = 1 AND MV.FILIAL = 5 AND MV.DATA_INICIO > '01-05-2019' AND MV.FLAGOFICINA ='S'" 
"""

SELECT = "select cargo, cod_cargo, descricao from cargos"

cur.execute(SELECT)

for fieldDesc in cur.description:
    print (fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE])), 
print() # Finish the header with a newline.
print ('-' * 78)

fieldIndices = range(len(cur.description))
for row in cur:
    for fieldIndex in fieldIndices:
        fieldValue = str(row[fieldIndex])
        fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]

        print (fieldValue.ljust(fieldMaxWidth)) ,

    print()# Finish the row with a newline.
