num1 = []
multi = 1
while True:
    num = int(input("Digite os números(Digite 0 se deseja parar): "))
    num1.append(num)
    if num == 0:
        num1.remove(0)
        break
soma = sum(num1)
maior = max(num1)
menor = min(num1)
for i in num1:
    multi *= i
print(f"Soma: {soma}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Multiplicação: {multi}")