x="Hello Woreld" #str
x=50 #int
x=60.5 #float
x=3j #complex
x=["geeks", 'for', "geeks"] #list
x=("geeks", 'for', "geeks") 
x=range(10)
x={"name": "Suraj", "age": 24}
x={"geeks", 'for', "geeks"}
x=frozenset({"geeks", 'for', "geeks"})
x=True
x=b"Geeks"
x=bytearray (4)
x=memoryview(bytes(6))
x=None

#Arrays can defined as lists in python

#operationon list -insert, append, length, remove, pop

my_list=[1,2,3,4,5, "som"] #array can store only one type of data but list can store all the types.
my_list.insert(1,0) #index of the list / add new variables 0 is the indexand 1 is the value
print (my_list)

my_list.append(5) #stacks and queques 
print (my_list)

#my_list.(5) # used in stacks and queques 
print (len(my_list)) 

my_list.remove(0) #removes the value of index (o==index) / remove"som"
my_list.remove(my_list[0])
print (my_list)

my_list.pop() #removes the last element 
print (my_list)

