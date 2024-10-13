'''
Trabalhando com listas.
- list, list comprehensions
- Title, Upper e Lower Case
- sort, sorted e reverse
- len
- for
- tuplas
'''

print("---- Lists ----")
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)


print("---- Acessando, Formatadando e Concatenando ----")
print(bicicletas[0])
print(bicicletas[0].title())
print(bicicletas[-1].title())

message = 'My First bicycle was a ' + bicicletas[0].title() + '.'
print(message)

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos[0] = 'ducati'
print(motos)


print("---- Incluindo Itens ----")
'''
- O append serve para adicionar itens ao final da lista.
- O insert serve para adicionar itens na posição que desejar.
'''
motos.append('honda')
print(motos)

motos_v2 = []

motos_v2.append('honda')
motos_v2.append('yamaha')
motos_v2.append('suzuki')

print(motos_v2)

motos_v2.insert(0, 'ducati')
print(motos_v2)


print("---- Removendo Itens ----")
'''
- Se a posição for conhecida é possivel remover um item da lista passando sua posição.
- A instrução pop sempre removerá o ultimo da lista e poderá ser armazenado o valor.
-- Também é possivel passar o indice da coluna para a função pop()
- É possivel remover itens de uma lista passando também o valor, apagando apenas a primeira correspondencia do valor.
'''
del motos_v2[0]
print(motos_v2)

popped_motos = motos_v2.pop()
print(motos_v2)
print(popped_motos)

motos_v3 = ['honda', 'yamaha', 'suzuki']
last_owned = motos_v3.pop(1) # 
print('The last motorcycle i owned was a ' + last_owned.title() + '.')

motos_v4 = ['honda', 'yamaha', 'suzuki', 'ducati']
motos_v4.remove('ducati') 
print(motos_v4)


print("---- Ordenando Itens ----")
'''
- sort, Função utilizada para ordenar em ordem alfabetica permanentemente.
-- "reverse = True", Função utilizada para ordenar em ordem alfabetica inversa permanentemente.
- sorted, Função ordena em ordem alfabetica de forma temporaria, também é possivel ordernar inversamente.
- reverse, Função que mostrar de forma inversa a lista sem mexer na ordem alfabetica.
'''
carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort() 
print(carros)

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort(reverse = True)
print(carros)

carros_v2 = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(carros_v2)

print('Here is the sorted list:')
print(sorted(carros_v2))

print('Here is the original list again:')
print(carros_v2)

carros_v3 = ['bmw', 'audi', 'toyota', 'subaru']
print(carros_v3)

carros_v3.reverse()
print(carros_v3)


print("---- Tamanho da Lista ----")
print('Tamanho da lista de carros: ' + str(len(carros_v3)))


print("---- Trabalhando com For + Lista ----")
magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico)

print('-----')

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magico.title() + ".\n")

print('Thank you, everyone. That was a great magic show!')


print("---- Trabalhando com For + Numeros ----")
'''
- É possivel converter um range de numeros diretamente em lista
'''
for value in range(1,6):
    print(value)

numeros = list(range(1,6))
print(numeros)

'''
- forma de exibir uma lista com numeros apenas pares.
'''
numeros_pares = list(range(2,11,2))
print(numeros_pares)

'''
- forma de criar um lista com quadrados perfeitos.
-- forma mais resumidade de criar um lista com quadrados perfeitos.
'''
quadrados = []
for value in range(1,11):
    quadrado = value**2
    quadrados.append(quadrado)

print(quadrados)

quadrados = []
for value in range(1,11):
    quadrados.append(value**2)

print(quadrados)


'''
- list comprehensions
'''
quadrados = [value**2 for value in range(1,11)]
print(quadrados)

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digitos)
print('Valor minimo da lista: ' + str(min(digitos)))
print('Valor maximo da lista: ' + str(max(digitos)))
print('Soma dos valores da lista: ' + str(sum(digitos)))


print("---- Fatiando Listas ----")
print('\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Lista original: ' + str(players))
print('Pegando um conjunto de dados do primeiro ao terceiro item: ' + str(players[0:3]))
print('Pegando um conjunto de dados até o quarto item: ' + str(players[:4]))
print('Pegando um conjunto de dados a partir do 2: ' + str(players[2:]))
print('Pegando um conjunto de dados começando do final: ' + str(players[-3:]))


print("---- Fatiando Listas + For ----")
print('Here are the first three players on my team: ')
for player in players[:3]:
    print(player.title())


print("---- Copiando Listas ----")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("---- Tuplas ----")
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
