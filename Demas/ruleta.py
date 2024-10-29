import random
participantes = 6
n1 = random.randint(1,participantes)
n2 = random.randint(1,participantes)
while n2 == n1:
    n2 = random.randint(1,6)
print(f"n2 -> {n2} n1 -> {n1}")

