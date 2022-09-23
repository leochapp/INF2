# Exercice 1

def palindrome(mot):
    mot = mot.lower()
    if len(mot) == 0:
        return True
    else:
        if mot[0] == mot[len(mot)-1]:
            return palindrome(mot[1:len(mot)-1])
        else:
            return False


# Exercice 2

def crypter(ch):
    newch = ""
    for i in ch:
        if i.isnumeric() == True:
            nb = i+1
            nb = chr(nb)
            newch += nb
        if i.isalpha() == True:
            nb = ord(i)
            if nb == 122:
                nb = 97
            elif nb == 90:
                nb = 65
            else:
                nb += 1
            nb=chr(nb)
            newch += nb
        else:
            newch += i
    return newch

# Exercice 3

