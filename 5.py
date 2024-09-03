currentString = input("Digite uma string para reverter: ")

reverseString = ""
i = len(currentString) - 1
while i >= 0:
    reverseString += currentString[i]
    i -=1

print("A string reverse é dada por {reverse}".format(reverse=reverseString))

