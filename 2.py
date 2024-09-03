# O valor será inserido pelo terminal
number = int(input("Digite o valor desejado para achar na sequencia de fibonacci: "))
seqFib = [0,1]
i = 1
isSeqFib = False
if number == 0:
    print("O valor pertence a sequencia")
    exit(1)
while True:
    nextNumber = seqFib[i-1] + seqFib[i]
    if  nextNumber == number:
        isSeqFib = True
        break
    elif nextNumber >= number:
        break


    seqFib.append(nextNumber)
    i += 1

if isSeqFib:
    print("O valor pertence a sequencia")
else:
    print("O valor não pertence a sequencia ")
