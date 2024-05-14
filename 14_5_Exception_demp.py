try:
    a= 18
    b=0
    c=b/a
    print(c)

except ZeroDivisionError:
    print("Can't divide by zero")

except NameError:
    print("Sonam variable isn't defined")

except:
    print("Some error has occured")

# print("This is another statement")
else:
    print("Everythhing worked fine")
finally:
    print("This is finnaly statement")

