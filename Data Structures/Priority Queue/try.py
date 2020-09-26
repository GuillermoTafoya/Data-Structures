from DataStructures import binTree

pine = binTree(25)
pine.addLeft(20)
pine.addLeft(10, pine.root.left)

for i in range(4):
    pine.addRight(i*50+50 , pine.travelRight(i))


print("Root: ")
print(pine.root.data)

print("Left: ")
for i in range(1, pine.height(pine.root.left)+1):
    print(pine.travelLeft(i).data)
print("Right: ")
for i in range(1,pine.height(pine.root.right)+1):
    print(pine.travelRight(i).data)


print(pine.height(pine.root))
print("-" * 20)
print("Level order traversal:")

pine.printLevelOrder(pine.root)




