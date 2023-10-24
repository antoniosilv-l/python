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

## Começando a trabalhar com if-else
print('----')
print('Testando se a idade já permite votar. Começo do if-else')
age = 17

if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('please register to vote as soon as you turn 18!')

## Começando a trabalhar com if-elif-else
## Essa tecnica é muito util quando apenas um dos testes deve ser True.
print('----')
print('Testando valores pagos em um parque. Começo do if-elif-else')
age = 67

# if age < 4:
#     print('You admission cost is $0.')
# elif age < 18:
#     print('You admission cost is $5.')
# else:
#     print('You admission cost is $10.')

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
# else:
#     price = 5

print('You admission cost is $' + str(price) + '.')

## Começando a trabalhar com if encadeado.
## Essa tecnica é muito util quando mais de um teste deve ser True
print('----')
print('Testando itens de uma pizza. Utilizando if encadeados.')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished making your pizza!')

## IF + Listas.
## Unindo essas duas tenicas é possivel deixar o código mais versatil.
print('----')
print('Testando itens de uma pizza. Começo do if  + listas')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')

## Checando se a lista está vazia.
print('----')
print('Testando se a lista de itens de uma pizza está vazia. Continuação do if  + listas')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza?')
else:
    print('Are you sure you want a plain pizza?')

## Usando duas listas.
print('----')
print('Testando duas listas de itens de uma pizza. Continuação do if  + listas')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza!')