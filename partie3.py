##Exercice 1
import random

a = random.randint(1,11)
b = random.randint(1,11)
c = random.randint(1,11)
d = random.randint(1,11)

list = [a,b,c,d]
print(max(list))

##Exercice 2
import math
user = ""
while user != "stop":
    print("entrer votre age")
    Age = int(input())
    if Age <= 0:
        print("merci d'indiquer un age réel")
    if Age >= 21:
        print("vous étes autorisé a accéder au portail")
    if Age%2 == 0:
        print("age pair,mhh,chanceux!!!")
    if math.sqrt(Age).is_integer():
        print("votre age et un carré")
    user = str(input("si vous voulez quittez tapez stop ou entrer pour continuer"))


##Exercice 3
v = random.randint(1,11)
u = int(input("trouver le chiffre au hasard: "))
s =""
while u != v and s !="stop":
     if u < v:
         print("trop bas mon petit")
         u=int(input("allez, un autre"))
         s=input(" taper stop")
     if u > v:
         print("trop haut mon grand")
         u=int(input("allez, un autre"))
         s=str(input(" enter stop pour sortir"))
     if u == v:
         print("petit ou grand malin,Bravo!!!")
         u=(input("trouver le chiffre au hasard: "))
         s=input(" enter stop pour sortir")
if(u==v):
    print("win")
if(s=="stop"):
    print("au revoir")


## 4\.Exercice 4 : Des nombres en boucle
input("appuie entrer pour que je compte jusqu'a 100")
for r in range(101):
    print(r)

## Exercice5
print("exercice5")
for x in range(101):
    if x%2 == 0:
        print(int(x), "paire")
