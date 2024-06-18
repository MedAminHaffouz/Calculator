def derivative(f, x):
    h = 1e-10
    return (f(x + h) - f(x)) / h

# get user input for function
f_str = input("Enter a function in terms of x: ")

# define the symbols to use
symbols = {'x': x, 'sin': sin, 'cos': cos, 'tan': tan, 'log': log}

# replace any symbol strings with the corresponding symbols
for symbol in symbols:
    f_str = f_str.replace(symbol, 'symbols["{}"]'.format(symbol))

# convert user input to a lambda function
f = lambda x: eval(f_str)

# calculate derivative of function at x = 0
df = derivative(f, 0)

# print derivative
print("The derivative of f(x) is: ", df)