print("Carreras disponibles:")
criterios = {1: ["Industrial", 6, 8.5], 2: ["Sistemas", 5, 9.0], 3: ["Mecatronica", 6, 8.8], 4: ["Ciberseguridad", 7, 9.0], }
for key, value in criterios.items():
    print(f"{key} - {value[0]}")
selected, semester, average, resp = int(input("Ingrese la clave de la carrera solicitada: ")), int(input("Semestre: ")), float(input("Promedio: ")), "Aceptado"
print(("No cumples con el semestre" + (" y no cumples con el promedio" if average < criterios[selected][2] else "") if semester < criterios[selected][1] else ("No cumples con el promedio" if average < criterios[selected][2] else ""))if (semester < criterios[selected][1] or average < criterios[selected][2]) else "Aceptado")

'''
match selected:
    case 1:
    case 2:
        print(("No cumples con el semestre" + (" y no cumples con el promedio" if average < criterios[selected][2] else "") if semester < criterios[selected][1] else ("No cumples con el promedio" if average < criterios[selected][2] else ""))if (semester < criterios[selected][1] or average < criterios[selected][2]) else "Aceptado")
    case 3:
        print(("No cumples con el semestre" + (" y no cumples con el promedio" if average < criterios[selected][2] else "") if semester < criterios[selected][1] else ("No cumples con el promedio" if average < criterios[selected][2] else ""))if (semester < criterios[selected][1] or average < criterios[selected][2]) else "Aceptado")
    case 4:
        print(("No cumples con el semestre" + (" y no cumples con el promedio" if average < criterios[selected][2] else "") if semester < criterios[selected][1] else ("No cumples con el promedio" if average < criterios[selected][2] else ""))if (semester < criterios[selected][1] or average < criterios[selected][2]) else "Aceptado")
    case _:
        print("Ingrese una opcion valida del 1 al 4")
'''
# original 58 aprox -> Esto no refleja ni un codigo legible ni escalable, solo mucho mas corto, es horrendo