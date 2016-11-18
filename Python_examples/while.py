#Primjer s while petljom

print 'Unesite brojeve za racunanje:'
print 'Za prekid izracuna upisite 0'
suma = 0

broj = int(raw_input('Upisite broj: '))

while(broj!=0):
    suma += broj
    print suma
    broj = int(raw_input('Upisite broj: '))
    
    if(broj==2):
        break

print 'Konacna suma'
print suma    