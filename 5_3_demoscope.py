#local scope & Global scope
def func():
    x=300 #local
    def myinnerfunc():
        print(x)
    myinnerfunc() 
func() #Whole is the global scope-

print("Gobal variables")
x=300
def func():
    print("inside func", x)
func()
print("outside func", x)
print(2+ x)
print(2, x)


def myfun_global(): #have to set different function name if it is in the same file
    global x
    x=300
myfun_global()
print(x)







