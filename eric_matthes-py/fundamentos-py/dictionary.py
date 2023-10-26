## Introdução a utilização de dicionarios em python.

print('----')
print('Exemplo de dicionario, personagens de um jogo.')

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

## Podemos armazenar informações em outras variaveis.
print('----')
print('Utilizando informações de um dicionario.')

new_points = alien_0['points']
print('You Just earned ' + str(new_points) + ' points!')

## Acrescentando novos itens ao dicionario
print('----')
print('Incluindo novos itens ao dicionario.')

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

## Modificando itens de um dicionario.
print('----')
print('Modificando itens do dicionario.')

alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0 = {'color': 'yellow'}
print('The alien is now ' + alien_0['color'] + '.')

print('\n')
print('Outro exemplo ...modificando itens do dicionario.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print('Original x-position: ' + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))

## Removendo itens de um dicionario
print('----')
print('Removendo itens de um dicionario.')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

## Continuação sobre armazenamento de dados em dicionario
print('----')
print('Evoluindo o dicionario.')

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_language['sarah'].title() + '.')

## Percorrendo um dicionario com um laço
print('----')
print('Laço + dicionario.')

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print('----')
print('Outro exemplo, Laço + dicionario.')

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

## Percorrendo todas as chaves de um dicionario.
print('----')
print('Percorrendo as chaves de um dicionario.')

for name in favorite_language.keys():
    print(name.title())

print('----')
print('Exibindo dados para apenas quem permitirmos.')

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(' Hi ' + name.title() + ', I see your favorite language is ' + favorite_language[name].title() + '!')

if 'erin' not in favorite_language.keys():
    print('\nErin, please take our poll!')

## Ordenando as chaves
print('----')
print('Ordenando os itens exibidos de um dicionario.')

for name in sorted(favorite_language.keys()):
    print(name.title() + ', thank you for taking the poll.')

## Percorrendo todas os valores de um dicionario.
## A utilização da função set() retira qualquer duplicidade que existir.
print('----')
print('Exibindo os valores de um dicionario.')

print('The following languages have been mentioned: (Duplicidade)')

for language in favorite_language.values():
    print(language.title())

print('\nThe following languages have been mentioned: (Sem Duplicidade)')

for language in set(favorite_language.values()):
    print(language.title())

