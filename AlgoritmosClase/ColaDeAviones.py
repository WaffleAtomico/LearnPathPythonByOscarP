import random
import time

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
        listaElementos = ''
        while temp:
            listaElementos = listaElementos + f"{temp.data}, "
            # print(temp.data, end=', ')
            #Temporal ahora va a ser la siguiente localidad 
            temp = temp.next 
        # print()
        return listaElementos
    
    def PrintByIndex(self, index=0):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                # print(temp.data)
                return temp.data
            temp = temp.next 
            index +=1
    
    def AppendEnd(self, newData):
        newnode = Node(newData)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
    
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
    
    arribo = LinkedList()
    partida = LinkedList()
    while True:
        print("\nMenú:")
        print("1. Nuevo Arribo")
        print("2. Nueva partida")
        print("3. Ver Estado")
        print("4. Asignar pista")
        print("5. Salir") 
        option = int(input("Seleccione una opción: "))
        
        if option == 5:
            break
        
        match option:
            case 1:
                print("Nuevo Arribo:", end=' ')
                vuelo = input()
                arribo.AppendEnd(vuelo)
                
            case 2:
                print("Nueva Partida:", end=' ')
                vuelo = input()
                partida.AppendEnd(vuelo)
                
            case 3:
                if arribo.CountList() > 0:
                    print('Vuelos esperando para aterrizar: ', arribo.PrintList())
                if partida.CountList() > 0:
                    print('Vuelos esperando para aterrizar: ', partida.PrintList())    
                
            case 4:
                if arribo.CountList() > 0:
                    print(f"El vuelo {arribo.PrintByIndex()} aterrizó con éxito")
                    arribo.DeleteFromBegin()
                elif partida.CountList() > 0:
                    print(f"El vuelo {partida.PrintByIndex()} despegó con éxito")
                    partida.DeleteFromBegin()
                else:
                    print("No hay vuelos en espera")
                
            case _:
                print("Seleccione una opcion valida")
