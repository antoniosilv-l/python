## Há a possibilidade de não sabermos com antecedencia qual tipo
## de informações será passado para a função;
## Para isso podemos aceitar um número arbitrário de argumentos
## aceitando pares chave-valor;
## É necessario passar asteriscos duplos antes do parametro para que
## python consiga criar um dicionario;

def build_profile(first, last, **user_info):
    '''
    Objetivo:
    Construir um dicionário contendo tudo que sabemos sobre um usuário

    Parâmetros:\n
    first (string): Primeiro nome do usuário.
    last (string): Sobrenome do usuário.
    user_info (tupla): Par de chave-valor, com informações que forem necessarias.
    '''

    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_profile = build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics'
)

print(user_profile)