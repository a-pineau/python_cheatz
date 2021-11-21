#####################
#      Modules      #
#####################
# General comments:
# list of base modules: https://docs.python.org/3/library

# with os
import os # by doing this, python knows about os, but nothing about its content
os.getcwd # to access a specific function of the module
from os import getcwd # to import a specific function
import math as m # to import a module using a different name
from os import * # to import everything (dangerous, since some function have the same name and can be erased, such as open)

# import its own modules (assuming main and the module are in the same folder)
import my_module
print(my_module.v)
my_module.f(4, 5)
print("NAME:", __name__)

# sys
from sys import modules
print(modules) # all base modules

# os
# Considering C://Python3/lib/tkinter/__init__.py
# nom propre: __init__.py
# nom pur: __init__
# extension: .py
# path: C://Python3/lib/tkinter
# full name: C://Python3/lib/tkinter/__init__.py

print("path=", os.path.dirname(__file__))
print(os.getcwd()) # current working directory (default python folder)
os.chdir("/home/adrian/Desktop/")
print(os.getcwd())
print(os.listdir())
os.makedirs("osdemomo/mono")
os.removedirs("osdemomo/mono")
os.chdir("/home/adrian/Desktop")
# os.rename("test1.txt", "test2.txt") # rename two files

# concatenation
from os.path import join
X, Y = os.getcwd(), "test.txt"
PATH = join(X, Y)
print("PATH=", PATH)

for dirpath, dirnames, filenames in os.walk("/home/adrian/Desktop"):
    pass
    # print('Current path:', dirpath)
    # print('dirnames:', dirnames)
    # print('filenames:', filenames)

print(os.environ.get("HOME"))
print(os.path.join(os.environ.get("HOME"), "test.txt"))
print(os.path.basename("/tmp/test.txt"))
print(os.path.dirname("/tmp/test.txt"))
print(os.path.exists("/tmp/test.txt"))
print(os.path.isfile("/tmp/test.txt"))
print(os.path.isfile("/tmp/"))