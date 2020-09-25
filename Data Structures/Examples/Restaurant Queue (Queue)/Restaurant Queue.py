from DataStructures import Queue

a = Queue()

personas = {'Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 
'Ava', 'William', 'Sophia', 'Elijah', 'Isabella',
'James', 'Charlotte', 'Benjamin', 'Amelia', 'Lucas', 'Mia', 
'Mason', 'Harper', 'Ethan', 'Evelyn'}

for i in personas:
    a.enqueue(i)

print("Current waiting queue:")
a.printList()

for i in range(5):
    print(f"It is {a.poll()}'s turn")

a.printList()
