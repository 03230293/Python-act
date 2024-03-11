fruits= ["apple", "banana", "cherry"]
for x in fruits:
    print (x)

for x in "banana":
    print(x)

#the break statement- stops the loop when the condition is made
print("It is break statement below")
fruits= ["apple", "banana", "cherry"]
for x in fruits:
    print (x)
    if x == "banana":
        break

#Continue statement
print("Continue statement topic")
fruits= ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana": #goes back to the loop - it goes to apple and bcherry
        continue
    print (x)

#RAnge function
print("Range function")
for c in range (6): #print till 5 starting from 0
    print(c)
print("Start")
for c in range(2,6): #2-5
    print(c)

print("increment sequence")
for c in range(2,30,3): #keeps on adding 3 till it reaches to 30
    print(c)

#else statement
print("Else statement")
for i in range(6):
    print(i)
else:
    print("Finally finished!")

