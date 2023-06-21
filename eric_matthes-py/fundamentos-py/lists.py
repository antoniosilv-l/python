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