# M3C5 Assigment

# 1

cats = ['Josu', 'Olga', 'Kata']
for cat in cats:
    print(cat)

# 2

def suma(a, b, c):
    return(a + b + c)

print(suma(10, 10, 2))

# 3

suma = lambda a, b, c : a + b + c

print(suma(2, 2, 2))

# 4

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

presente = False

for personaje in lista_nombre:
    if personaje == nombre:
        presente = True

if presente:
    print('Presente en la lista')
else:
    print('No presente en la lista')
        
