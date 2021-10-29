#####################
#     Aliasing      #
#####################

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
'''