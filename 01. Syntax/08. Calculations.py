# Using numbers in calculations means we have to define them in a very specific way. We can't define them as strings (surrounded by quote marks). They need to be defined as INT() or FLOAT() to be used in mathmatical equations.
# When building equations, remember the "Order of Operations", or PMDAS for short (Parenthisis > Multiplication > Division > Addition > Subtraction).
#Also note that when Python performs division, it will automatically convert all INTs into FLOATS, due to the necessity of possible decimal points.

# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)

#IF you try to divide by zero, Python can throw a special error for that. It's called the ZeroDivisionError, since you can't divide by 0.
print(115/0)
