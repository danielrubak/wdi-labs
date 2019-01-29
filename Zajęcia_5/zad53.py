# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:46:32 2017

@author: rubadani
"""

x = float(input("Podaj współrzędną x: "))
y = float(input("Podaj współrzędną y: "))4

p = x*y

if p>0:
    if y<0:
        print("III ćwiartka")
    else:
        print("I ćwiartka")
elif p<0:
    if y<0:
        print("IV ćwiartka")
    else:
        print("II ćwiartka")
else:
    if y!=0:
        print("Oś OY")
    elif x!=0:
        print("Oś OX")
    else:
        print("Środek układu")
    