import re
from sympy import *

# get user input for function
f_str = input("Enter a function in the format 'f(x) = ...': ")

# extract function expression from input string using regular expressions
pattern = r"([+-]?\d*)([a-z]?)(\^?\d*)"
terms = re.findall(pattern, f_str)
expr = ""
for term in terms:
    coeff = term[0] if term[0] != "" else "1"
    var = term[1] if term[1] != "" else "1"
    power = term[2].replace("^", "") if term[2] != "" else "1"
    expr += f"{coeff}*x**{power}*sqrt({var}) + "

# remove trailing plus sign and space
expr = expr[:-2]

# convert expression to SymPy expression
f_sym = sympify(expr)

# take derivative of function with respect to x
df_sym = diff(f_sym, x)

# print derivative expression
print("The derivative of f(x) is: ", df_sym)
