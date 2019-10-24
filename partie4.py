## 1\.Exercice 1 : Un échiquier ma logique a peaufinner.
#i = "# "
#b = " #"
#echiquier = ""
#while len(echiquier) <= 73:
#    echiquier.append(b)
#if echiquier.append(b)
#    echiquier.append(i)
#if len(echiquier) == 73:
#    print(echiquier)

#Exercice 1 fait
c = "# "
b = " #"
echiquier =""

for i in range(0, 8):
    if (i % 2 == 0):
        echiquier += b *8 + "\n"
    else:
        echiquier += c *8 + "\n"
print(echiquier)

###exercice 2:
code=[0, 0, 0, 0]
a= 0
b= 0
c= 0
d= 0
e= "------------"
for i in range(0,4) :
    code[i] = 1
    a = code[0]
    b = code[1]
    c = code[2]
    d = code[3]
    print("{}\n{}\n{}\n{}\n{}".format(a,b,c,d,e))
    code[i]= 0
###exercice 3:
from math import *

def pair(panier):
    if panier %2 == 0:
        print("True")
    else:
        print("False")



panier = round(63.4)
print(panier)
print(pair(panier))

###exercice 4:
print("insert number ")
chiffre= int(input())
print("le factorielle de ", chiffre, "=")
facto = 1
while chiffre != 1:
    print("*",chiffre, end='' )
    facto *= chiffre
    chiffre -= 1
print("\n", facto)

###exercice 5:
def re(text):
    text = text.replace('-', '\_')
    return(text)

texti="oulou - - - - - louuuu"
print(re(texti))
