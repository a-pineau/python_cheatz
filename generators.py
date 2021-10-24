#####################
#  Data structures  #
#####################
from random import randint
import itertools

# -- General comments:
# 1. The memory isn't filled with all the elements
# 2. The formula defining the generator is kept in memory as well as its rank
# 3. A StopIteration exception is raised after reaching the last rank
# 4. A generator is not a sequence (no indexing or slicing)
# 5. Non-mutable
# 6. No len() or reversed()

G1 = (x**2 for x in range(100)) # type(G): <class 'generator'>
G2 = (x**4 for x in range(100)) # type(G): <class 'generator'>
G3 = (x for x in range(10)) # type(G): <class 'generator'>

for element in G1: # Iterate over generator G
    print(element)

print(next(G2), next(G2), next(G2)) # 0 1 16 
print(5 in G3) # True
print(2 in G3) # False (you cant go backwards)

# -- Reversed() method
# Transforms a sequence by reversing it
# Returns a specific generator (<class 'reversed'>)
rev = reversed([4, 5, 6]) # <class 'list_reverseiterator'>
print(type(rev))
for element in rev:
    print(element)
# next(rev) -> StopIteration raised

# -- Function iter()
# Creates a generator from any iterator
iter_string = iter("The Smiths")
iter_list = iter([1, 2, 3, 4, 5])
print(type(iter_string)) # <class 'str_iterator'>
print(type(iter_list)) # <class 'list_iterator'>

'''
let L be an iterable
for x in L:
    print(x) : is equivalent to:

X = iter(L)
while True:
    try:
        print(next(X))
    except StopIteration:
        break
'''

# -- Personalized generator
class MyRange():
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_range = MyRange(4, 15)
print(next(my_range))

# target value with iter()
def get_rnd():
    return randint(0, 50)

IT = iter(get_rnd, 25)
for x in IT: # stop right before the target value (25) is returned. No StopIteration exception
    print(x)

# -- Generator w/ yield()
def g():
    for x in range(10):
        yield x**2

type(g) # <class 'function'>
G = g() 
type(g) # <class 'generator'>
print(next(G)) # 0
print(next(G)) # 1
print(next(G)) # 2

# -- Function enumerate()
L = ["David", "John", "Robert", "Richard"]
for t in enumerate(L):
    print(t) # tuple: (0, "David"), (1, "John"), etc.

for index, name in enumerate(L):
    print(index, name) # 0 "David", etc.

# -- Function zip()
L1 = ["a", "b", "c", "d", "e"]
L2 = list("".join(L1).upper())
for elem in zip(L1, L2): # Can use zip w/ more than 2 iterables
    print(elem) # tuple: ("a", "A"), ("b", "B"), etc.

for x, y in zip(L1, L2):
    print(x, y) # "a" "A", etc.

# -- Function filter()
# Let L be an iterable and f a function thats returns True or False
# filter(f, L) returns a generator such as f(x) is True
L = [randint(0, 100) for x in range(20)]
filt = filter(lambda x: x > 50, L) # <filter object>
for x in filt:
    print(x)

# print(next(filt)) # StopIteration exception
filt = list(filter(lambda x: x > 50, L))
print(filt)
# /!\ BETTER USE LIST COMPREHENSION
filt = [x for x in L if x > 50]
print(filt)

# -- Function map()
# Let L be an iterable and f a function
# map(f, L) returns a sequence with f(x) for x in L as elements
squares = map(lambda x: x**2, L) # <map object>
# /!\ BETTER USE LIST COMPREHENSION
squares = [x**2 for x in L]

# -- Itertools (some example)
# itertools.chain : concatenate iterables
X, Y = [1, 2, 3], [4, 5, 6]
Z = itertools.chain(X, Y) # Can chain as much as needed
for x in Z:
    print(x)

# next(Z) # StopIteration