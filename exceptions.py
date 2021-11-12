#####################
#    Exceptions     #
#####################
# General comments:
# Better use try-except than if else to handle exceptions
# 64 exceptions (built-ins)
# An exception is a class
# BaseException: SystemExit, KeyboardInterrupt, GeneratorExit, Exception ()

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
