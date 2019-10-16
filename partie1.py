#ex 1 afficher "hello world"
print ("hello world")
variable = "hello world"
print(variable)

#ex 2 afficher resultat
print(3*3, 4+9+78, 12-7, 5+4)

try:
    print(12/0)
except ZeroDivisionError:
    print("12 n'est pas divisible par 0")


# ex 3 communiqué avec l'ordinateur
B = input("merci d'indiquer votre nom ")
print("bienvenue" +" "+ B)

#ex 4 Nom et prénom
nom = "kassama"
prenom = "fally"
print("bonjour" +" "+nom+" "+prenom)
print("bonjour {} {}".format(nom, prenom))

#ex 5  Modifier son type String en type Integer
MyNumber = "123"

MyNumber = int(MyNumber)
print(type(MyNumber))

nom = str(nom)
prenom = str(prenom)

# ex 6  Ecrire un programme permettant de mettre en majuscule le contenu d'une String donnée par l'utilisateur
print(nom.upper())
print(prenom.lower())
