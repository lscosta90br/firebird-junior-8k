import csv

file_name = "showroom.csv"
try:
    csvfile = open(file_name, 'rt')
except:
    print("Arquivo não encontrado")
csvReader = csv.DictReader(csvfile, delimiter=";")

data = [cr for cr in csvReader]

lines_data = len(data) + 1
cor_proxima = ''
tamanhos = ''
for num_line in range(lines_data):
    codigo = data[num_line]['Codigo'] 
    descricao = data[num_line]['Descricao'] 
    cor = data[num_line]['Cor'] 
    tam =  data[num_line]['Tam'] 
    tam_numero = tam[:11]
    tam_letra = tam[11:]
    qtde_ped =  data[num_line]['Qtde Ped.'] 
    valor_pedido =  data[num_line]['Valor pedido'] 
    v_unit=  data[num_line]['V. Unit.'] 
    
    proximo = num_line + 1
    anterior = num_line - 1
    codigo_anterior = data[anterior]['Codigo'] 

    if (codigo != codigo_anterior) and (proximo + 1) == lines_data:
        tam =  data[num_line]['Tam'] 
        tam_letra = tam[11:]
        tamanhos_ultimo = tam_letra

    if (proximo + 1) == lines_data:
        print(f'{num_line};{codigo};{descricao};{cor};{tamanhos_ultimo};{qtde_ped};{valor_pedido};{v_unit}')
        break
    else:
        tamanhos_ultimo = ''

    cor_proxima = data[proximo]['Cor'] 
    codigo_proximo = data[proximo]['Codigo'] 
    valor_pedido_proximo =  data[proximo]['Valor pedido']
    if (cor == cor_proxima) and (valor_pedido == valor_pedido_proximo) and (codigo == codigo_proximo):
        tamanhos = tamanhos + tam_letra +  ';' 
        tamanhos_ultimo = tamanhos_ultimo + tam_letra +  ';' 
    else:
        tamanhos = tamanhos + tam_letra
        tamanhos_ultimo = tamanhos_ultimo + tam_letra
        print(f'{num_line};{codigo};{descricao};{cor};{tamanhos};{qtde_ped};{valor_pedido};{v_unit}')
        tamanhos = ''
