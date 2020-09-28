from DataStructures import BinarySearchTree

searchPine = BinarySearchTree(10)

searchPine.add(5)
searchPine.add(20)
searchPine.add(3)
searchPine.add(15)

print("Dup:" , searchPine.add(15))
searchPine.printLevelOrderTraversal()

print("Root:" , searchPine.root.key)
print("Test 0:", searchPine.root.right.key)
print("Test 1:" , searchPine.root.right.left.key)
print("Test 2:", searchPine.root.left.key)
print("Test 3:", searchPine.root.left.left.key)

print("Binary search:", searchPine.search(15).key)
print("Size:" , searchPine.size)
