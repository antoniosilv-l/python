## Valores de retorno
## São dados que foram processados dentro de uma função e são devolvidos.

def get_formatted_name(first_name, last_name):
    '''
    Objetivo:
    Formatar o nome fornecido do cliente.

    Parâmetros:\n
    first_name (String): Primeiro nome do cliente.
    last_name (String): Sobrenome do cliente.

    Retorno:
    full_name (String): Nome completo formatado para a primeira letras ser maiuscula.
    '''

    full_name = first_name + ' ' + last_name
    return full_name.title()

## Podemos também criar funções com argumentos opcionais.

def get_formatted_name1(first_name, last_name, middle_name=''):
    '''
    Objetivo:
    Formatar o nome fornecido do cliente.

    Parâmetros:\n
    first_name (String): Primeiro nome do cliente.
    middle_name (String): Nome do meio do cliente.
    last_name (String): Sobrenome do cliente.

    Retorno:
    full_name (String): Nome completo formatado para a primeira letras ser maiuscula.
    '''
    if middle_name:
        full_name = first_name + ' ' + middle_name  + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

def get_formatted_name2(first_name, last_name):
    '''
    Objetivo:
    Formatar o nome fornecido do cliente.

    Parâmetros:\n
    first_name (String): Primeiro nome do cliente.
    last_name (String): Sobrenome do cliente.

    Retorno:
    full_name (String): Nome completo formatado para a primeira letras ser maiuscula.
    '''

    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\Please tell me you name:')
    print('(enter "q" at any time to quit)')
    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name2(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')
    print('\n')