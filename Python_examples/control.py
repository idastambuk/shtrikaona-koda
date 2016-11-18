#Usporedba brojeva unesenih putem konzole

x = int(raw_input('Unesite prvi broj: '))
print x

y = int(raw_input('Unesite drugi broj: '))
print y

if x==y:
    print 'Brojevi su jednaki'
elif x>y:
    print 'Prvi broj je veci od drugoga'
else:
    print 'Drugi broj je veci od prvoga'        