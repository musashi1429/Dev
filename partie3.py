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
while user != "D":
    print("entrer votre age")
    Age = int(input())
    if Age <= 0:
        print("merci d'indiquer un age réel")
    elif Age >= 21:
        print("vous étes autorisé a accéder au portail")
    elif Age%2 == 0:
        print("age pair,mhh,chanceux!!!")
    user = str(input("si vous voulez quittez tapez D "))
