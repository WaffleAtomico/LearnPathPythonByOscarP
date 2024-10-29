# Network X

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self): 
        self.head = None
        
    def AppendBeggin(self, newData):
        newnode = Node(newData)
        newnode.next = self.head 
        # Si la lista no está vacía, ajusta el puntero anterior del nodo actual
        if self.head is not None:
            self.head.prev = newnode
        # El nuevo nodo será el primer nodo, así que prev es None    
        newnode.prev = None
        # Actualiza la cabeza de la lista
        self.head = newnode
        
    def PrintList_I_D(self):
        temp = self.head
        while temp:
            print(f"Prev: {temp.prev} Val: {temp.data} Next: {temp.next}")
            temp = temp.next
            
    def PrintList_D_I(self):
        temp = self.head
        #Se llega primero al final
        while temp.next:
            temp = temp.next  
        #Para             
        while temp:
            print(f"Prev: {temp.prev} Val: {temp.data} Next: {temp.next}")
            temp = temp.prev 
            
    def DeleteAllList(self):
        temp = self.head
        if self.head is None:
            return "Empty list"
        
        if self.head.next is None:
            self.head = None
            return
        #Se llega primero al final
        while temp.next.next:
            temp = temp.next  
        #Para     
        while temp:
            print(f"Prev: {temp.prev} Val: {temp.data} Next: {temp.next}")
            temp.next = None
            temp = temp.prev
        self.head=None
        
        '''Recomendacion ia
         while temp:
            temp.prev = None
            temp.next = None
            temp = None
        self.head = None 
        '''
        
            
              
        
        
        
if __name__ == "__main__":
    listaDE = DoubleLinkedList()
    for x in range(10):
        listaDE.AppendBeggin(x)
    # listaDE.PrintList_I_D()
    print()
    # listaDE.PrintList_D_I()
    listaDE.DeleteAllList()
    
    print()
    listaDE.PrintList_I_D()
    