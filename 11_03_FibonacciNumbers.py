def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2) #This will run / can't be neg
n = 10
print("Fibonacci sequence:")
for i in range(n): #run 10 times starts from fib 0
    print(fib(i))
    print(i)

  