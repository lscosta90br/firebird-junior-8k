import csv

file_name = "exemplo-dict.csv"
try:
    csvfile = open(file_name, 'rt')
except:
    print("Arquivo não encontrado")
csvReader = csv.DictReader(csvfile, delimiter=";")

data = [cr for cr in csvReader]
lines_data = len(data) 
cor_proxima = ''
tamanhos = ''

# data_new = [] #lista
# registro_new = {} #dicionario

for num_line in range(lines_data):
    codigo = data[num_line]['codigo'] 
    produto = data[num_line]['produto'] 
    cor = data[num_line]['cor'] 
    tam =  data[num_line]['tam'] 
    tam_letra = tam[5:]
    
    # cor_proxima = data[(num_line)]['Cor'] 
    # codigo_proximo = data[num_line]['Codigo'] 

    proximo = num_line + 1
    print(f' antes do if proximo: {proximo}')
    if (proximo + 1) == lines_data:
        print(f'Proximo if break {proximo+ 1}')
        print(f'{num_line};{codigo};{produto};{cor};{tam_letra}')
        break

    cor_proxima = data[proximo]['cor']
    codigo_proximo = data[proximo]['codigo']
    
    
    if (cor == cor_proxima) and (codigo == codigo_proximo):
        print(f'{num_line};{codigo};{produto};{cor};{tam_letra}')

