##
## IF é uma instrução que permite analisar o estado atual de um programa e responder
## de forma apropriada a esse estado

print('Exemplo de if, BMW ficará maiuscula e o resto apenas a inicial.')

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('----')
print('\n')

## Teste condicionais
## Verificação de igualdade
car = 'audi'

print('Testando se a variavel é igual a string passada. String: audi')
print(car == 'bmw')
print(car == 'audi')

##
print('----')
car = 'Audi'

print('''
Testando se a variavel é igual a string passada independente se é maiusculo ou não. 
String: audi
''')
print(car.lower() == 'bmw')
print(car.lower() == 'audi')

##
print('----')
print('Testando se a variavel é igual a int passada. int: 18')
age = 18
print(age == 18)

print('Testando se a variavel é diferente da int passada. int: 17')
age = 17
if age != 42:
    print('That is not the corret answer. Please try again!')

## Verificação de diferença
print('----')

print('Testando se a variavel é diferente a string passada. String: mushrooms')
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!!')

## Verificação se um item já está dentro de uma lista
print('----')

print('Verificando se um item já está dentro de uma lista.')
requested_topping = ['mushrooms', 'onions', 'pineapple']

print('Verificando se o item "mushrooms" já está dentro da lista: ' + str('mushrooms' in requested_topping))
print('Verificando se o item "pepperoni" já está dentro da lista: ' + str('pepperoni' in requested_topping))

## Verificação se um item não está dentro de uma lista
print('----')

print('Verificando se um item não está dentro de uma lista.')
print('Verificando seo usuario foi banido: ')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish')