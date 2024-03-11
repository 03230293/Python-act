#Loop inside a loop
adj=["red", "big", "taste"] # 3 elements in this list
fruits= ["apple", "banana", "cherry"] # 3 elements in this list

for i in adj:
    print("fruits") #executes 3 times
    for x in fruits:
        print(i, x) #print statement is executed 3*3=9 times

#pass stamenet
for x in [0,1,2]:
    pass
    