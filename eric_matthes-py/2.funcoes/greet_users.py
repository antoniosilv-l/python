## Lista para função
## A utilização da passagem de listas para uma função é comum
## e não só facilita como deixa mais eficiente o processo.

def greet_users(names):
    '''
    Objetivo:
    Exibir uma saudação para cada usuário da lista.

    Parâmetros:\n
    names (list): Lista com nomes de usuários.
    '''
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

#usernames = ['hannah', 'ty', 'margot']
#greet_users(usernames)
    
    