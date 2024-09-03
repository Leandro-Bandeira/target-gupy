import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

# Leitura do menor valor ocorrido 
# Estamos considerando o menor faturamento, ignorando o zero
menorValor = dados[0]['valor']
menorValorDia = dados[0]['dia']
maiorValor = dados[0]['valor']
maiorValorDia = dados[0]['dia']
sum = 0
count_dias = 0
for valor in dados:
    
    if valor['valor'] != 0 :
        count_dias += 1
        sum += valor['valor']


    if  valor['valor'] != 0 and valor['valor'] < menorValor:
        menorValor = valor['valor']
        menorDia = valor['dia']

    if valor['valor'] > maiorValor:
        maiorValor = valor['valor']
        maiorDia = valor['dia']
    

media = sum/count_dias
print("Maior Valor : {maiorValor}, dia: {diaMaior}\nMenor Valor: {menorValor}, dia: {menorDia}\n Media = {media}".format(maiorValor=maiorValor,
                                                           diaMaior=maiorDia, menorValor=menorValor, menorDia=menorDia, media=media))
    
