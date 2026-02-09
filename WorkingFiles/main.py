# working files
import os

f_names = open("names.txt","r")
# print(f_names.read())
# print(f_names.readline())
# print(f_names.readline())
# print(f_names.readline())

for line in f_names:
    print(line)


f_names.close()



with open("numbers.txt") as f:
    content = f.read()
    numbers_list = content.split()
    print(numbers_list)
    numbers_list = map(int, numbers_list)
    print(sum(numbers_list))

if os.path.exists('forDelate.txt'):
    os.remove('forDelate.txt')
else:
    print("Bunday file yoq! Oldinroq o'chirib yubording!")
