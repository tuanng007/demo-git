import os

current_directory = os.getcwd()
print(f'Current Directory: {current_directory}')

os.chdir('E:/')
print(f'Changed Directory: {os.getcwd()}')

try:
    os.makedirs('E:/thuchanh')
    os.makedirs('E:/lythuyet')
except FileExistsError:
    pass  

open('E:/thuchanh/bai01.py', 'w').close()
open('E:/thuchanh/taptin.txt', 'w').close()
open('E:/thuchanh/code.c', 'w').close()
open('E:/lythuyet/chap01.txt', 'w').close()
open('E:/lythuyet/final.txt', 'w').close()
open('E:/diem.json', 'w').close()

print(f'Files and Directories: {os.listdir()}')
