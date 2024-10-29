value = int(input("Cuantos terminos de fibonacci deseas generar: "))
final = 0
n1 = 0
n2 = 1
numbers = [n1, n2]
for _ in range(0, value-2):
    final = n1 + n2
    print(f"{n1} + {n2} = {final}")
    n1 = n2
    n2 = final
    numbers.append(final)
print(numbers if value-2 > 3 else numbers[:value])