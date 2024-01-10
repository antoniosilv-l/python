## Funções, são blocos de códigos criados para realizar uma tarefa específica.

## Criando uma função simples para saudações.
### def: informa ao python que estamos definindo uma função.

def greet_user():
    '''
    Objetivo:
    Exibir uma saudação simples.
    '''

    print('Hello!')

greet_user()

def greet_user_pls(username):
    '''
    Objetivo:
    Exibir uma saudação simples, recebendo uma variavel.

    Parâmetros:\n
    username (String): Nome do usuário.
    '''

    print('Hello, ' + username.title() + '!')

greet_user_pls('mrs.python')



