x = float(input('Enter first number '))
y = float(input('Enter second number '))
output = 0
operation = input('Enter operations: add, subtract, multiply, divide, power,ceiling ')

if operation == 'add':
    output = x + y
    print('product:',output)
elif operation == 'subtract':
    output = x - y
    print('product:', output)
elif operation == 'multiply':
    output = x * y
    print('product:', output)
elif operation == 'divide':
    output = x / y
    print('product:', output)
elif operation == 'power':
    output = x ** y
    print('product:', output)   
elif operation == 'ceiling':
    output = x // y
    print('product:', output)
else: 
    print('Invalid operation')