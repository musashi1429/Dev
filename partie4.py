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

### exercice 6
tableau = ["botte", "glasse", "ruta", "hotte","op"]
print("merci d'acheté", tableau[0],"et", tableau[-1])
print("merci d'acheté", max(tableau))

###exercice 7

#import json

#def personne(personnage,info ):
#    values = []
#    with open("personnage") as f:
#        data = json.load(f)
#        for entry in data:
#            values.append(entry[2])
#    return values


#print(personne([2],info))

character = [
["kassama","fally","28","1990"],
["kazama","jin","33","1986"],
["","","",""]
]


if input("choisi le perso que tu veux 1,2 ou 3 ") == "1":
    print(character[0],)
if input("choisi le perso que tu veux 1,2 ou 3 ") == "2":
    print(character[1],)

if input("choisi le perso que tu veux 1,2 ou 3 ") == "3":
    print(character[2],)


perso=["kassama", "fally", "28", "1990"]
perso2=["ouloulou","tmsoule","56", "1936"]

nom = input("nom? ")
prenom= input("prenom? ")
age = input("age? ")
date_de_naissance= input("date de naissance ?")

perso3=[nom, prenom, age, date_de_naissance]

character=[perso,perso2,perso3]
off = ""
print("perso differents")

while off != "stop":
    off = input("tu veux arreter?")
    if input("tapez 1 pour le premier perso") == "1":
        print(perso[0], perso[1],"a",perso[2], "et est néé en",perso[3])

    if input("tapez un 2 pour le deuxieme perso") == "2":
        print(perso2[0], perso2[1],"a",perso2[2], "et est néé en",perso2[3])

    if input("tapez 3 pour le troisieme perso") == "3":
        print(perso3[0], perso3[1],"a",perso3[2], "et est néé en",perso3[3])
    else :
        print("merci de de choisir 1 ou 2 ou 3")

if input() == "stop":
    print("bye bye")
###exercice 8
grille = ["nsdvnsl","hsdljshg","jnskjn", 349,6754754, 9]
listtr = []
listint = []

def table(tab):
    listtr = list()
    listint = list()
for element in grille :
    if isinstance((element),str):
        listtr.append(element)
    if isinstance((element),int):
        listint.append(element)

print(len(listtr))


#### exercice 9
todolist = []
task = ""
while task != "stop":
    task = input("met ce que tu veux pardi !!")
    todolist.append(task)
for task in todolist :
    print(task)
