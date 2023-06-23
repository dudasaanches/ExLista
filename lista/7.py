num = []
while True:
    escolha = int(input("Adicione um número: "))
    if escolha in num:
        num.pop()
    num.append(escolha)
    sair = str(input("Quer sair?"))
    if sair == "s":
        break
num.sort()
print(num)