import string

def zKluczem(text, key):
    encrypted = ''
    k = 0
    for i in text:
        j = key[k%len(key)]
        diff = ord(j) - 96
        if ord(i) == 32:
            encrypted += '_'
        elif ord(i) + diff <= 122 and (ord(i) + diff != 32):
            encrypted += chr(ord(i)+diff)
        else:
            encrypted += chr(ord(i)+diff-26)
        k += 1
    return encrypted

def deZKluczem(text, key):
    decrypted = ''
    k = 0
    for i in text:
        j = key[k%len(key)]
        diff = ord(j) - 96
        if ord(i) == 95:
            decrypted += ' '
        elif ord(i)-diff>=97:
            decrypted += chr(ord(i)-diff)
        else:
            decrypted += chr(ord(i)-diff+26)
        k += 1
    return decrypted

text = 'Cokolwiek Do Zakodowania'
text = text.lower()
print(text)
enc = zKluczem(text, 'jestemzajebisty')
print(enc)
dec = deZKluczem(enc, 'jestemzajebisty')
print(dec)
