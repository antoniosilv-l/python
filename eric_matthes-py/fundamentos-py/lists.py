##
## Trabalhando com listas

bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)

print(bicicletas[0]) ## Acessando um objeto da lista
print(bicicletas[0].title()) ## Formatando o objeto da lista
print(bicicletas[-1].title()) ## Acessando o ultimo objeto da lista

message = 'My First bicycle was a ' + bicicletas[0].title() + '.' ## Utilizando a concatenação para pegar um objeto da lista
print(message)

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos[0] = 'ducati'
print(motos)

##
## Acrescentando itens a uma lista existente ou a uma nova lista

motos.append('honda')
print(motos)

motos_v2 = []

motos_v2.append('honda')
motos_v2.append('yamaha')
motos_v2.append('suzuki') # O append serve para adicionar itens ao final da lista.

print(motos_v2)

motos_v2.insert(0, 'ducati') # O insert serve para adicionar itens na posição que desejar.
print(motos_v2)

del motos_v2[0] # Se a posição for conhecida é possivel remover um item da lista passando sua posição.
print(motos_v2)

popped_motos = motos_v2.pop() # a instrução pop sempre removerá o ultimo da lista e poderá ser armazenado o valor.
print(motos_v2)
print(popped_motos)

motos_v3 = ['honda', 'yamaha', 'suzuki']
last_owned = motos_v3.pop(1) # Também é possivel passar o indice da coluna para a função pop()
print('The last motorcycle i owned was a ' + last_owned.title() + '.')

motos_v4 = ['honda', 'yamaha', 'suzuki', 'ducati']
motos_v4.remove('ducati') # É possivel remover itens de uma lista passando também o valor, apagando apenas a primeira correspondencia do valor.
print(motos_v4)

##
## Ordenando itens dentro de uma lista.

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort() # Função utilizada para ordenar em ordem alfabetica permanentemente.
print(carros)

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort(reverse = True) # Função utilizada para ordenar em ordem alfabetica inversa permanentemente.
print(carros)

carros_v2 = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(carros_v2)

print('Here is the sorted list:')
print(sorted(carros_v2)) # Essa função ordena em ordem alfabetica de forma temporaria, também é possivel ordernar inversamente.

print('Here is the original list again:')
print(carros_v2)

carros_v3 = ['bmw', 'audi', 'toyota', 'subaru']
print(carros_v3)

carros_v3.reverse() # Aqui podemos mostrar de forma inversa a lista sem mexer na ordem alfabetica.
print(carros_v3)

print('Tamanho da lista de carros: ' + str(len(carros_v3)))

print('-----')

##
## Trabalhando com o for

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico)

print('-----')

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magico.title() + ".\n")

print('Thank you, everyone. That was a great magic show!')

print('-----')

##
## for com numeros

for value in range(1,6):
    print(value)

numeros = list(range(1,6)) ## é possivel converter um range de numeros diretamente em lista
print(numeros)

numeros_pares = list(range(2,11,2)) ## forma de exibir uma lista com numeros apenas pares.
print(numeros_pares)

quadrados = []
for value in range(1,11):
    quadrado = value**2 ## forma de criar um lista com quadrados perfeitos.
    quadrados.append(quadrado)

print(quadrados)

quadrados = []
for value in range(1,11):
    quadrados.append(value**2) ## forma mais resumidade de criar um lista com quadrados perfeitos.

print(quadrados)

quadrados = [value**2 for value in range(1,11)] ## exemplo de list comprehensions
print(quadrados)

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digitos)
print('Valor minimo da lista: ' + str(min(digitos)))
print('Valor maximo da lista: ' + str(max(digitos)))
print('Soma dos valores da lista: ' + str(sum(digitos)))

print('-----')

##
## Fatiando listas.

print('\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Lista original: ' + str(players))
print('Pegando um conjunto de dados do primeiro ao terceiro item: ' + str(players[0:3])) # Pegando um conjunto especifico de dados
print('Pegando um conjunto de dados até o quarto item: ' + str(players[:4])) # Pegando até o quarto item da lista
print('Pegando um conjunto de dados a partir do 2: ' + str(players[2:]))
print('Pegando um conjunto de dados começando do final: ' + str(players[-3:]))

print('\n')
print('Percorrendo uma lista for usando fatias...')
print('Here are the first three players on my team: ')
for player in players[:3]:
    print(player.title())

##
## Copiando listas.

print('\n')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print('-----')

##
## Tuplas
## Tuplas são listas que possuem dados imutaveis ao inves de colchetes usamos parenteses.

print('\n')

dimensions = (200, 50)
print('Original dimensions:')
#print(dimensions[0])
#print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)