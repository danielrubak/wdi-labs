# Napisz funkcję szyfrującą podany tekst za pomocą szyfru podtawieniowym za pomocą danego alfabetu

import string
alphabet = dict(zip(string.ascii_lowercase, range(0,26)))
rev_alphabet = string.ascii_lowercase[::-1]
rev_alphabet = dict(zip(rev_alphabet, range(0,26)))

#text = str(input("Podaj napis: "))
text = "Cokolwiek Do Zakodowania: "
text = text.lower()
print("Przed zakodowaniem: ", text)

def podstawieniowy(text,code):
    encrypted = ""
    for i in text:
        index = alphabet.get(i)
        if index == None:
            encrypted += " "
        else:
            for alpha, value in code.items():
                if value == index:
                    encrypted += alpha
    return encrypted
enc = podstawieniowy(text, rev_alphabet)
print("Zakodowany: ", enc)

def dePodstawieniowy(text, code):
    decrypted = ""
    for i in text:
        index = code.get(i)
        if index == None:
            decrypted += " "
        else:
            for alpha, value in alphabet.items():
                if value == index:
                    decrypted += alpha
    return decrypted

result = dePodstawieniowy(enc, rev_alphabet)
print("Po odkodowaniu: ", result)
