#####################
#  Data structures  #
#####################

# In console "help" to enter help mode
dir(object) # Shows object's attribute
help(object) # Shows documentation (if any) of a module, class, function, object, variable, etc.
help(object.method) # Shows documentation (if any) of object's specified method

# ----- list ----- #
# General comments:
# 1. Iterable
# 2. Items can de duplicated
# 3. Ordered collection
# 4. Mutable collection
# 5. Sequential collection (elements can be accessed through indexes. Slicing is doable)

l = [] # Create empty list
l.append(5) # Add 5
l[-1] # Last element w/ negative index
del l[0] # Remove element 0 (mutation)
l = l + [4, 5, 6] # Add values to list
l = l + ["a"] * 3 # Add same value n times
l = l * 2 # Multiply n times
l = list("abcdefghijklmnpoqrstuvwxyz") # Convert to list. Any iterable can be converted

# Slicing (l[start:stop:step]) /!\ proceeds by shallow copy
l[2:5] # From index 2 to 4 (5 is excluded)
l[::] # Full list
l[::-1] # Full reversed list
l[-3:] # Third element from end to end
l[-3:15:-1] # Third element from end to index 16
l[-1::-1] # Full reversed list
l[:-2] # All elements except the last twos
l[::2] # Take every two elements (first is included)
l[2:5:-1] # Will return empty list. Negative step works from right to left (stop before start)
l[2:5] = [1, 2, 3] # Assigment by slicing (adding more element will extend the list)
l[2:5] = [] # Remove element from 2 to 4 (included)
# Declaring a slice in case of repeated use
from_2_to_10 = slice(2, 2 + 10) # slice(start, stop, step)
l[from_2_to_10]
del l[10:20] # Slice deletion

# list methods
l = [1, 5, 243, -23, 234, 934] 
len(l) # Returns (int) list's size
l.sort() # Mutation. sort(reverse=True/False, key=fun())
sorted(l) # Return reversed list. sorted(list, reverse=True/False, key=fun())
l.reverse() # Mutation
reversed(l) # Return reversed list. /!\ returns and iterator
l.remove(value) # Remove value from list
l.index(value) # Returns value's index
l.count(value) # Returns value's occurence number
l.insert(index, value) # Insert value at index. Mutation
l.extend(ll) # Extend l w/ l1. Mutation
l.pop() # Remove last element. Mutation
l.max() # Returns max element
l.min() # Returns min element
ll = l.copy() # Shallow copy
l.clear() # Clear content 

# ----- tuple ----- #
# General comments:
# 1. Iterable
# 2. Items can de duplicated
# 3. Ordered collection
# 4. Non-mutable collection
# 5. Sequential collection (elements can be accessed through indexes. Slicing is doable)

t = () # Create empty tuple
t = (1, 4, 20) # Create non-empty tuple
t[0] = 8 # AttributeError (Non-mutable collection)

# ----- set ----- #
# General comments:
# 1. Iterable
# 2. Items are unique
# 3. Unordered collection
# 4. Mutable collection
# 5. Non-sequential collection (elements cannot be accessed through indexes)

