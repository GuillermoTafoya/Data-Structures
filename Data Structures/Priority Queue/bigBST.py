import random
from DataStructures import BinarySearchTree

hugeOak = BinarySearchTree(random.randint(0, 100))

for i in range(2000):
    hugeOak.add(random.randint(0, 1000))

hugeOak.printLevelOrderTraversal()

print("Size:" , hugeOak.size)

print("Outer Left: ")

print(hugeOak.travelAllLeft().key)

print("Outer Right: ")

print(hugeOak.travelAllRight().key)
