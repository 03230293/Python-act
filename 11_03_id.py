from ctypes import c_int, addressof 

 
a =1
print(id(a)) 

# # get id of a variable 
# a = 12
# print(id(a)) 

# # get id of tuple 
# a = (1, 2, 3, 4, 5) 
# print(id(a)) 

# # get id of a dictionary 
# a = {'a': 1, 'b': 2} 
# print(id(a)) 

# import addressof and c_int modules 
# from ctypes module 

# get memory address of variable

print(addressof(c_int(a))) 
