from node import Node

# sequencial = []

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem): #function to add element
        if self.head:
            # inserTion if list have elements
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            else:
                pointer.next = Node(elem)
        else:
            # first inserTion
            self.head = Node(elem)
        self._size = self._size + 1
    def __len__(self):
        return self._size

    def get(self, index):
        pass
   
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('List index out of range')
        if pointer:
            return pointer.data
        else:  raise IndexError('List index out range')

    def set(self):
        pass

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(pointer):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('List index out of range')
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('List index out range')
    
    def index(self, elem):
        pointer = self.head
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        return ValueError(f'{elem} is not in list ')

lista = LinkedList()


"""
from linkedList import LinkedList
lista = LinkedList()
lista.append(1)
lista.append(22)
lista.append(33)

"""