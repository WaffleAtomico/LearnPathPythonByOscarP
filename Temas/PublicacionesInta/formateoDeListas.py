list1 = "1 2 3 4 5 6"
#   int
#   float
#   list
formatted_list = list(map(int, list1.split()))
print(formatted_list)
# print(list1.split())

print(*formatted_list )             # Ponemos todo fuera de una lista
print(*formatted_list * 2)          # Multiplicamos 2 veces lo que tenemos dentro
print(*[iter(formatted_list)])      # Tenemos que hacerlo una lista de esta lista ya iterable
print(*[iter(formatted_list)]*2)    # Partimos en 2 partes, al parecer acompañan misma direccion de memoria



# Alrevez
# print(*formatted_list)
# final_list = *formatted_list

# if list1 == *formatted_list: