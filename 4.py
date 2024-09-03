
faturamentos = [67836.43,36678.66,29299.88,27165.48,19849.53]

sum = 0
for faturamento in faturamentos:
    sum += faturamento

i = 0
for faturamento in faturamentos:
    percent = faturamento / sum * 100
    if i == 0:
        print("Porcentagem SP: {percent}".format(percent=percent))
    elif i == 1:
        print("Porcentagem RJ: {percent}".format(percent=percent))
    elif i == 2:
        print("Porcentagem MG: {percent}".format(percent=percent))
    elif i == 3:
        print("Porcentagem ES: {percent}".format(percent=percent))
    elif i == 4:
        print("Porcentagem Outros: {percent}".format(percent=percent))
    i += 1

