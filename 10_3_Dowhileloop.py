# defining list of strings 
list1 = ["geeksforgeeks", "C++", 
		"Java", "Python", "C", "MachineLearning"] 

# initialises a variable 
i = 0

print("Printing list items\ using while loop") 
size = len(list1) 
print(size)
#Implement while loop to print list items 

while(i < size): 
	print(list1[i]) 
	i = i+1

i = 0

print("Printing list items\ using do while loop") 

# Implement do while loop to print list items 
while(True): 
	print(list1[i]) 
	i = i+1
	if(i < size and len(list1[i]) < 10): 
		continue
	else: 
		break

print("In python 3 ")
total = 0
# loop will run at least once 
while True: 
	# ask the user to enter a number 
	num = int(input("Enter a number (or 0 to exit): ")) 

	# exit the loop if the user enters 0 
	if num == 0: 
		break
	total += num 

# print the total 
print("Total:", total) 
