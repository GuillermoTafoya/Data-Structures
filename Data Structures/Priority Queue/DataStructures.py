# https://github.com/GuillermoTafoya
# My objective is to create my own library for data structures 
# in python and make an example of a practical use for each type.
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
            if pointer is self.head:
                self.deleteFirst()
            elif pointer is self.tail:
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

    def contains(self, element, arg=""):
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
            if pointer is self.head:
                self.deleteFirst()
            elif pointer is self.tail:
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

    def contains(self, looking, arg=""):
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

    def contains(self, element, arg=""):
        return self._methods.contains(element, arg)

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

    def empty(self):
        self._methods.deleteList()
        self.size = self._methods.size

class Queue():
    def __init__(self):
        self._methods = SinglyLinkedList()
        self.size = self._methods.size

    def isEmpty(self):
        return self._methods.isEmpty()

    def contains(self, element, arg=""):
        return self._methods.contains(element, arg)

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

    def empty(self):
        self._methods.deleteList()
        self.size = self._methods.size

class BinaryTree():

    class node:
        def __init__(nodeSelf, Key, Data = None, Left = None, Right = None, Prev = None):
            nodeSelf.key = Key
            nodeSelf.data = Data
            nodeSelf.left = Left
            nodeSelf.right = Right
            nodeSelf.prev = Prev

    def __init__(self, Key, Data = None):
        self.size = 1
        self.root = self.node(Key, Data)
        self._methods = Queue()

    def addRoot(self, Key, Data = None):
        if self.root is None:
            self.root = self.node(Key, Data)
            self.size += 1
        else: 
            return False

    def isEmpty(self):
        return self.size == 0

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

    def addLeft(self, Key, node = None, Data = None):
        """
        Adds a node to the left of the specified node.
        The default node is the tree's root
        Returns false if the specified node already has a left node.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                addRoot(Key, Data)
                return
        else:
            pointer = node
        
        if pointer.left is None:
            pointer.left = self.node(Key, Data)
            pointer.left.prev = pointer
            pointer = None
            gc.collect()
            self.size += 1
        else:
            return False

    def travelLeft(self, iterator = 1, node = None):
        """
        Returns a node n times to the left of the specified node.
        The default node is the tree's root.
        Returns False if there aro not enough nodes to travel.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                return False
        else:
            pointer = node

        for i in range(iterator):
            if pointer.left is not None:
                pointer = pointer.left
            else:
                return False
        return pointer

    def travelAllLeft(self, node = None):
        """
        Returns the node that is to the most left of the specified node.
        The default node is the tree's root.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                return False
        else:
            pointer = node
        
        while pointer.left is not None:
            pointer = pointer.left
        return pointer

    def addRight(self, Key, node=None, Data=None):
        """
        Adds a node to the right of the specified node.
        The default node is the tree's root
        Returns false if the specified node already has a right node.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                addRoot(Key, Data)
                return
        else:
            pointer = node

        if pointer.right is None:
            pointer.right = self.node(Key, Data)
            pointer.right.prev = pointer
            pointer = None
            gc.collect()
            self.size += 1
        else:
            return False

    def travelRight(self, iterator=1, node=None):
        """
        Returns a node n times to the right of the specified node.
        The default node is the tree's root.
        Returns False if there aro not enough nodes to travel.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                return False
        else:
            pointer = node

        for i in range(iterator):
            if pointer.right is not None:
                pointer = pointer.right
            else:
                return False
        return pointer

    def travelAllRight(self, node=None):
        """
        Returns the node that is to the most right of the specified node.
        The default node is the tree's root.
        """
        if node is None:
            pointer = self.root
            if pointer is None:
                return False
        else:
            pointer = node

        while pointer.right is not None:
            pointer = pointer.right
        return pointer

    def printLevelOrderTraversal(self, arg = ".key", node = None):
        """
        The method will print all nodes (taking a specified node as the root) in level order.
        The default node is the tree's root.
        The default argument to print is the key, but another can be specified as a string (for example ".data.name").
        """
        self._methods.empty()

        if node is None:
            if self.root is not None:
                self._methods.add(self.root)
            else:
                return False
        else:
            self._methods.add(node)

        level = Queue()
        levelTracker = 1
        levelRequirements = 1
        level.add(self._methods.peek())

        while not self._methods.isEmpty():
            
            #Print Level
            if levelRequirements == levelTracker:
                levelRequirements = 0
                for i in range(levelTracker):
                    print(eval("level.peek()" + arg), end = " ")
                
    
                    if level.peek().left is not None:
                        levelRequirements += 1
                        level.add(level.peek().left)

                    if level.peek().right is not None:
                        levelRequirements += 1
                        level.add(level.peek().right)
                    
                    level.poll()
                    gc.collect()
                levelTracker = 0
                print("")

            if self._methods.peek().left is not None:
                self._methods.add(self._methods.peek().left)
            if self._methods.peek().right is not None:
                self._methods.add(self._methods.peek().right)
            self._methods.poll()
            levelTracker += 1

    def getLevel(self, Level = 0, node = None):
        """
        The method will return all nodes (from left to rigth) in a level as a tupple (taking a specified node as the root).
        The default node is the tree's root.
        The default level, that is also the root level, is 0.
        Returns false if the specified level does not exist.
        """
        self._methods.empty()

        if node is None:
            if self.root is not None:
                self._methods.add(self.root)
            else:
                return False
        else:
            self._methods.add(node)

        level = Queue()
        levelTracker = 1
        levelRequirements = 1
        level.add(self._methods.peek())
        currentLevel = 0
        while not self._methods.isEmpty():

            #Level
            if levelRequirements == levelTracker:
                
                levelRequirements = 0
                #Get rid of previous level while getting the new one.
                for i in range(levelTracker):

                    if level.peek().left is not None:
                        levelRequirements += 1
                        level.add(level.peek().left)

                    if level.peek().right is not None:
                        levelRequirements += 1
                        level.add(level.peek().right)

                    level.poll()

                currentLevel += 1

                if currentLevel == Level:
                    gc.collect()
                    return level
                levelTracker = 0

            if self._methods.peek().left is not None:
                self._methods.add(self._methods.peek().left)
            if self._methods.peek().right is not None:
                self._methods.add(self._methods.peek().right)
            self._methods.poll()
            levelTracker += 1
        return False

    def deepSearch(self, element, arg = ".key", node = None):
        """
        The method will search for a given element in all nodes (taking a specified node as the root) and return the node (or False if it's not contained).
        The default node is the tree's root.
        The default argument is the key, but another can be specified as a string (for example ".data.name").
        Returns false if the specified level does not exist.
        """
        self._methods.empty()

        if node is None:
            if self.root is not None:
                self._methods.add(self.root)
            else:
                return False
        else:
            self._methods.add(node)

        while not self._methods.isEmpty():

            if self._methods.peek().left is not None:
                self._methods.add(self._methods.peek().left)

            if self._methods.peek().right is not None:
                self._methods.add(self._methods.peek().right)

            if eval("self._methods.peek()" + arg) == element:
                return self._methods.poll()
            self._methods.poll()

        return False

    def deepestNode(self, Node = None):
        """
        The method will search for the deepest of all nodes (taking a specified node as the root) and return the node.
        The default node is the tree's root.
        """
        self._methods.empty()

        if Node is None:
            if self.root is not None:
                self._methods.add(self.root)
            else:
                return False
        else:
            self._methods.add(Node)

        while not self._methods.isEmpty():

            pointer = self._methods.peek()

            if self._methods.peek().left is not None:
                self._methods.add(self._methods.peek().left)

            if self._methods.peek().right is not None:
                self._methods.add(self._methods.peek().right)

            if self._methods.size > 1:
                self._methods.poll()
            else:
                return self._methods.poll()

    def delete(self, Node = None):
        """
        The method will delete the specified node and replace it with the deepest node.
        If one of the deepest node is being deleted, it is not replaced with anything.
        The default node is the tree's root.
        """
        
        if Node is None:
            if self.root is not None:
                node = self.root
            else: 
                return False
        else:
            node = Node

        if self.size == 1:
            self.root = None
            gc.collect()
            self.size -= 1
            return

        pointer = self.deepestNode(node)
        node.key = pointer.key
        node.data = pointer.data
        
        if pointer.prev.right is pointer:
            pointer.prev.right = None
        else:
            pointer.prev.left = None
        pointer = None
        self.size -= 1
        gc.collect()

    def deleteTree(self):
            """
            Deletes the tree.
            """
            if self.isEmpty():
                return

            self._methods.empty()

            self._methods.add(self.root)

            while not self._methods.isEmpty():

                if self._methods.peek().left is not None:
                    self._methods.add(self._methods.peek().left)

                if self._methods.peek().right is not None:
                    self._methods.add(self._methods.peek().right)

                pointer = self._methods.poll()

                if pointer is self.root:
                    continue
                elif pointer.prev.right is pointer:
                    pointer.prev.right = None
                else:
                    pointer.prev.left = None
                gc.collect()

            self.root = None
            self.size = 0
            pointer = None
            gc.collect()
            return

class BinarySearchTree():
    def __init__(self, Key, Data = None):
        self._tree = BinaryTree(Key, Data)
        self.size = self._tree.size
        self.root = self._tree.root

    def addRoot(self, Key, Data = None):
        self._tree.addRoot(Key, Data)
        self.size = self._tree.size
        self.root = self._tree.root

    def add(self, Key, Data = None, _Node = None):
        """
        Adds a not in the correct position given a priority key.
        Returns False if there is already a key with that value.
        """
        if self.size == 0:
            self.addRoot(Key, Data)
            return

        if _Node is None:
            pointer = self._tree.root

        while True:

            if Key < pointer.key:
                if pointer.left is None:
                    self._tree.addLeft(Key, pointer, Data)
                    self.size = self._tree.size
                    return
                else:
                    pointer = pointer.left
            elif Key > pointer.key:
                if pointer.right is None:
                    self._tree.addRight(Key, pointer, Data)
                    self.size = self._tree.size
                    return
                else:
                    pointer = pointer.right
            else:
                return False

    def printLevelOrderTraversal(self):
        self._tree.printLevelOrderTraversal()

    def search(self, Key):
        """
        Performs binary search with a given key.
        Returns false if the key is not in the tree.
        """
        pointer = self.root
        while True:
            if Key == pointer.key:
                return pointer
            elif Key <= pointer.key:
                if pointer.left is None:
                    return False
                pointer = pointer.left
            else:
                if pointer.right is None:
                    return False
                pointer = pointer.right
        return False


"""
class PriorityQueue():
    def __init__(self):
        self._methods = SinglyLinkedList()
        self.size = self._methods.size

    def isEmpty(self):
        return self._methods.isEmpty()

    def contains(self, element, arg=""):
        return self._methods.contains(element, arg)

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
"""
