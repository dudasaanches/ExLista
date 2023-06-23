num1 = []
while True:
    num = int(input("Digite os números(Digite 0 se deseja parar): "))
    num1.append(num)
    if num == 0:
        num1.remove(0)
        break

soma = sum(num1)
menor = min(num1)
print(f"Soma: {soma}")
print(f"Menor: {menor}")