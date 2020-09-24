from LinkedLists import DoublyLinkedList
#import DoublyLinkedList

class Book:
    def __init__(self, Title, Author, Date):
        self.description = {
            "title" : Title,
            "author" : Author,
            "date" : Date
        }
    def printDescription(self):
        for atrr, value in self.description.items():
            print(f"{atrr}: {value}")



iBooks = DoublyLinkedList()

iBooks.add("This is the title and is not an object.")
iBooks.add(HarryPotter := Book("Harry Potter", "J. K. Rowling", 1997))
iBooks.add(LordOfTheRings := Book("Lord of the Rings", "J. R. R. Tolkien", 1954))
iBooks.add(DonQuijote := Book("Don Quijote", "Miguel de Cervantes", 1605))

iBooks.clearList()

print("-"*20)

# Prints the data cointained in each node of the list with a numerator on the side.

iBooks.printList()

print("-"*20)

# Search: returns the node. The arguments include the item to search for 
# and optionally the attribute of the object you expect to find as a string

print(iBooks.search("Harry Potter", '.description["title"]'))

# Index. returns the index. The arguments include the item to search for 
# and optionally the attribute of the object you expect to find as a string

print(iBooks.index("Harry Potter", '.description["title"]'))

# Index. returns wheter what you searched for exists or not whith a boolean. 
# The arguments include the item to search for and optionally the attribute
# of the object you expect to find as a string

print(iBooks.exists("Harry Potter", '.description["title"]'))

print("-"*20)

print(iBooks.search("Harry Potter", '.description["title"]').data.description["title"])
print(iBooks.search("Harry Potter",'.description["title"]').data.description["author"])

print("-"*20)

iBooks.search("Harry Potter", '.description["title"]').data.printDescription()

print("-"*20)

print("iBooks size:" , iBooks.size)

print("-"*20)

print(iBooks.head)

print("-"*20)

# Nodes in a doubly linked list can be accessed from the tail or from the head

iBooks.get(-2).printDescription()

print("-"*20)

"""
while True:
    x = input()
    if x.lower() == "next":
        if iBooks.size > iBooks.index(currentNode.data.description["title"], '.description["title"]')+1:
            currentNode = currentNode.next
            index = iBooks.index(
                currentNode.data.description["title"], '.description["title"]')
            print(f"Current Node: {index}")
        else:
            print("You are currently in the tail.")
    elif x.lower() == "prev":
        if iBooks.index(currentNode.data.description["title"], '.description["title"]') != 0:
            currentNode = currentNode.prev
            index = iBooks.index(
                currentNode.data.description["title"], '.description["title"]')
            print(f"Current Node: {index}")
        else:
            print("You are currently in the head.")
    elif x.lower() == "index":
        index = iBooks.index(
            currentNode.data.description["title"], '.description["title"]')
        print(f"Current Node: {index}")
    elif x.lower() == "print":
        print("-"*20)
        currentNode.data.printDescription()
    elif x.lower() == "print all":
        for i in range(iBooks.size):
            print("-"*20)
            iBooks.get(i).printDescription()
    elif x.lower() == "exit":
        break
"""

#iBooks.search("Harry Potter", '.description["title"]').data.printDescription()

currentNode = iBooks.head
index = 0
while True:
    x = input()
    if x.lower() == "next":
        if iBooks.size > index + 1:
            currentNode = currentNode.next
            index += 1
            print(f"Current Node: {index}")
        else:
            print("You are currently in the tail.")
    elif x.lower() == "prev":
        if index != 0:
            currentNode = currentNode.prev
            index -= 1
            print(f"Current Node: {index}")
        else:
            print("You are currently in the head.")
    elif x.lower() == "index":
        print(f"Current Node: {index}")
    elif x.lower() == "print":
        print("-"*20)
        try:
            currentNode.data.printDescription()
        except:
            print(currentNode.data)
    elif x.lower() == "print all":
        for i in range(iBooks.size):
            print("-"*20)
            try:
                iBooks.get(i).printDescription()
            except:
                print(iBooks.get(i))
    elif x.lower() == "exit":
        break
    else:
        try:
            eval(x)
            currentNode = iBooks.getNode(index)
        except:
            continue

