#Primjer koristenja for petlje

colors = ['blue', 'red', 'green']

for color in colors:
    print color

users = [
    {'id': 1, 'name': 'Martina'}, 
    {'id': 2, 'name': 'Eva'}, 
    {'id': 3, 'name': 'Jelena'}
    ]

for user in users:
    print 'User: '
    print user['id']
    print user['name']

for number in range(0, 10):
    if (number%2 == 1):
        continue #ispisi samo neparne brojeve
    print number    