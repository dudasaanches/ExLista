num1 = []
while True:
    num = int(input("Digite os números(Digite 0 se deseja parar): "))
    num1.append(num)
    if num == 0:
        num1.remove(0)
        break
num1.sort(reverse=True)
contagem = len(num1)
print(f"Contagem: {contagem}")
print(f"Ordem decrescene: {num1}")
if 5 in num1:
    print("Possui o número 5 no lista")