s = set() # Create empty set. Writing s = {} will create an empty dictionnary
s = {2, 4, 6} # Create non empty set
s = {2, 2, 4, 6, 6} # >>> s : {2, 4, 6}
s = set("abcdefg") # Create set from iterable (string in this case)
s = set([0, 2, 4, 5, 26]) # From list
s = set((0, 2, 4, 5, 26)) # From tuple
# Operations on set
X = {0, 1, 2, 3}
Y = {2, 3, 7, 10, 11}
X - Y # Difference -> {0, 1}
Y - X # Difference -> {7, 10, 11}
X | Y # Reunion -> {0, 1, 2, 3, 7, 10, 11}
Y | X # Reunion -> {0, 1, 2, 3, 7, 10, 11}
X & Y # Intersection -> {2, 3}
Y & X # Intersection -> {2, 3}
X ^ Y # Symmetric difference -> {0, 1, 7, 10, 11}
Y ^ X # Symmetric difference -> {0, 1, 7, 10, 11}
# set methods
s.add(10) # Mutation. Add element to set
s.remove(10) # Mutation. Remove element. KeyError of element isn't found
s.discard(-1) # Mutation. Remove element. No exception raised
s.update({22, 44, 66}) # Mutation. Update set. Works w/ any iterable
s.pop() # Mutation. Remove last element. KeyError is empty est
s.clear() # Mutation. Clear set. No exception raised if empty set
s |= {22, 44, 66} # Mutation. Same than above. Works only w/ set
s = {1, 3, 7} # Re-initialisation
s.intersection_update({7, 9, 14}) # Mutation. Intersection. Works w/ any iterable (s = {7})
s &= {7, 9, 14} # Mutation. Same than above. Works only w/ set (s = {7})
s.difference_update({7, 9, 14}) # Mutation. Difference. Works w/ any iterable (s = {1, 3})
s -= {7, 9, 14} # Mutation. Same than above. Works only w/ set
s.symmetric_difference({7, 9, 14}) # Mutation. Symmetric difference. Works w/ any iterable (s = {1, 3, 9, 14})
s ^= {7, 9, 14} # Mutation. Same than above. Works only w/set

# ----- frozenset ----- #
# 1. Iterable
# 2. Items are unique
# 3. Unordered collection
# 4. Non-mutable collection
# 5. Non-sequential collection (elements cannot be accessed through indexes)

fs = frozenset() # Create empty frozenset
fs = frozenset({2, 4, 6})
fs.add(5). # AttributeError. No mutation allowed

# ----- dict ----- #
# General comments:
# 1. Hash table (similar to map in C++)
# 2. format: { key: value } 
# 3. Authorized keys: non mutable data (int, float, string). To potentially avoid this, use repr(non-mutable data) as key
# 4. Non-sliceable, but subscriptable: dict[key] = value
# 5. Mutable collection

d = {} # Create empty dict
d = dict() # Same (less efficient?)
d = {"a": 1, "b": 2, "c": 3, "d": 4} # Standard creation
d = dict([["a", 1], ["b", 2], ["c", 3], ["d", 4]]) # Using dict(). From an iterable (list) of couples (only!)
d = dict([("a", 1), ("b", 2), ("c", 3), ("d", 4)]) # Using dict(). From an iterable of (tuple) couples (only!)
# dict methods
# set methods
d.items() # Returns a <dict_items> object (iterable) /!\ Unordered (can use l = sorted(list(dict.items())))
d.values() # Returns a <dict_values> object (iterable) 
d.keys() # Returns a <dict_keys> object (iterable) 
d.get(key, default) # If key is found, returns d[key], else default (to avoid KeyError exception)
d.pop(key) # Mutation. Returns d[key] and removes the associated item
d.popitem(key) # Mutation. Returns a tuple (key, value) from the last inserted item and removes it
d.setdefault(key, value) # Mutation. Returns d[key] if key exists, else return d[key] anyway and inserts key:value
d.update(other_d) # Mutation. Mix two dicts. If a key is repeated, the item from other_d is used
d = dict.fromkeys(keys) # Returns a dict of keys: None (keys must be hashable)
d = dict.fromkeys(keys, value) # Returns a dict of keys: value (keys must be hashable)
d.clear() # Mutation. Clear dict
del d[key] # Mutation. Remove d[key] if key exists. KeyError otherwise
# Iteration
for item in dict: # Iterate over KEYS! /!\ ("x in d" will lookup the keys only)
for x, y in dict.items(): # Iterate over items (x: keys, y: values)



# ----- Miscellaneous # -----
l = "a b c d".split(" ") # Conversion string -> list (returns [a, b, c, d])
indexes = [i for i, x in enumerate(l_keys) if x == min_key] # Returns all indexes of an identical value
return max(dico, key = lambda k: dico[k]) # Returns the key associated to the max value (first key if multiples max)
for key, value in dico.items(): # Returns the key corresponding to the value
  if value == target:
     return key
     
