class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AppendBeggin(self, newData):
        #Instanciamos nodo vaya
        newnode = Node(newData) #No le pasamos self, ya que self solo hace referencia a si mismo
        # Le agregamos al nuevo nodo, en el siguiente se asigna a NONE,
        newnode.next = self.head 
        # Ahora la instancia de la lista, su cabeza va a asignarle al nuevo nodo
        self.head = newnode
     
    def PrintList(self):
        #Se comienza desde la cabeza
        temp = self.head 
        #Mientras temporal no sea falso, o None
        while temp:
            print(temp.data, end=' -> ')
            #Temporal ahora va a ser la siguiente localidad 
            temp = temp.next 
        print()

    def DeleteFromBegin(self):
        if self.head is None:
            return "Empty list" 
        self.head = self.head.next 
   
    def CountList(self):
        temp = self.head
        cont = 0 
        #Por cada elemento que no sea Nulo contamos uno
        while temp:
            temp = temp.next 
            cont +=1
        return cont
    
if __name__ == "__main__":
    listaEnlazada = LinkedList()
    
    while True:
        print("\nMenú:")
        print("1. Añadir elemento a la pila")
        print("2. Sacar elemento de la pila")
        print("3. Longitud de la pila")
        print("4. Mostrar pila")
        print("5. Salir")
        
        option = int(input("Seleccione una opción: "))
        
        if option == 1:
            element = input("Ingrese el elemento a añadir: ")
            listaEnlazada.AppendBeggin(element)
        
        elif option == 2:
            if listaEnlazada.CountList() > 0:
                listaEnlazada.DeleteFromBegin()
                print("Elemento sacado de la pila.")
            else:
                print("La pila está vacía.")
        
        elif option == 3:
            print(f"Ciudades recorridas: {listaEnlazada.CountList()}")
        
        elif option == 4:
            print("Camino a casa: ", end='')
            listaEnlazada.PrintList()
        
        elif option == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")
