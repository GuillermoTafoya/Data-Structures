# https://github.com/GuillermoTafoya
# My objective is to create my own library for data structures 
# in python and make n example of a practical use for each type.
import gc

class SinglyLinkedList:

    class node:
        def __init__(nodeSelf, Data, Next):
            nodeSelf.next = Next
            nodeSelf.data = Data

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        """
        Deletes the content of all nodes in the list.
        """
        pointer = self.head
        while pointer != None:
            pointer.data = None
            pointer = pointer.next

    def deleteList(self):
        """
        Deletes all nodes in the list.
        """
        while self.head != None:
            self.head = self.head.next
        self.size = 0
        gc.collect()

    def deleteFirst(self):
        """
        Deletes the head and returns the data contained.
        Returns False if the list is empty.
        """
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            gc.collect()
            return data
        else:
            return False

    def deleteLast(self):
        """
        Deletes the tail and returns the data contained.
        Returns False if the list is empty.
        """
        if not self.isEmpty():
            if self.size == 1:
                self.deleteFirst()
            else:
                data = self.head.data
                self.tail = self.getNode(self.size-2)
                self.size -= 1
                gc.collect()
                return data
        else:
            return False

    def deleteAt(self, i=None):
        """
        Deletes the node specified and returns the data contained.
        Returns False if node doesn't exists.
        """
        if i is None:
            i = int(self.size-1)
        else:
            i = int(i)
        if not self.isEmpty():
            if i == self.size:
                self.deleteLast()
            elif i == 0:
                self.deleteFirst()
            else:
                data = self.get(i)
                pointer = self.getNode(i)
                pointerPrev = self.getNode(i-1)
                pointerPrev.next = pointer.next
                pointer = None
                self.size -= 1
                gc.collect()
                return data
        else:
            return False

    def searchDel(self, element="", arg=""):
        """
        Searches for an element in the nodes of the list, deletes the node and
        returns the data contained.
        If the node contains an object, you can search in its attributes using a string
        in the args: arg = '.name'
        Returns False if node doesn't exists.
        """
        pointer = self.search(element, arg)
        if pointer is not False:
            if pointer == self.head:
                self.deleteFirst()
            elif pointer == self.tail:
                self.deleteLast()
            else:
                data = pointer.data
                pointerPrev = self.getNode(self.index(element, arg)-1)
                pointerPrev.next = pointer.next
                pointer = None
                self.size -= 1
                return data
        else:
            return False

    def delete(self, Data=None, iteration=None, element=""):
        """
        Searches for an element in the nodes of the list, deletes the node and
        returns the data contained.
        """
        arg = None
        if iteration is None:
            iteration = int(self.size)
        elif type(iteration) == type("string"):
            arg = iteration
        else:
            iteration = int(iteration)
        if arg is not None:
            self.searchDel(arg)
        elif iteration == self.size:
            self.deleteLast(Data)
        elif iteration == 0:
            self.deleteFirst(Data)
        elif iteration > self.size:
            return False
        else:
            self.deleteAt(iteration, Data)

    def printList(self, arg=""):
        if self.size > 0:
            pointer = self.head
            for i in range(self.size):
                print(i, eval("pointer.data" + arg))
                pointer = pointer.next
        else:
            return False

    def iterate(self, iteration):
        if not self.isEmpty():
            if iteration >= 0:
                pointer = self.head
                for i in range(iteration):
                    pointer = pointer.next
                return pointer
            else:
                return False
        else:
            return False

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None)
        else:
            self.head = self.node(Data, self.head)
        self.size += 1

    def addLast(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None)
        else:
            self.tail.next = self.node(Data, None)
            self.tail = self.tail.next
        self.size += 1

    def addAt(self, trav=None, Data=None):
        if trav is None:
            trav = int(self.size-1)
        
        if trav == 0:
            self.addFirst(Data)
        elif trav == self.size-1:
            self.addLast(Data)
        else:
            newNode = self.node(Data, self.iterate(trav))
            self.iterate(trav-1).next = newNode
            self.size += 1

    def add(self, Data=None, iteration=None):
        if iteration is None:
            iteration = int(self.size-1)
        else:
            iteration = int(iteration)
        
        if iteration == self.size-1:
            self.addLast(Data)
        elif iteration == 0:
            self.addFirst(Data)
        elif iteration >= self.size:
            return False
        else:
            self.addAt(iteration, Data)

    def exists(self, element, arg=""):
        """
        Searches for an element in the nodes and returns wheter the node
        exists or not in the args: (element, arg = '.name')\n
        Returns False if node doesn't exists.
        """
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == element:
                    return True
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def search(self, element, arg=""):
        """
        Searches for an element in the nodes of the list and returns the node.
        If the node contains an object, you can search in its attributes using a string
        in the args: (element, arg = '.name')\n
        Returns False if node doesn't exists.
        """
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == element:
                    return trav
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def index(self, element, arg=""):
        """
        Searches for an element in the nodes of the list and returns the index
        where the node was found.
        If the node contains an object, you can search in its attributes using a string
        in the args: (element, arg = '.name')\n
        Returns False if node doesn't exists.
        """
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == element:
                    return i
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def get(self, i):
        """
        Returns the data of the specified index node.
        Returns False if the list is empty or the node doesn't exists.
        """
        if self.size > abs(i):
            return self.getData(i)
        else:
            return False

    def getNode(self, i):
        """
        Returns the node of the specified index.
        Returns False if the list is empty or the node doesn't exists.
        """
        if self.size > abs(i):
            return self.iterate(i)
        else:
            return False

    def getData(self, i):
        """
        Returns the data of the specified index node.
        Returns False if the list is empty or the node doesn't exists.
        """
        if self.size > abs(i):
            return self.iterate(i).data
        else:
            return False

