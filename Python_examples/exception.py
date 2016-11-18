#Primjer hvatanja greske

try:
    x = int(raw_input('Unesite broj: '))
except ValueError:
    print 'Oops! Ovo nije dobar broj'
else:
    print 'Ovo je ispravan broj'

#x = int(raw_input('Unesite broj: '))          