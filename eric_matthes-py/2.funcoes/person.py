## Funções podem retornar qualquer tipo de valor que seja necessário.

def build_person(first_name, last_name):
    '''
    Objetivo:
    Formatar o nome fornecido do cliente.

    Parâmetros:\n
    first_name (String): Primeiro nome do cliente.
    last_name (String): Sobrenome do cliente.

    Retorno:
    person (Dict): Dicionario de dados contendo informações do cliente.
    '''
        
    person = {'first': first_name, 'last': last_name}
    return person

def build_person_pls(first_name, last_name, age=''):
    '''
    Objetivo:
    Formatar o nome fornecido do cliente.

    Parâmetros:\n
    first_name (String): Primeiro nome do cliente.
    last_name (String): Sobrenome do cliente.

    Retorno:
    person (Dict): Dicionario de dados contendo informações do cliente.
    '''
        
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person_pls('jimi', 'hendrix', age=27)
print(musician)