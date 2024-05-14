#Read mode

# f= open("hello.txt", "r")
# for i in f:
#     print(i)
# # text=f.read()
# # print(text)
# line1=f.readlines()
# print(line1)
# line2=f.readlines()
# print(line2)

# text=f.readlines()
# print(text)
# hello.txt 
 
#Write mode
# f= open("newfile.txt", "w")
# f.write("Hello")
# f.write("Good Morning\nThis is some dummy text\nGood Bye")
# # text=f.read()
# # print(text)
# f.close() #close the file, f variable will have not content

#Append mode
# f= open("newfile.txt", "a")
# f.write("Python is the best language\nPython is easy")
# f.close() 
 
#Delete the file 
import os
os.remove("hello.txt")

