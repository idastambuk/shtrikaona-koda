#Primjer manipuliranja s nizom znakova

poruka = 'Hello world'

print poruka[0]
print poruka[0:5]
print poruka[-2]

print len(poruka) #duljina stringa
print poruka.lower() #pretvori sve u mala slova
print poruka.count('l') #prebroji koliko puta se javlja 'l'

poruka = poruka.replace('H', 'h', 1)
print poruka

