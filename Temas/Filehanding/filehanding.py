fileselected = "C:/Users/penil/OneDrive/Escritorio/ITESO/Semestres/1ero/Clases/Algoritmos/PythonPracticas/Temas/Filehanding/demofile.txt"
newfile = "C:/Users/penil/OneDrive/Escritorio/ITESO/Semestres/1ero/Clases/Algoritmos/PythonPracticas/Temas/Filehanding/newdemofile.txt"

'''

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''


# f = open("demofile.txt")
# f = open("demofile.txt", "rt")
f = open(fileselected, "rt")

print(f)
print(f.read()) 
f.close() 

#Cambiamos rt por r
f = open(fileselected, "r")
print(f.read(5)) #Le pongo el limite de caracteres que lee
f.close() 


print("----------Leer hasta el final----------------")

with open(fileselected, "r") as f:
    contenido = f.read()  # Lee todo el contenido del archivo
    print(contenido)


print("----------Por bloques----------------")
i = 100  # Número de caracteres a leer en cada iteración

with open(fileselected, "r") as f:
    while True:
        bloque = f.read(i)  # Lee hasta i caracteres
        if not bloque:  # Si no hay más datos, sal del bucle
            break
        print(bloque)  # Imprime el bloque leído

'''
Explicación del código

    with open(...) as f:: Este contexto asegura que el archivo se cierre 
        automáticamente al final del bloque, incluso si ocurre un error.
        
    f.read(i): Lee hasta i caracteres del archivo.
    
    if not bloque:: Verifica si bloque está vacío, lo que indica que hemos llegado al
        final del archivo. Si está vacío, se sale del bucle.
        
    print(bloque): Imprime el bloque de texto leído.

'''

print("----------Con un ciclo for----------------")

with open(fileselected, "r") as f:
    for x in f:
        print(x) 
        
        
#Recuerda siempre cerrar los archivos

# En la primera vez lo va a actualizar, mejor lo comento
f = open(fileselected, "a")
# f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open(fileselected, "r")
print(f.read()) 


# Nuevo archivo
f = open(newfile, "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open(newfile, "r")
print(f.read())

f = open(newfile, "x") 