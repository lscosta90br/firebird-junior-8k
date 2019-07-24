import csv

file_name = "showroom-csv_v02.csv"
try:
    csvfile = open(file_name, 'rt')
except:
    print("Arquivo não encontrado")
csvReader = csv.DictReader(csvfile, delimiter=";")

# for lista in csvReader:
#     for k, v in lista.items():
#         print(f'O campo {k} tem valor {v}.')

data = [cr for cr in csvReader]
lines_data = len(data) 
cor_proxima = ''
tamanhos = ''

data_new = [] #lista
registro_new = {} #dicionario
tam_new = [] #lista
qtde_new = [] #lista

for num_line in range(lines_data):

    if num_line + 1  == (lines_data):
        break

    codigo = data[num_line]['Codigo'] 
    codigo_proximo = data[num_line + 1]['Codigo']     
    descricao = data[num_line]['Descricao'] 
    cor = data[num_line]['Cor'] 
    cor_proxima = data[(num_line + 1)]['Cor'] 
    tam =  data[num_line]['Tam'] 
    tam_letra = tam[11:]
    qtde_ped =  data[num_line]['Qtde Ped.'] 
    # print(f'numero linhas:{num_line} proximo:{num_line + 1} total linhas:{lines_data}')

    if (cor == cor_proxima) and (codigo == codigo_proximo):
        
        tam_new.append(tam_letra)
        qtde_new.append(qtde_ped)
    else:
        tam_new.append(tam_letra)
        qtde_new.append(qtde_ped)
        tamanhos = [list(x) for x in zip(tam_new, qtde_new)]
        registro_new = {'codigo': codigo, 'descricao': descricao, 'cor': cor, 'tam': tamanhos}
        # print(f'{num_line};{codigo};{descricao};{tamanhos}')
        print(registro_new)
        tam_new.clear()
        qtde_new.clear()



    # if (cor == cor_proxima) and (codigo == codigo_proximo):
    #     print(f'{num_line};{codigo};{descricao};{cor};{tamanhos}')
#         tamanhos = tamanhos + tam_letra +  ';' + qtde_ped + ';'
#         tamanhos_ultimo = tamanhos_ultimo + tam_letra +  ';' + qtde_ped + ';'
#     else:
#         tamanhos = tamanhos + tam_letra + ';' + qtde_ped + ';'
#         tamanhos_ultimo = tamanhos_ultimo + tam_letra + qtde_ped + ';'
#         print(f'{num_line};{vendedor};{codigo};{descricao};{cor};{tamanhos};{valor_pedido};{v_unit}')
#         tamanhos = ''


# for num_line in range(lines_data):
#     vendedor = data[num_line]['Vendedor']
#     codigo = data[num_line]['Codigo'] 
#     descricao = data[num_line]['Descricao'] 
#     cor = data[num_line]['Cor'] 
#     tam =  data[num_line]['Tam'] 
#     tam_numero = tam[:11]
#     tam_letra = tam[11:]
#     qtde_ped =  data[num_line]['Qtde Ped.'] 
#     valor_pedido =  data[num_line]['Valor pedido'] 
#     v_unit=  data[num_line]['V. Unit.'] 
    
#     proximo = num_line + 1
#     anterior = num_line - 1
#     codigo_anterior = data[anterior]['Codigo'] 

#     if (codigo != codigo_anterior) and (proximo + 1) == lines_data:
#         tam =  data[num_line]['Tam'] 
#         tam_letra = tam[11:]
#         tamanhos_ultimo = tam_letra + ';' + qtde_ped 

#     if (proximo + 1) == lines_data:
#         print(f'{num_line};{vendedor};{codigo};{descricao};{cor};{tamanhos_ultimo};{valor_pedido};{v_unit}')
#         break
#     else:
#         tamanhos_ultimo = ''

#     cor_proxima = data[proximo]['Cor'] 
#     codigo_proximo = data[proximo]['Codigo'] 
#     valor_pedido_proximo =  data[proximo]['Valor pedido']
#     if (cor == cor_proxima) and (codigo == codigo_proximo):
#         tamanhos = tamanhos + tam_letra +  ';' + qtde_ped + ';'
#         tamanhos_ultimo = tamanhos_ultimo + tam_letra +  ';' + qtde_ped + ';'
#     else:
#         tamanhos = tamanhos + tam_letra + ';' + qtde_ped + ';'
#         tamanhos_ultimo = tamanhos_ultimo + tam_letra + qtde_ped + ';'
#         print(f'{num_line};{vendedor};{codigo};{descricao};{cor};{tamanhos};{valor_pedido};{v_unit}')
#         tamanhos = ''
