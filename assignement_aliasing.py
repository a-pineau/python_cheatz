###################################
#     Assignement & Aliasing      #
###################################
import copy

# Permutation
x, y = 1, 2
x, y = y, x
# Returns multiple variables using decompression
def fun(x):
    return x**2, x*10, x-2 # Returns a tuple: (25, 50, 3)
# Decompression using splat (*)
a, b, *c = range(0, 8) # 0 1 [2, 3, 4, 5, 6, 7]
a, b, c = 1, 2, range(0, 8) # 1 2 [0, 1, 2, 3, 4, 5, 6, 7]
# Affectation using queues
x = y = z = 2 # Not the best practice
# Using inplace operator
a = 2
a += 2 # a = a + 2
a -= 2 # a = a - 2
a /= 2 # a = a / 2
a *= 2 # a = a * 2
# Notions of identificator
a = 2 
'''
The integer 2 is written in memory scope
The char "a" is written in the name scope
"a" points towards 2 and "a" is an identificator of 2
Python only works w/ identificators (which can be seen as pointers)
'''
a = "abcd"
'''
Python writes the string "abcd" in the memory scope
"a" points towards "abcd" and 2 is removed through the garbage collector
An identificator always points to a variable, and not another identificator
'''
# Case of mutable data
# Mutable data: dict, list, bytearray, set
X = [1, 10, 100] # Creates an identificator "X" and 3 variables: 1, 10, 100. 
# X[0], X[1], X[2] are not identificators
# Aliasing
Y = X
Y[0] = 5 # Y: [5, 10, 100], X: [5, 10, 100] -> X was CHANGED too
X[2] = [444] # X, Y: [5, 100, [444]]
X = 0 # X: 0, Y: [5, 100, [444]] X = 0 isn't a mutation
'''
Any mutation of X will modify Y (works in both way)
'''
X = Y # X is Y: True
# If X is Y is True: X and Y points to the same data
a = 5
b = 5 # a is b: True, a == b: True, id(a) == id(b)
A = [10, 20]
B = [10, 20] # A is B: False, A == B: True, id(A) != id(B)
# A mutation occurs when the content of a mutable object was modified while keeping the same object's id()
# Shallow copy
L1 = [[1, 2, 3], [4, 5, 6]]
L2 = L1.copy() 
L1[0][2] = "Z" # L1: [[1, 2, "Z"], [4, 5, 6]], L2: [[1, 2, "Z"], [4, 5, 6]]
# Deep copy
L1 = [[1, 2, 3], [4, 5, 6]]
L2 = copy.deepcopy(L1)
L1[0][2] = "Z" # L1: [[1, 2, "Z"], [4, 5, 6]], L2: [[1, 2, 3], [4, 5, 6]]
# global, local and built-ins variables
# global: lowest level, at the root of the code
# local: defined in a function
# built-ins: defined in the built-ins module
s = "abcd"
def f():
    print(s) # global variable s ("abcd")
# Name resolution order: local -> global -> built-ins -> NameError exception
globals() # display global variables
locals() # display local variables. Using locals at root == globals()