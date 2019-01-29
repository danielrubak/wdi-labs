import string
s = str(input('Podaj napis: '))

def cezar(text, shift):
    encrypted = ""
    for i in text:
        if (ord(i)+shift>90 and ord(i)+shift<94) or ord(i)+shift>122:
            encrypted += chr(ord(i) + shift - 26)
        elif ord(i)==32:
            encrypted += chr(ord(i))
        else:
            encrypted += chr(ord(i) + shift)
    return encrypted

def deCezar(text, shift):
    decrypted = ""
    for i in text:
        if (ord(i)-shift>93 and ord(i)-shift<97) or (ord(i)-shift<65 and ord(i) != 32):
            decrypted += chr(ord(i) - shift + 26)
        elif ord(i) == 32:
            decrypted += chr(ord(i))
        else:
            decrypted += chr(ord(i) - shift)
    return decrypted

enc = cezar(s, 3)
print(enc)
dec = deCezar(enc, 3)
print(dec)
