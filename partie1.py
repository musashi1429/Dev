#ex 1 afficher "hello world"
print ("hello world")
variable = "hello world"
print(variable)

#ex 2 afficher resultat
print(3*3, 4+9+78, 12-7, 5+4)

try:
    print(12/0)
except ZeroDivisionError:
    print("pas divisible par 0")


# ex 3 communiqué avec l'ordinateur
nom = input("merci d'indiquer votre nom")
print("bienvenue" +""+ nom)
