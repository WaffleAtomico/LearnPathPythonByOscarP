# fuente https://www.datacamp.com/es/tutorial/python-linked-lists
class Node: # Esta clase es un objeto, nuestro objeto nodo
    def __init__(self, data): 
        # El método __init__ es un método especial en Python, conocido como constructor
        #Un constructor nos ayuda a poder inicializar un objeto
        #Se inicializa para poderlo utilizar y asginarle valores
        self.data = data
        #self es una referencia a una instancia actual de la clase
        #Donde la instancia actual va a contener una variable
        self.next = None
        #Y la misma instancia, va a tener la siguiente posision
        #En este caso no tiene absolutamente nd


class LinkedList: #Creamos un nuevo objeto, la lista enlazada
    def __init__(self): #Solo necesitamos la misma referencia
        self.head = None 
        '''
        Al establecer self.head como Ninguno, estamos afirmando que la lista enlazada 
        está inicialmente vacía y que no hay nodos en la lista a los que apuntar.
        Cuando se le dan valores la cabeza va a apuntar al primer nodo SIEMPRE
        '''
    
    #CRUD
       
    ''' Create '''
    def AppendBeggin(self, newData):
        #Instanciamos nodo vaya
        newnode = Node(newData) #No le pasamos self, ya que self solo hace referencia a si mismo
        # Le agregamos al nuevo nodo, en el siguiente se asigna a NONE,
        newnode.next = self.head 
        # Ahora la instancia de la lista, su cabeza va a asignarle al nuevo nodo
        self.head = newnode
        
    def AppendEnd(self, newData):
        newnode = Node(newData)
        #Si la cabeza no apunta a nd, entonces es el primero
        if self.head is None:
            self.head = newnode
            return
        #Tomamos el primero que vamos a recorrer hasta el final
        last = self.head
        #Si el siguiente ya no existe, entonces es el ultimo
        while last.next:
            #Del actual al siguiente podemos pasar al siguiente
            last = last.next
        last.next = newnode
         
    ''' Read '''
    def PrintList(self):
        #Se comienza desde la cabeza
        temp = self.head 
        #Mientras temporal no sea falso, o None
        while temp:
            print(temp.data, end=', ')
            #Temporal ahora va a ser la siguiente localidad 
            temp = temp.next 
        print()
    
    def PrintByIndex(self, index=0):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                # print(temp.data)
                return temp.data
            temp = temp.next 
            index +=1
    
    
    ''' Update '''
    def UpdateByValue(self, valueUpdate, up_data):
        #Cambiando el nodo, no solo el valor, para hacer el cambio verdadero y la adaptacion bien
        if self.head is None:
            return "Empty list"
        
        newnode = Node(up_data)
        if self.head.data == valueUpdate:
            #Si el unico que hay, el cual es cabeza, existe, se actualiza
            newnode.next = self.head.next
            self.head = newnode
            return
        
        prev = None
        temp = self.head
        while temp.next.next and (temp.data != valueUpdate):
            prev = temp
            temp = temp.next
        #Asignamos al nodo anterior la union al nuevo nodo
        prev.next = newnode 
        #Asignanos a nuestro actual la siguiente como su siguiente
        newnode.next = temp.next
        #Eliminamos el nodo actual
        temp = None
        
    def UpdateByPosition(self, up_data, ubication):
        if self.head is None:
            return "Empty list"
        
        newnode = Node(up_data)
        if self.head.data is None or ubication == 0:
            newnode.next = self.head.next
            self.head = newnode
            return
        
        temp = self.head
        prev = None
        current_pos = 0
        while temp.next.next and current_pos != ubication:
            prev = temp
            temp = temp.next
            current_pos += 1  
        prev.next = newnode 
        newnode.next = temp.next
        temp = None

    ''' Delete '''   
    def DeleteFromBegin(self):
        if self.head is None:
            return "Empty list" 
        self.head = self.head.next 
        
    def DeleteFromEnd(self):
        if self.head is None:
            return "Empty list"
        if self.head.next is None:
            #Si el siguiente no tiene nd, solo hay 1 y ese se elimina
            self.head = None
            return
        temp = self.head
        #Mientras el siguiente del siguiente exista y haya algo
        while temp.next.next:
            temp = temp.next 
        temp.next = None #Asi se elimina un nodo      
        
    def DeleteNodeByValue(self, rm_data):
        if self.head is None:
            return "Empty list"
        if self.head.data == rm_data:
            #Si el unico que hay, el cual es cabeza, existe, se elimina
            self.head = self.head.next
            return
        temp = self.head
        #Es necesario saber el anterior para saber como lo conectamos con el siguiente
        prev = None
        # while temp.next.next and temp.data != rm_data:
        while temp.next.next and temp.data != rm_data:
            prev = temp
            temp = temp.next
            #termina en temp igual a rm_data
        #ya que necesitamos saber que el siguiente debe de ser el hueco
        # prev: 6 -> Abxd123  -  temp: 7 -> Abxd124      temp.next: X ->
        # prev: 6 -> Abxd124      temp.next: X -> 
        prev.next = temp.next
        temp = None            
        
    def DeleteNodeByPosition(self, ubication):
        if self.head is None:
            return "Empty list"
        if (self.head.data is None and ubication==0) or ubication == 0:
            #Si el unico que hay, el cual es cabeza, existe, se elimina
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        current_pos = 0
        while temp.next.next and current_pos != ubication:
            prev = temp
            temp = temp.next
            current_pos += 1  
        prev.next = temp.next
        temp = None
            
    #EXTRAS 
        
    ''' Count '''
    def CountList(self):
        temp = self.head
        cont = 0 
        #Por cada elemento que no sea Nulo contamos uno
        while temp:
            temp = temp.next 
            cont +=1
        return cont
    
    ''' Search '''
    def SearchInList(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value: {value} is in position {position}"
            current = current.next
            position += 1
        return f"Value: {value} no found in list"
        
if __name__ == "__main__":
    #Instanciamos la lista
    listaEnlazada = LinkedList()
    
    for x in range(10):
        listaEnlazada.AppendEnd(x)
    
    #El ultimo que entra, es el primero que se imprime
    listaEnlazada.PrintList()
    print("Cantidad de elementos",listaEnlazada.CountList())
    
    
    listaEnlazada.DeleteNodeByValue(7)
    print("Se elimina el 7: ")
    listaEnlazada.PrintList()
    print("Cantidad de elementos",listaEnlazada.CountList())

    
    listaEnlazada.DeleteNodeByPosition(4)
    print("Se elimina la posicion 4: ")
    listaEnlazada.PrintList()
    print("Cantidad de elementos",listaEnlazada.CountList())
    
    
    listaEnlazada.UpdateByValue(0, 100)
    print("Se cambia el valor de 0 por 100: ")
    listaEnlazada.PrintList()
    print("Cantidad de elementos", listaEnlazada.CountList())
    
    listaEnlazada.UpdateByPosition(200, 0)
    print("Se cambia en la posicion 0 por 200: ")
    listaEnlazada.PrintList()
    print("Cantidad de elementos", listaEnlazada.CountList())


