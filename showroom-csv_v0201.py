import uteis as u 


# joga o arquivo csv em memoria
data = u.ler_csv('showroom-csv_v02.csv')

lines_data = len(data) 

campos= { 
    'codigo': 'Codigo',
    'descricao': 'Descricao',
    'cor': 'Cor',
    'tam': 'Tam',
    'quantidade': 'Qtde Ped.',
    }


for num_line in range(lines_data):
    for k,v in campos.items():
        exec(k +" = data[" + "num_line" +"]['"+ v + "']" )
        # print(k +" = data[" + "num_line" +"]['"+ v + "']" )
        

        
    tamanho = u.ajusta_tamanho(tamanho=tam)

    if num_line <= (lines_data -2):
        codigo_proximo = data[num_line + 1]['Codigo']
        cor_proxima = data[(num_line + 1)]['Cor'] 
        u.cria_adicao_lista(num_line=num_line, tamanho=tamanho, quantidade=quantidade,
                cor=cor, cor_proxima=cor_proxima, codigo = codigo, codigo_proximo=codigo_proximo,
                registros=
                    { 'codigo': codigo,
                    'descricao': descricao, 
                    'cor': cor
                    })

data_last = u.data_new


lines_data2 = len(data) - 1
# print(f's-007 lines_data2:{lines_data2}')

para_for = True # refine parar como booleanos
tamanho_new = [] #lista
quantidade_new = [] #lista
registro_new = {} #dicionario
data_new = [] #lista
for num_line in range(lines_data2, -1, -1):
    for k,v in campos.items():
        exec(k +" = data[" + "num_line" +"]['"+ v + "']" )
        # print(k +" = data[" + "num_line" +"]['"+ v + "']" )
    
    tamanho = u.ajusta_tamanho(tamanho=tam)

    # print(f's048. num_line:{num_line} lines_data2:{lines_data2} codigo: {codigo}' )
    cor_ultimo = data[lines_data2]['Cor'] 
    codigo_ultimo = data[lines_data2]['Codigo'] 

    if (cor == cor_ultimo) and (codigo == codigo_ultimo):
        tamanho_new.append(tamanho)
        quantidade_new.append(quantidade)
        # print(f's055. => num_line: {num_line} tamanho_new: {tamanho_new} quantidade_new:{quantidade_new}')    

        registros={ 'codigo': codigo, 'descricao': descricao, 'cor': cor}
    else:
        u.adicao_tamanho_completo(tamanho= tamanho_new, quantidade=quantidade_new)
        tamanhos = dict(zip(tamanho_new, quantidade_new))
        # print(f's058.=> num_line: {num_line} tamanhos: {tamanhos}')    
        
        registro_new = registros
        registro_new.update(tamanhos)
        # print(f's078. => num_line: {num_line} registro_new: {registro_new}')

        data_last.append(registro_new)
        break

u.gera_csv(arquivo='zshowroom-19.csv', 
        cabecalho=['codigo', 'descricao', 'cor', 'P', 'PP', 'M', 'G', 'GG', 'T2', 'T4', 'T6', 'T8', 'T10'], 
        linhas=data_last,
        gera='S'
    )

# print(f's069 data_last {data_last}')


