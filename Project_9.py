#Sum of ASCII codes for letters entered
print('*********Sum of ASCII codes for letters entered*********')
Ascii = str(input('Enter Your Letters: '))
b = 0
for i in Ascii:
    b += ord(i)
    continue;
print(b)
        