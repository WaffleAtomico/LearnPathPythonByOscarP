frase = "Hello world"

# 1. capitalize
capitalized = frase.capitalize()
print("capitalize:", capitalized)  # "Hello world"

# 2. casefold
casefolded = frase.casefold()
print("casefold:", casefolded)  # "hello world"

# 3. count
count_h = frase.count('o')
print("count 'o':", count_h)  # 2

# 4. find
find_h = frase.find('world')
print("find 'world':", find_h)  # 6 (posición de la primera aparición)

# 5. index
try:
    index_h = frase.index('world')
    print("index 'world':", index_h)  # 6
except ValueError:
    print("'world' no encontrado")

# Métodos adicionales de búsqueda

# 6. rfind
rfind_h = frase.rfind('o')
print("rfind 'o':", rfind_h)  # 7 (posición de la última aparición)

# 7. rindex
try:
    rindex_h = frase.rindex('o')
    print("rindex 'o':", rindex_h)  # 7
except ValueError:
    print("'o' no encontrado")

# 8. startswith
starts_with_hello = frase.startswith('Hello')
print("startswith 'Hello':", starts_with_hello)  # True

# 9. endswith
ends_with_world = frase.endswith('world')
print("endswith 'world':", ends_with_world)  # True

# 10. split
split_frase = frase.split()
print("split:", split_frase)  # ['Hello', 'world']

# 11. join
joined = " ".join(split_frase)
print("join:", joined)  # "Hello world"

# 12. replace
replaced = frase.replace('world', 'Python')
print("replace 'world' with 'Python':", replaced)  # "Hello Python"
