#This is a simple password generator
# Imports

import random
import sys

def password_gen(complexity):
    #This function generate the string with the password

    #We open the local dictionary (on Linux systems)
    word_file = '/usr/share/dict/words'
    words = open(word_file).read().splitlines()

    #We create the container variable to add the words and a count variable for our loop
    password = ""
    count = 0

    #We pick 3 of them and add it to the container
    while count < complexity:
        word = str(random.choice(words))
        #add a method to remove the element from the array , to avoid duplication
        word = word.translate(None, "'")
        word = word.title()
        password += word
        if count != complexity-1:
            password += "|"
        count += 1

    return password

def options_gen(complexity):
    options = []
    count = 0

    while count < 3:
        password=password_gen(complexity)
        options.append(password)
        count += 1

    return options

def iteraction():
    #This function interacts with the user and use the generator function
    complexity = int(input("Que tantas palabras debe de tener el password? "))
    print("Tus 3 opciones son:")
    options=options_gen(complexity)
    print(options)
    election=input("Escribe el numero de la opcion deseada y aprieta enter ")
    print("Tu password es: "+str(options[election-1]))
    size = len(options[election-1])
    print("El numero de caracteres del password es: "+str(size))

if len(sys.argv) >= 2:
    foo = str(sys.argv[1])
else:
    foo = ""

if foo == "options":
    iteraction()
else:
    quick=password_gen(2)
    print(quick)
    print("El numero de caracteres del password es: "+str(len(quick)))
