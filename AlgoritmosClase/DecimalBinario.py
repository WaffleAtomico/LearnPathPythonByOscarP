num = int(input("Escribe un numero: "))

result = []

while num > 0:
    result.append(num % 2)
    num = num//2

print(result[::-1])