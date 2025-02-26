import os
import string
import shutil
#1
path = r"C:\Users\User\OneDrive\Рабочий стол"

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories:", directories)

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files:", files)

all_items = os.listdir(path)
print("All items:", all_items)
#2
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))
#3
exictence=os.access(path, os.F_OK)
if exictence==True:
    print("path exists")
    print("directory path: "+ os.path.dirname(path))
    print("name: "+ os.path.basename(path))
else:
    print("path dont exist")

#4
with open('row1.txt', 'r', encoding='utf-8') as file:
    count=sum(1 for l in file)
print(count)
#5
li=['Assel', 'Anel', 'Dariya', 'Bek', 'Serdar', 'Nurasyl']
file1='row1.txt'
with open(file1, 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(li))
print('done')
#6
lettters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for let in lettters:
    with open(let + '.txt', 'w') as file2:
        file2.writelines('file '+ let+'.txt' ' have been opened')
print('26 files are created')
#7
with open('A.txt', 'r') as from1, open('B.txt', 'a') as to1:
    to1.write("\n"+from1.read())
print('file copied')

shutil.copyfile('C.txt', 'D.txt')
print('file copied 2.0')

#8
pathd=r'C:\Users\User\OneDrive\Рабочий стол\Текстовый документ.txt'
existi=os.access(pathd, os.F_OK)
if existi == True:
    print('file exist')
    os.remove(pathd)
    existi1=os.access(pathd, os.F_OK)
    if existi1 == False:
        print('file has been deleted')
    else:
        print('file are still exist')
else:
    print("file don't exist")