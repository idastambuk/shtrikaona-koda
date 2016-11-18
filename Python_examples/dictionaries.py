#Primjer koristenja rjecnika

user = {'id': 1, 'name': 'Ivan', 'age': 30}
print user

user['age'] = 35
print user

user['height'] = 180 #dodavanje novog key-value para
print user

print user.keys() #vraca sve keyeve
print user.values() #vraca sve vrijednosti