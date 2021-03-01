from node import Node

class Linkedlist:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        if self.head:
            #adicionando quando a lista já tem elemento
            pointer = self.head
            
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #Adicionando primeiro elemento na lista
            self.head = Node(elem)
        self._size += 1
    
    def __len__(self):
        #Retornando o tamanho da lista
        return self._size
    
    def get(self, index):
        pass
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")
  
    def set(self, index, elem):
        pass
   
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range") 
    
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            else:
                pointer = pointer.next
                i += 1
        raise ValueError("Elemento não Encontrado.")
"""
Test area
"""

"""
from linkedlist import Linkedlist
lista = Linkedlist()

"""