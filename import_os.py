#####################
#        OS         #
#####################

import os
from datetime import datetime

print("path=", os.path.dirname(__file__))
print(os.getcwd())
os.chdir("/home/adrian/Desktop/Python_training")
print(os.getcwd())
# os.makedirs("osdemomo/mono")
# os.removedirs("osdemomo/mono")
os.chdir("/home/adrian/Desktop")
# os.rename("testes.txt", "loulz.txt")
print(os.getcwd())
# print(os.listdir())
# print(os.stat("loulz.txt"))
# mod_time = os.stat("loulz.txt").st_mtime
# print(datetime.fromtimestamp(mod_time))

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