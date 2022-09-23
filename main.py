from TP2 import *

def palindrome_verif():
    mot=str(input("Veuillez rentrer un mot : "))

    if palindrome(mot) == True:
        print(f"Le mot '{mot}' est un palindrome")
    else:
        print(f"Le mot '{mot}' n'est pas un palindrome")

# palindrome_verif()

print(crypter("J'ai une adorable copine"))