import csv


def ler_csv(arquivo):
    try:
        csvfile = open(arquivo, 'rt')
    except:
        print("Arquivo não encontrado")

    csvReader = csv.DictReader(csvfile, delimiter=";")
    data = [cr for cr in csvReader]
    return data


def adiciona_lista(tamanho, quantidade):
    # cria o ultimo item da lista com tamanhos e quantidades
    tam_new.append(tamanho)
    qtde_new.append(quantidade)


def cria_dicionario_registro_new(tamanho_new, quantidade_new, registros, imprime_tela):
    adiciona_lista(tam_letra, qtde_ped)
    # transforma lista em dicionario  tam_new ['P', 'M', 'G'] e qtde_new['2', '1', '1']
    # em dicionario tamanhos { 'P': '2', 'M': '1', 'G': '1'}
    tamanhos = dict(zip(tamanho_new, quantidade_new))
    # cria dicionario => codigo, descricao e cor
    registro_new = registros
    # adiciona ao dicionario => (codigo, descricao e cor) + (tam e quantidade)
    registro_new.update(tamanhos)
    #adiciona dicionario na lista 
    data_new.append(registro_new)
    if imprime_tela == 'S':
        print(registro_new)
    #limpa os dicionarios para as proximas linhas
    tam_new.clear()
    qtde_new.clear()

def gera_csv(arquivo, cabecalho, linhas, gera):
    if gera == 'S':
        with open(arquivo, mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = cabecalho
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";") 
            writer.writeheader()
            for d in linhas:
                writer.writerow(d)


data = ler_csv('showroom-csv_v02.csv')
lines_data = len(data)

#cria variaveis para for
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

    #compara cor corrente com proxima cor e codigo_corrent com codigo_proximo 
    # agrupando tam e qtd de codigos iguais
    if (cor == cor_proxima) and (codigo == codigo_proximo):
        # cria uma lista com tamanhos e quantidades
        # tam_new.append(tam_letra)
        # qtde_new.append(qtde_ped)
        adiciona_lista(tam_letra, qtde_ped)
    else:
        # cria o ultimo item da lista com tamanhos e quantidades
        cria_dicionario_registro_new(tamanho_new=tam_new, 
                                    quantidade_new=qtde_new, 
                                    registros={'codigo': codigo, 'descricao': descricao, 'cor': cor},
                                    imprime_tela='S'
                                )

gera_csv(arquivo='zshowroom-19.csv', 
        cabecalho=['codigo', 'descricao', 'cor', 'P', 'PP','M', 'MM', 'G', 'GG'] , 
        linhas=data_new,
        gera='S'
    )




# ====================================
    # writer.writeheader()
    # writer.writerow({'nome': 'João Silva', 'depto': 'Contabilidade', 'mes_aniv': 'novembro'})
    # writer.writerow({'nome': 'Catarina Andrade', 'depto': 'Informática', 'mes_aniv': 'março'})



# print(data_new)
# print('-'* 100)

# for dw in data_new:
#     for k, v in dw.items():
#         print(v, end=';' )
#     print()


# data2 = [cr for cr in data2 ]
# lines_data = len(data2) 
# # for  in dw.items():
# for num_line in range(lines_data):
#     codigo = data[num_line]['Codigo'] 
#     print(codigo)