from judete import judete
import random
import string

def roplategen():
    nrjudet = random.randint(1, 42) # Generate random judet from dictionary.

    nr = random.randint(1, 99)  # Generate random two digit number.
    if nr < 10: # If the number only has one digit, add a leading zero.
        nr = str(nr) # zfill() requires nr to be a string.
        #              This shouldn't cause any problems (hopefully).
        nr = nr.zfill(2)

    if nrjudet == 1: # If the judet is Bucharest, generate a three digit
        #              number instead.
        nr = random.randint(1,999)
        if nr < 10:
            nr = str(nr)
            nr = nr.zfill(3)

    ltr1 = random.choice(string.ascii_letters).upper()  # Generate three
    ltr2 = random.choice(string.ascii_letters).upper()  # random uppercase
    ltr3 = random.choice(string.ascii_letters).upper()  # letters.

    nr = str(nr) # If nr isn't a string, make it one to enable the concatenation.
    print(judete.get(nrjudet) + nr + ltr1 + ltr2 + ltr3)