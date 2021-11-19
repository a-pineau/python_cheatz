#####################
#    Exceptions     #
#####################
# General comments:
# Better use try-except than if else to handle exceptions
# Python encourages EAFP (“It’s easier to ask for forgiveness than permission”)
# 64 exceptions (built-ins)
# An exception is a class
# BaseException: SystemExit, KeyboardInterrupt, GeneratorExit, Exception ()
# Python raises exception when those occur
# Can "manually" raise one

# try-except (classic example)
# 1
while True:
    try:
        age = int(input("Age?: "))
        break
    except Exception:
        print("Not a valid age, try again")

# or...
# 2
keep_asking = True
while keep_asking:
    try:
        age = int(input("Age?: "))
        keep_asking = False
    except Exception as e:
        print("Not a valid age, go again.", e)

# try-except (classic example, again)
while True:
    try:
        age = int(input("Age?: "))
    except Exception:
        print("Not a valid age, try again")
    else:
        print("Correct input")
        break

# try-except-else-finally (to make sure to close a file)
def display_begining(file_name):
    try:
        f = open(file_name, "r")
    except Exception:
        print("File not found")
    else:
        print(f.readline())
    finally:
        try:
            f.close()
            print("Closing file...")
        except:
            pass

# Specify an exception instead of an empty except
try:
    a = 1/0
except ZeroDivisionError:
    print("Oof")

# Successives except blocks
try:
    pass
except ZeroDivisionError:
    print("Division error")
except FloatingPointError:
    print("Numerical issue")
except ValueError:
    print("Value Error") # etc

# Raise an exception w/ raise
ch = int(input("1, 2 or 3? : "))
if ch not in {1, 2, 3}:
    raise ValueError("Incorrect input")

# Test an assertion w/ assert
try:
    age = int(input("Age? : "))
    assert age > 0
except ValueError:
    print("Incorrect input")
# /!\ assert is best used for debuging purposes
# Better use the code below
try:
    age = int(input("Age? : "))
    if age < 0:
        raise ValueError
except ValueError:
    print("Incorrect input")

# Forget the errors (obviously dangerous)
try:
    a = 1/0
except Exception:
    pass