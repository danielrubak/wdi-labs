# Napisz funkcję która usunie z podanego tekstu wszystkie znaku nie będące literami, oraz zmieni wszystkie litery na małe.
import string

text = str(input('Podaj napis: '))
text = text.lower()
text = ''.join([i for i in text if not i.isdigit()])
print(text)
