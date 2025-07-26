#strong password generator
import random
import string

s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.printable)
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
inpo = input('what lent of strong pasword :')
while True:
    try:
        inpo = int(inpo)
        if inpo < 6 or inpo > 20:
            inpo = input("pleas enter uppur 6 and under 20: ")
        else:
            break
    except:
        inpo = input("Only number pleas :")

part1 = round(inpo*30/100)
part2 = round(inpo*20/100)
password = []
for i in range(part1):
    password.append(s3[i])
    password.append(s4[i])
for i in range(part2):
    password.append(s1[i])
    password.append(s2[i])
random.shuffle(password)
password = "".join(password[0:])

print(password)