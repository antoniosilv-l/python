## Caso não seja possivel saber quantos argumentos será passado
## para uma função com antecedencia, python fornece uma opção
## que permite a função receber quantos argumentos forem fornecidos.

## O asterisco no nome do parâmetro, diz a python para criar uma
## tupla vazia.

def make_pizza(*toppings):
    '''
    Objetivo:
    Apresenta a pizza que testamos prestes a preparar.

    Parâmetros:\n
    toppings (tupla): Sabores de pizzas.
    '''
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

## É possivel criar funções que aceitem tanto argumentos posicionais
## quanto argumentos arbitrários, para isso é necessario, passar
## o argumento arbitrário por ultimo.

def make_pizza_pls(size, *toppings):
    '''
    Objetivo:
    Mostrar todos os modelos impressos.

    Parâmetros:\n
    size (int): Tamanho da pizza
    toppings (tupla): Sabores de pizzas.
    '''

    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza_pls(16, 'pepperoni')
make_pizza_pls(12, 'mushrooms', 'green peppers', 'extra cheese')
