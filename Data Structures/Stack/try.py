from DataStructures import Stack

cards = Stack()

cards.push("10")
cards.push("K")
cards.push("J")
cards.push("11")
cards.push("A")

cards.printList()
print("-" * 20)
print("Deleted:" , cards.pop())
print("Deleted:", cards.pop())
cards.printList()
print("Size:" , cards.size)

