import csv


def ajusta_tamanho(tamanho):
    tamanho = tamanho[11:]
    if is_int(tamanho) == True:
        tamanho = 'T' + tamanho 
        # print(f'tam_letra numero: {tam_letra}')
        return tamanho
    else:
        # print(f'tam_letra so letra: {tam_letra}')
        return tamanho


tamanho_new = [] #lista
quantidade_new = [] #lista
registro_new = {} #dicionario
data_new = [] #lista
def cria_adicao_lista(num_line, tamanho, quantidade,  
                    cor, cor_proxima, codigo, codigo_proximo,
                    registros
                 ):
    if (cor == cor_proxima) and (codigo == codigo_proximo):
        # agrupa tamnaho e quantidade
        tamanho_new.append(tamanho)
        quantidade_new.append(quantidade)
    else:
        tamanho_new.append(tamanho)
        quantidade_new.append(quantidade)
        # print(f'u030.cria_adicao_lista=> num_line: {num_line} tamanho_new: {tamanho_new} quantidade_new:{quantidade_new}')


        # transforma lista em dicionario  tam_new ['P', 'M', 'G'] e qtde_new['2', '1', '1']
        # em dicionario tamanhos { 'P': '2', 'M': '1', 'G': '1'}
        tamanhos = dict(zip(tamanho_new, quantidade_new))
        # print(f'u036.cria_adicao_lista=> num_line: {num_line} tamanhos: {tamanhos}')

        # cria dicionario => codigo, descricao e cor
        registro_new = registros

        # adiciona ao dicionario => (codigo, descricao e cor) + (tam e quantidade)
        registro_new.update(tamanhos)
        # print(f'u043.cria_adicao_lista=> num_line: {num_line} registro_new: {registro_new}')

        #adiciona dicionario na lista 
        data_new.append(registro_new)

        # limpa lista tamanho_new e quantidade_new
        tamanho_new.clear()
        quantidade_new.clear()
        # return data_new


def is_int(valor):
    try:
        int(valor)
        return True
    except:
        return False


def ler_csv(arquivo):
    try:
        csvfile = open(arquivo, 'rt')
    except:
        print("Arquivo não encontrado")

    csvReader = csv.DictReader(csvfile, delimiter=";")
    data = [cr for cr in csvReader]
    return data


#     # # print(f'p002 num_line:{num_line} tam_letra: {tam_letra}')
def gera_csv(arquivo, cabecalho, linhas, gera):
    if gera == 'S' or gera == 's':
        with open(arquivo, mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = cabecalho
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";") 
            writer.writeheader()
            for d in linhas:
                writer.writerow(d)










# def adiciona_lista(tamanho, quantidade):
#     # cria o ultimo item da lista com tamanhos e quantidades
#     tam_new.append(tamanho)
#     qtde_new.append(quantidade)


# def cria_dicionario_registro_new(tamanho_new, quantidade_new, registros):
#     adiciona_lista(tam_letra, qtde_ped)
#     # transforma lista em dicionario  tam_new ['P', 'M', 'G'] e qtde_new['2', '1', '1']
#     # em dicionario tamanhos { 'P': '2', 'M': '1', 'G': '1'}
#     tamanhos = dict(zip(tamanho_new, quantidade_new))
#     # cria dicionario => codigo, descricao e cor
#     registro_new = registros
#     # adiciona ao dicionario => (codigo, descricao e cor) + (tam e quantidade)
#     registro_new.update(tamanhos)
#     #adiciona dicionario na lista 
#     data_new.append(registro_new)
#     #limpa os dicionarios para as proximas linhas
    
# tam_new = [] #lista
# qtde_new = [] 
# def zera_lista_tamanho():
#     tam_new.clear()
#     qtde_new.clear()

# def imprime_registro_em_tela(imprime):
#     if imprime == 'S':
#         for d in data_new:
#             print(d)


# def gera_csv(arquivo, cabecalho, linhas, gera):
#     if gera == 'S':
#         with open(arquivo, mode='w', encoding='utf-8', newline='') as csv_file:
#             fieldnames = cabecalho
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";") 
#             writer.writeheader()
#             for d in linhas:
#                 writer.writerow(d)

