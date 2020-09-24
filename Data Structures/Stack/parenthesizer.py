from DataStructures import Stack

par = { ")":"(", "}":"{", "]":"["}
state = True
stack = Stack()
print("Enter a text to check wether it is or not correctly parenthesized.")
texto = input("Enter a text : ")

for i in texto:
    if i in par.values():
        stack.push(i)
        continue
    elif i in par.keys():
        if not stack.isEmpty() and par[i] == stack.peek():
            stack.pop()
            continue
        else:
            state = False
            break

if stack.isEmpty() and state == True:
    print("VALID")
else:
    print("NOT VALID")


