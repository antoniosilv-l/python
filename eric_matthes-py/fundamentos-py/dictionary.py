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


## Dicionarios Aninhados
print('----')
print('Criando uma lista de dicionarios.')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('----')
print('Criando varios itens de um dicionario de uma vez.')

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print('----')
print('Alterando alguns itens de um dicionario.')

print('Total number of aliens: ' + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15        

for alien in aliens[0:5]:
    print(alien)
print('...')

## Lista dentro de um dicionario
print('\n----')
print('Listas dentro de dicionarios.')

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You ordered a ' + pizza['crust'] + '-crust pizza' + ' with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

print('----')
print('Outro exemplo.')

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_language.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

print('----')
print('Outro exemplo, aperfeiçoado.')

for name, languages in favorite_language.items():
    if len(languages) == 1:
        for language in languages:
            print('\n' + name.title() + "'s favorite language is " + language.title())
    else:
        print('\n' + name.title() + "'s favorite language are:")
        for language in languages:
            print('\t' + language.title())

## Dicionario dentro de dicionario.
print('\n----')
print('Dicionarios dentro de dicionarios.')

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())