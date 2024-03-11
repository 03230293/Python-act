# Create a variable with an integer value 
x = 10
# Get the memory address of x and store it in ptr
ptr = id(x) 
# Print the memory address 
print(ptr)
# Change the value of x
x = 15
# Print the memory address again
print(id(x))