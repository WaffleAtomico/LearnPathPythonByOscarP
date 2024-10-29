import pandas as pd

criterios = {
    1: ["Industrial", 6, 8.5],
    2: ["Sistemas", 5, 9.0],
    3: ["Mecatronica", 6, 8.8],
    4: ["Ciberseguridad", 7, 9.0], 
}
df = pd.DataFrame(criterios)

print("Carreras disponibles:")
for x in criterios:
    print(f"{x} --> {df.iloc[0, (x-1)]}")

selected = int(input("Ingrese la clave de la carrera solicitada: "))
semester = int(input("Semestre: "))
average = int(input("Promedio: "))

resp = "Aceptado"
# Se puede hacer mas rapido sin switch, de esta manera

# if semester < df.iloc[1, selected]:
#     resp = "No cumples con semestre "
# if average < df.iloc[2, selected]:
#     if resp != "Aceptado":
#           resp += "y no cumples con el promedio "
#     else:
#         resp = "No cumples con el promedio "

match selected:
    case 1:
        if semester < df.iloc[1, selected]:
            resp = "No cumples con semestre "
        if average < df.iloc[2, selected]:
            if resp != "Aceptado":
                resp += "y no cumples con el promedio "
            else:
                resp = "No cumples con el promedio "

    case 2:
        if semester < df.iloc[1, selected]:
            resp = "No cumples con semestre "
        if average < df.iloc[2, selected]:
            if resp != "Aceptado":
                resp += "y no cumples con el promedio "
            else:
                resp = "No cumples con el promedio "

    case 3:
        if semester < df.iloc[1, selected]:
            resp = "No cumples con semestre "
        if average < df.iloc[2, selected]:
            if resp != "Aceptado":
                resp += "y no cumples con el promedio "
            else:
                resp = "No cumples con el promedio "

    case 4:
        if semester < df.iloc[1, selected]:
            resp = "No cumples con semestre "
        if average < df.iloc[2, selected]:
            if resp != "Aceptado":
                resp += "y no cumples con el promedio "
            else:
                resp = "No cumples con el promedio "

print(resp)