class DoublyLinkedList:

    class node:
        def __init__(nodeSelf, Data, Prev, Next):
            nodeSelf.prev = Prev
            nodeSelf.next = Next
            nodeSelf.data = Data

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clearList(self):
        pointer = self.head
        while pointer != None:
            pointer.data = None
            pointer = pointer.next

    def deleteList(self):
        while self.head != None:
            self.head = self.head.next
        self.size = 0
        gc.collect()

    def deleteFirst(self):
        if not self.isEmpty():
            pointer = self.head
            self.head = pointer.next
            pointer = None
            gc.collect()
            self.size -= 1
        else:
            return False

    def deleteLast(self):
        if not self.isEmpty():
            self.tail.prev.next = self.tail.prev
            gc.collect()
            self.size -= 1
        else:
            return False

    def deleteAt(self, i=None):
        if i is None:
            i = int(self.size-1)
        else:
            i = int(i)
        if not self.isEmpty():
            if i == self.size-1:
                self.deleteLast()
            elif i == 0:
                self.deleteFirst()
            else:
                pointer = self.getNode(i)
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                pointer = None
                gc.collect()
                self.size -= 1
        else:
            return False

    def searchDel(self, arg="", element=""):
        pointer = self.search(element, arg)
        if pointer is not False:
            if pointer == self.head:
                self.deleteFirst()
            elif pointer == self.tail:
                self.deleteLast()
            else:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                pointer = None
                self.size -= 1
        else:
            return False

    def delete(self, Data=None, iteration=None, element=""):
        arg = None
        if iteration is None:
            iteration = int(self.size-1)
        elif type(iteration) == type("string"):
            arg = iteration
        else:
            iteration = int(iteration)
        if arg is not None:
            self.searchDel(arg)
        elif iteration == self.size-1:
            self.deleteLast(Data)
        elif iteration == 0:
            self.deleteFirst(Data)
        else:
            self.deleteAt(iteration, Data)

    def printList(self, arg=""):
        if self.size > 0:
            pointer = self.head
            for i in range(self.size):
                print(i, eval("pointer.data" + arg))
                pointer = pointer.next
        else:
            return False

    def iterate(self, iteration):
        if not self.isEmpty():
            if iteration >= 0:
                pointer = self.head
                for i in range(iteration):
                    pointer = pointer.next
                return pointer
            else:
                try:
                    pointer = self.tail
                    for i in range(iteration*-1-1):
                        pointer = pointer.prev
                    return pointer
                except:
                    return False
        else:
            return False

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None, None)
        else:
            self.head.prev = self.node(Data, self.tail, self.head)
            self.head = self.head.prev
        self.size += 1

    def addLast(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None, None)
        else:
            self.tail.next = self.node(Data, self.tail, self.head)
            self.tail = self.tail.next
        self.size += 1

    def addAt(self, trav=None, Data=None):
        if trav is None:
            trav = int(self.size-1)
        if trav == 0:
            self.addFirst(Data)
        elif trav == self.size-1:
            self.addLast(Data)
        else:
            newNode = self.node(Data, self.iterate(
                trav).prev, self.iterate(trav-1).next)
            self.iterate(trav).prev = newNode
            self.iterate(trav-1).next = newNode
            self.size += 1

    def add(self, Data=None, iteration=None):
        if iteration is None:
            iteration = int(self.size-1)
        else:
            iteration = int(iteration)
        if iteration == self.size-1:
            self.addLast(Data)
        elif iteration == 0:
            self.addFirst(Data)
        else:
            self.addAt(iteration, Data)

    def exists(self, looking, arg=""):
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == looking:
                    return True
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def search(self, looking, arg=""):
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == looking:
                    return trav
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def index(self, looking, arg=""):
        trav = self.head
        for i in range(self.size):
            try:
                if eval("trav.data" + arg) == looking:
                    return i
            except:
                trav = trav.next
                continue
            trav = trav.next
        return False

    def get(self, i):
        if self.size > abs(i):
            return self.getData(i)
        else:
            return False

    def getNode(self, i):
        if self.size > abs(i):
            return self.iterate(i)
        else:
            return False

    def getData(self, i):
        if self.size > abs(i):
            return self.iterate(i).data
        else:
            return False

class Stack():
    def __init__(self):
        self._methods = SinglyLinkedList()
        self.size = self._methods.size

    def isEmpty(self):
        return self._methods.isEmpty()

    def printList(self, arg = ""):
        self._methods.printList(arg)

    def push(self, data):
        self._methods.addFirst(data)
        self.size = self._methods.size

    def pop(self):
        pointer = self._methods.head.data
        self._methods.deleteFirst()
        self.size = self._methods.size
        return pointer

    def peek(self):
        return self._methods.head.data

class Queue():
    def __init__(self):
        self._methods = SinglyLinkedList()
        self.size = self._methods.size

    def isEmpty(self):
        return self._methods.isEmpty()

    def printList(self, arg=""):
        self._methods.printList(arg)

    def enqueue(self, data):
        self._methods.addLast(data)
        self.size = self._methods.size

    def dequeue(self):
        pointer = self._methods.head.data
        self._methods.deleteFirst()
        self.size = self._methods.size
        return pointer

    def add(self, data):
        self.enqueue(data)

    def poll(self):
        return self.dequeue()

    def peek(self):
        return self._methods.head.data
