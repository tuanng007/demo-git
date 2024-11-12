file = open('E:/diem.txt', 'w')

file.write('Hello, world!')

file.close()

file = open('E:/diem.txt', 'r')

content = file.read()
print(content)
file.close()
