## Argumentos posicionais
### Acontece quando cada argumento da chamada da função está na mesma
### ordem dos parametros da função.

def describe_pet(animal_type, pet_name):
    '''
    Objetivo:
    Exibir o tipo e o nome do animal de estimação.

    Parâmetros:\n
    animal_type (String): Tipo do animal de estimação.
    pet_name (String): Nome do animal de estimação.
    '''

    print('\nI have a ' + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'lara')
describe_pet('cat', 'claudio')

## Argumentos nomeados / keyword argument
### é passado um par nome-valor para a função, associando automaticamente
### o argumento ao valor.

describe_pet(animal_type='hamster', pet_name='harry')

## Valores Default
### São interessantes caso seja necessario simplificar a chamada
### da função, podendo na chamada omitir um dos parametros.
### Ao optar por colocar um valor default, é necessario mudar o posicionamento
### dos parametros, pois não é mais necessario especificar o tipo do animal
### e com isso é permitido que python continue a interpretar os argumentos posicionais
### corretamente.

def describe_pet_pls(pet_name, animal_type='dog'):
    '''
    Objetivo:
    Exibir o tipo e o nome do animal de estimação.

    Parâmetros:\n
    animal_type (String): Tipo do animal de estimação, valor padrão é 'dog'.
    pet_name (String): Nome do animal de estimação.
    '''

    print('\nI have a ' + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_pls(pet_name='rodolfo')
