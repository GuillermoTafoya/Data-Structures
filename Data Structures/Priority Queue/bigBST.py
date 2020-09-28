import random
from DataStructures import BinarySearchTree

hugeOak = BinarySearchTree(random.randint(0, 100))

for i in range(2000):
    hugeOak.add(random.randint(0, 1000))

hugeOak.printLevelOrderTraversal()

print("Size:" , hugeOak.size)

print("Outer Left: ")
for i in range(1, hugeOak.height(hugeOak.root.left)+1):
    print(hugeOak.travelLeft(i).key)
print("Outer Right: ")
for i in range(1, hugeOak.height(hugeOak.root.right)+1):
    print(hugeOak.travelRight(i).key)
