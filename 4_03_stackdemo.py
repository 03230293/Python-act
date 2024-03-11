#stack is just a list
 #removed the last element
#make a list stack by pop, append, follow last in first out, 
#complexity O(n)

stack=[]
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack")
print(stack)

print(stack.pop()) #appears the element that removed 
print(stack.pop()) 

