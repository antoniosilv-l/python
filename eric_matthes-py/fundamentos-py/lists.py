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