import os
import shutil


print(os.listdir())
print(os.getcwd('/home/username/1.py'))
# C:\Users\user1\Desktop\1.py -- Windows
# /home/user1/Desktop/1.py -- Linux, MacOS, Unix-like
print(os.cpu_count())

print(os.path.abspath('3_os.py'))


