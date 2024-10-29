print("Servicio de telefonia")
print("Ingrese la clave de pais")
criterios = {1: ["Estados unidos", 0.13],2: ["Canadá", 0.11],5: ["América del sur", 0.22],6: ["America Central", 0.19],7: ["México", 0.17],9: ["Europa", 0.17],10: ["Asia", 0.20],15: ["Africa", 0.39],20: ["Oceanía", 0.28]}
print(f"{'Clave':<10} {'Zona':<20} {'Precio':<10}")
for key, value in criterios.items():
    print(f"{key:<10} {value[0]:<20} ${value[1]:<10.2f}") 
clave, time = int(input("Clave:")), int(input("Segundos de llamada:"))
print(f"Costo final: ${criterios[clave][1] * time:.2f}" if clave in criterios else "Digite una clave válida")  

'''
match clave:
    case 1:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 2:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 5:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 6:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 7 | 9:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 10:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 15:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case 20:
        print(f"Costo final: ${criterios[clave][1] * time:.2f}")
    case _:
        print("Digite una clave válida")
'''