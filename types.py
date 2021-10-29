#####################
#       Types       #
#####################

# General comments:
# 1. Strings are immutable
# 2. Iterable
# 2. Sequential (slicing doable)

s = "new string"
s = 'new string with "those things"'
s = 'that\'s a string with an escape character'
s = "\\"  # \
# s = "\"  # SyntaxError
# s = "string with \" # SyntaxError
s = "string with \ stuff"
s = "string with a \nNew line"  # \n linebreak
s = "string with no \\nNew line"
# All escape characters: https://www.w3schools.com/python/gloss_python_escape_characters.asp
repr(s) # Literal expression: 
s = "\\" # repr(s): "\\\\"
s = "This is a \\n test" # repr(s) "'This is a \\n test'"
s = """With the use 
of triple quotes""" # Equivalent to "With the use of \ntriple quotes"
s = r"With no \n escape character" # Raw string to avoid escape characters
# for letter in s: # Iterate over a string
s = reversed("abcdef") # Returns a reversed object. Can be transformed using a list conversion (list(reversed("abcdef"))
s = "abcdef"
s = s[::-1] # Better solution to avoid conversion
s = "ABC" + "DEF" # Concatenation
s = "A" * 3 # Multiplication
# s = "AB" - "BC" TypeError obviously
n = int("-123456") # Conversion string -> int
s = str(n) # Conversion string -> int
f = float("-1234.567") # Conversion string -> float
s = str(f) # Conversion float -> string
res = eval("(2*3)/(5+10)+27") # Evaluate arithmetic expression (here, res=27.4)
l = list("abcdefg") # Conversion string -> list: ["a", "b", "c", "d", "e", "f", "g"]
t = tuple("abcdefg") # Conversion string -> tuple
set_ = set("aaaabbbbccc") # Conversion string -> set ({a, b, c}, unordered)
s = str([0, 1, 2]) # Conversion list -> string ("[0, 1, 2]", i.e. what print(object) returns)

# format
s = "This is test {}, test {} with test {}".format(3, 2, 1) # Standard
s = "This is test {2}, test {1} and test {0}".format(3, 2, 1) # Positional 
a, b, c = 4, 5, 6
s = "This is test {a}, test {b} and test {c}".format(a=a, b=b, c=c) # Named

# with "-f" (better)
a, b, c = 10, 11, 12
s = f"This is test {a}, test {c} and test {b}"

s = chr(80) # chr(n): Unicode character of number n (here, s = "P")
n = ord("P") # Unicode number of a charachter (here, n=80)

"a" in "abcd" # True
"e" not in "abcd" # False
"a" < "b" # True
"a" < "1" # False (Unicode numbers are being compared)

# Methods
n = "ABCCDDABXDABUZUZAB".count("AB") # Returns (int) number of occurrence of "AB"
pos = "AB AAAA B CCCC DDDD EF GGG".find("E") # Returns (int) index at which the substring starts (returns -1 if not found)
pos = "AB AAAA B CCCC DDDD EF GGG".rfind("E") # Same except starts from the end (returns -1 if not found)
pos = "AB AAAA B CCCC DDDD EF GGG".index("E") # Same than find, but ValueError if substring not found
pos = "AB AAAA B CCCC DDDD EF GGG".rindex("E") # Same than rfind, but ValueError if substring not found
s = "AAABBBCCCDDDEEE".replace("A", "-20") # Returns a new string with "A" replaced by -20
s = "AAABBBCCCDDDEEE".replace("A", "-20", 2) # Returns a new string with "A" replaced by "-20" but two times only (the firsts)
s = "-".join(["A", "B", "C", "D", "E"]) # A-B-C-D-E (s = "<string>".join(iterable))
s = "".join(("A", "B", "C", "D", "E")) # ABCDE
s = "#".join("ABCDE") # A#B#C#D#E
s = "A B C D E".split() # Returns a list, ["A", "B", "C", "D", "E"] (space is the by default separator)
s = "A,B,C,D,E".split(",") # ["A", "B", "C", "D", "E"]. If the separator cannot be used, return the original string
s = "ABCDE".split("C") # ["AB", "DE"]
s = """AAA
BBB
CCC
DDD""".splitlines() # Split string accodring to \n (["AAA", "BBB", "CCC", "DDD"])
s = "abcdef".upper() # Converts to uppercase # "ABCDEF"
s = "ABCDEF".lower() # Converts to lowercase # "abcdef"
s = "ABCDEF".isupper() # True
s = "abcdef".islower() # True
s = "abcdeF".islower() # False
s = "salut bonjour oui bonsoir merci bye".title() # Each letter becomes uppercase
s = "I NEED Money".istitle() # False
s = "i NEED Money".capitalize() # First letter of the string becomes uppercase, (other uppercase become lowercase)
s = "aBcDeFgHiJ".swapcase() # Inverts uppercase and lowercase: "AbCdEfGhIj"
test = "12345abcdef".isalnum() # True (only numbers and letters)
test = "*12 # ab".isalnum() # False
test = "12345abcdef".isalpha() # False (only letters)
test = "12+34".isdigit() # False
test = "1234".isdigit() # True
test = "1234".isdecimal() # True (same than isdigit())
test = "1234".isnumeric() # True (shan than isdigit())
test = "          ".isspace() # True (only spaces)
test = "    .     ".isspace() # False
test = "This is a very useful test".endswith("test") # True (ends with "test")
s = "   AB   ".strip() # Returns a string with no left and right spaces (s = "AB")
s = "   AB   ".lstrip() # Returns a string with no left space (s = "AB   ")
s = "   AB   ".rstrip() # Returns a string with no right space (s = "   AB")
s = "ABCD".center(40) # Returns a centered string of length 40 (n) 
test = "Hello\n Hello".isprintable() # False, not every character can be printable
test = "Hello and hello".isprintable() # True

# maketrans (class method: str.maketrans)
# Creates a dict used to transform a string using the translate method
intab = "aeiou"
outtab = "12345"
TABLE = str.maketrans(intab, outtab) #intab and outtab must be of equal length
# keys: unicode numbers of letters a, e, i, o and u
# values: unicode numbers of "1", "2", "3", "4" and "5"
print(TABLE)
# translate
# Replace (returns) characters of a string according to a table (dict)
s = "Les sanglots longs des violons"
s = s.translate(TABLE)
print(s)
