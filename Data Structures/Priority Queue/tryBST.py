from DataStructures import BinarySearchTree

searchPine = BinarySearchTree(10)

searchPine.add(5)
searchPine.add(20)
searchPine.add(3)
searchPine.add(15)

searchPine.printLevelOrderTraversal()

print("Test 0:", searchPine._tree.root.right.key)
print("Test 1:" , searchPine._tree.root.right.left.key)
print("Test 2:", searchPine._tree.root.left.key)
print("Test 3:", searchPine._tree.root.left.left.key)
