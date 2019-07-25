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


def cria_dicionario_registro_new(tamanho_new, quantidade_new, registros):
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
    #limpa os dicionarios para as proximas linhas
    

def zera_lista_tamanho():
    tam_new.clear()
    qtde_new.clear()

def imprime_registro_em_tela(imprime):
    if imprime == 'S':
        for d in data_new:
            print(d)


def gera_csv(arquivo, cabecalho, linhas, gera):
    if gera == 'S':
        with open(arquivo, mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = cabecalho
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";") 
            writer.writeheader()
            for d in linhas:
                writer.writerow(d)


data = ler_csv('showroom-csv_v02.csv')
lines_data = len(data) + 1

#cria variaveis para for
cor_proxima = ''
tamanhos = ''
data_new = [] #lista
registro_new = {} #dicionario
tam_new = [] #lista
qtde_new = [] #lista
for num_line in range(lines_data):
    codigo = data[num_line]['Codigo'] 
    descricao = data[num_line]['Descricao'] 
    cor = data[num_line]['Cor'] 
    tam =  data[num_line]['Tam'] 
    tam_letra = tam[11:]
    qtde_ped =  data[num_line]['Qtde Ped.'] 

    num_line_plus_plus = num_line + 2
    codigo_anterior = data[num_line - 1]['Codigo'] 
    if (codigo != codigo_anterior) and (num_line_plus_plus) == lines_data:
        cria_dicionario_registro_new(tamanho_new=tam_new, 
                            quantidade_new=qtde_new, 
                            registros={'codigo': codigo, 'descricao': descricao, 'cor': cor},
                        )

    if num_line_plus_plus == lines_data:
        break
    else:
        zera_lista_tamanho()

    #compara cor corrente com proxima cor e codigo_corrent com codigo_proximo 
    # agrupando tam e qtd de codigos iguais
    codigo_proximo = data[num_line + 1]['Codigo']     
    cor_proxima = data[(num_line + 1)]['Cor'] 
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
                                )

imprime_registro_em_tela(imprime='S')
gera_csv(arquivo='zshowroom-19.csv', 
        cabecalho=['codigo', 'descricao', 'cor', 'P', 'PP','M', 'MM', 'G', 'GG'] , 
        linhas=data_new,
        gera='S'
    )
