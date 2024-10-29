def fibbonacci(n1, n2, position):
  if position == 0:
    return n1
  else:
    print("Fibbonacci numero: ", n1)
    return fibbonacci((n1 + n2), n1, position - 1)

print("Final: ", fibbonacci(1, 0, 5))