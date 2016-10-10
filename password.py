#This is a simple password generator
# Imports

import random

def generator(complexity):
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
        word = word.translate(None, "'")
        word = word.title()
        password += word
        count += 1

    return password

print(generator(3))
