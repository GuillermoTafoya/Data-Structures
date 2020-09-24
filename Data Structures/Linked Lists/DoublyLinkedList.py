import gc


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
        """
        Deletes the content of all the nodes in the list.
        """
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
            print("Exception: current list has 0 nodes.")

    def deleteLast(self):
        if not self.isEmpty():
            self.tail.prev.next = self.tail.prev
            gc.collect()
            self.size -= 1
        else:
            print("Exception: current list has 0 nodes.")

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
            print("Exception: current list has 0 nodes.")

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
        elif iteration > self.size:
            print("Exception: current DoublyLinkedList has not valid iterable node.")
        else:
            self.deleteAt(iteration, Data)

    def printList(self, arg=""):
        if self.size > 0:
            pointer = self.head
            for i in range(self.size):
                print(i, eval("pointer.data" + arg))
                pointer = pointer.next
        else:
            print("Exception: current list has 0 nodes.")

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
                    print(
                        "Exception: current DoublyLinkedList has not valid iterable node.")
        else:
            print("Exception: current list has 0 nodes.")

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None, None)
        else:
            self.head.prev = self.node(Data, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def addLast(self, Data=None):
        if self.isEmpty():
            self.head = self.tail = self.node(Data, None, None)
        else:
            self.tail.next = self.node(Data, self.tail, None)
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
        elif iteration >= self.size:
            print("Exception: current DoublyLinkedList has not valid iterable node.")
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
            print("Exception: invalid node.")

    def getNode(self, i):
        if self.size > abs(i):
            return self.iterate(i)
        else:
            print("Exception: invalid node.")

    def getData(self, i):
        if self.size > abs(i):
            return self.iterate(i).data
        else:
            print("Exception: invalid node.")
