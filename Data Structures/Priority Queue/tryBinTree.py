from DataStructures import BinaryTree

pine = BinaryTree(25)
pine.addLeft(20)
pine.addLeft(10, pine.root.left)

for i in range(4):
    pine.addRight(i*50+50 , pine.travelRight(i))

print("Root: ")
print(pine.root.key)

print("Left: ")
for i in range(1, pine.height(pine.root.left)+1):
    print(pine.travelLeft(i).key)
print("Right: ")
for i in range(1,pine.height(pine.root.right)+1):
    print(pine.travelRight(i).key)


print("Height from root:" , pine.height(pine.root))
print("-" * 20)
print("Level order traversal:")

pine.printLevelOrderTraversal()
print("Deep Search:" , pine.deepSearch(10))

for i in range(pine.height(pine.root.left), pine.height(pine.root.left)+4):
    pine.addLeft(i*50+50, pine.travelLeft(i))
    pine.addRight(777, pine.travelLeft(i))

pine.addRight(777, pine.travelLeft(pine.height(pine.root.left)))


print("-" * 20)

print("Level order traversal:")
pine.printLevelOrderTraversal()

#25
#20 50
#10 100
#150 777 150
#200 777 200
#250 777
#300 777
#777

print("-" * 20)
print("Level order traversal from rigth node:")
pine.printLevelOrderTraversal(".key" , pine.root.right)

#50
#100
#150
#200

print("-" * 20)

print("Deepest node:" , pine.deepestNode().key)
print("Size:" , pine.size)

print("-" * 20)


pine.delete(pine.root.right) # Deletes node at the right of the root and puts the local deepest node there
pine.delete() #Deletes tree root and puts the deepest node there

pine.printLevelOrderTraversal(".key", pine.root)

print("New size:", pine.size)

print("Level order traversal after 2 deletions:")

pine.deleteTree()

print("Post delete size:", pine.size)
print("Level order traversal after tree deletion:")
pine.printLevelOrderTraversal(".key", pine.root)
