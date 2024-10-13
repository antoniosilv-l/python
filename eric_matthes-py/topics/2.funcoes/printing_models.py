## Podemos realizar modificações nas listas ao passar para uma função
## toda alteração sera permanente.

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)

# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)

## Reorganizando código em funções

def print_models(unprinted_designs, completed_models):
    '''
    Objetivo:
    Simular a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.

    Parâmetros:\n
    unprinted_designs (list): Lista com design ainda não impressos.
    completed_models (list): Lista com design que já foram impressos.
    '''

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)

        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''
    Objetivo:
    Mostrar todos os modelos impressos.

    Parâmetros:\n
    completed_models (list): Lista com design que já foram impressos.
    '''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

## Ao chamar uma lista passando '[:]' após o seu nome, faz com que
## o python crie um copia da lista orignal, e não aplique nenhuma
## mudança na lista original.
##
## Porém esse uso não é o mais performatico, é sempre bom passar
## a lista original, e apenas passar a copia se for um motivo
## muito específico.
## Pois ao passar a copia se usa tempo e memória para criar 
## a copia.