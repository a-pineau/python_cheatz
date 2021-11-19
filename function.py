import doctest

#####################
#     Functions     #
#####################
# General comments:
# A function is a type (type(f) == function)
# A function is a calleable (along w/ classes and methods)
# In Python, a function that doesn't return anything actually returns None
# A parameter is the variable listed inside the parentheses in the function definition
# An argument is the value that is sent to the function when it is called
# Do not use default argument values when using mutable data in function (side effects)
# Global mutable variable can be modified inside functions (e.g. lists, etc.)
# Positional arguments are arguments that can be called by their position in the function definition
# Keyword arguments are arguments that can be called by their name
# Required arguments are arguments that must passed to the function
# Optional arguments are arguments that can be not passed to the function. In Python, optional arguments are arguments that have a default value
# Using restrictions: def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2) 


# Multiple return
def f(x, y):
    return x**2, y**3 # type tuple

# A function as a variable
var = f # no paranthesis

# Functions can be put inside iterable
t = (f, f)
t = [f, f]
t = {f, f}

# Returning None
def no_return():
    pass # print(no_return()) : None

# Any type of argument
def square(val):
    return val*2

print(square(2), square("ABC"))

# docstring
def doc():
    """
    A very useful function
    Arguments: None
    Returns: None
    """
    pass
#print(help(doc))

# doctests
def square(x):
    """
    Computes square of positional argument x
    Argument: x
    Returns: x**2
    >>> square(5)
    25
    >>> square(10)
    100
    """
    return x**2
doctest.testmod() # test OK

# global vs local
def f(): # no global
    x = 0
    print("In the function f, x=", x, sep="")

x = 3
f()
print(f"In the main program, x={x}")

def f(): # with global
    global x
    x = 0
    print("In the function f, x=", x, sep="")

x = 3
f() # f modifies the x variable declared just above
print(f"In the main program, x={x}")

# Default arguments
def f(a, b=1, c=2): # non-default arguments always come first unless specified by name
    return a + 2*b + c

print(f(1), f(c=1, a=4, b=10))

# Side effects (occurs when using mutable data)
def f(L=[1, 2, 3]): # Nope, because the default value is evaluated only once, i.e. during its definition
    L.append(0)
    return L

def f(L=None): # Better
    if not L:
        L = [1, 2, 3]
    L.append(0)
    return L

# Specials arguments
# Positional argument that is optional 
def f(x=2, /): # f() OK, f(1) OK, f(x=1) NOT OK
    pass
# Positional argument that is required 
def f(x, /): # f() NOT OK, f(1) OK, f(x=1) NOT OK
    pass
# Keyword argument that is optional
def f(*, x=2): # f() OK, f(1) NOT OK, f(x=1) OK
    pass
# Keyword argument that is required
def f(*, x): # f() NOT OK, f(1) NOT OK, f(x=1) OK
    pass

# Unpacking iterables w/ *
# 1
def f(a, b, c):
    return a + 2*b + c

print(f(*[1, 2, 3])) # Unpacked list 
 
# 2
def sum(*data):
    s = 0
    for val in data:
        s += val
    return s

print(sum(*[1, 2, 3, 4, 5]))

# 3
def f(*args):
    print(*args, args)

f((1, 2, 3), "a", "b", 456)

# 4
def f(a, b, c):
    return a + 2*b + c

d = {"a": 1, "b": 2, "c": 3}
print(f(**d), f(**{"a": 1, "b": 2, "c": 3})) # Unpacked form of d is a=1, b=2, c=3

# 5
def f(**kwargs):
    for key in kwargs.keys():
        print(key)

f(a=1, b=2, c=3) # keys must be of string type
f(**{"a": 1, "b":2, "c": 3})

# lambda functions
# 1
square = lambda x: x**2
print(square(2))

# 2 (multiples variables)
f = lambda x, y, z: x**2 + y/10 - z*5
print(f(1, 2, 3))
print(f(*(1, 2, 3))) # Unpacking tuple

# 3 (simulating a if-else)
b = False
f = b and (lambda x: x**2) or (lambda x: x-10)
print(f(10)) # 0

