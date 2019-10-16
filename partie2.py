##1\.Exercice 1 : True ou False ?
#Déclarer 2 variables de type String. L'une d'entre elles doit être vide.
#Ecrire un programme vérifiant si chacune des deux variables est vide ou non, et renvoyer la valeur (True ou False) dans le terminal selon le cas de figure.
#Pour cet exercice, vous devrez commencer à vous renseigner par vous-même sur les conditions en Python.

a = ""
b = "non vide"

nombrea = len(a)
nombreb = len(b)

if nombrea == 0:
    print(nombrea == 0)
else:
    print(nombrea == 0)

if nombreb == 0:
    print(nombreb == 0)
else:
    print(nombreb == 0)

## 2\.Exercice 2 : Calculer mon âge
#Réalisez un programme qui demande au visiteur l'année actuelle, son année de naissance puis calcule l'âge du visiteur et l'affiche dans un message à l'écran.
#Pour aller plus loin, demandez dans le terminal l'âge de la personne à côté de vous et afficher dans un message le cumul de vos deux âges.

Annee_actuelle = int(input("Annee actuelle ?:"))
Annee_de_naissance = int(input("votre  annee de naissance ?:"))
age = Annee_actuelle - Annee_de_naissance
print(age)
