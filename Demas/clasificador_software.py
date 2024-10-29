final_price = 0.0  # Precio final

''' Recomendacion de ia para hacerlo mas pythonic
# Diccionario para mapear tipos de software
software_types = {
    1: "Sistema Operativo",
    2: "Suite de Oficina",
    3: "Herramienta de Desarrollo",
    4: "Otro"
}
'''

# Solicitar tipo de software
print("Tipo de software")
print("    1- Sistema Operativo")
print("    2- Suite de Oficina")
print("    3- Herramienta de Desarrollo")
print("    4- Otro")
try:
    type_ = int(input("Ingrese el tipo de software: "))
except:
    type_  = 4
try:   
    price = float(input("Precio: "))
except:
    price  = 50
try:
    is_open = bool(int(input("¿Es código abierto? Escribir: 1 (Sí) o 0 (No): ")))
except:
    is_open = True



str_open = "libre" if is_open else "propietario"

# Clasificador de software
print("Clasificador de software")

if not is_open:
    if type_ == 1 and price > 100:
         final_price = price * 0.90  # 10% de descuento
    elif type_ == 2 and price > 50:
        final_price = price * 0.85  # 15% de descuento
    elif type_ == 3 and price > 80:
        final_price = price * 0.80  # 20% de descuento
    else: #type_ == 4:
        final_price = price  # No aplicar descuento
else:
    final_price = 0  # Si es libre, no hay descuento

    
# Determinar el tipo de software
if type_ == 1:
    str_type = "Sistema Operativo"
elif type_ == 2:
    str_type = "Suite de Oficina"
elif type_ == 3:
    str_type = "Herramienta de Desarrollo"
elif type_ == 4:
    str_type = "Otro"

# str_type = software_types.get(type_, "Desconocido")

# Mostrar resultados

resp = " Tipo: {0} \n El software es: {1}\n Precio base: ${2:,.2f}\n Precio final: ${3:,.2f}\n"
print(resp.format(str_type, str_open, price, final_price))

