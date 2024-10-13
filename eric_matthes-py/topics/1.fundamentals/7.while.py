'''
Tabralhando com While
- while
- input
'''
# print("---- receber dados que um usuario digitar. ----")
# print('Exemplo de input de dados.')

# message  = input('Tell me something, and i will repeat it back to you: ')
# print(message)

# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += '\nWhat is yout first name? '

# name = input(prompt)
# print('\nHello, ' + name + '!')

# height = input('How tall are you, in inches? ')
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# print("---- Testando se um variavel é impar ou par. ----")
'''
- Utilizamos um operador de módulo (%), ele divide um número por outro e devolve o resto.
'''
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print('\nThe number ' + str(number) + ' is even.')
# else:
#     print('\nThe number ' + str(number) + ' is odd.')


# print("---- executando durante um tempo, ou enquanto uma determinada ----")
'''
- Enquanto a condição for verdadeira.
'''
# current_number = 1
# while current_number <= 5:
#    print(current_number)
#    current_number += 1

# prompt = "\nTell me something, and i will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# print("---- Utilização de uma variavel booleano para continuar ou parar o programa. ----")
# active = True
# while active:
#    message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)

# print("---- Usando o break para encerrar o programa e sair do laço. ----")
'''
- Também é possivel usar o break dentro de um for.
'''
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#    city = input(prompt)

#    if city =='quit':
#        break
#    else:
#        print("I'd love to go to " + city.title() + "!")


# print("---- Utilizando o continue para retornar o inicio ----")
# current_number = 0
# while current_number < 10:
#     current_number += 1
    
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# print("---- Transferindo dados de uma lista para outra utilizando o while ----")
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print('Verifyng user: ' + current_user.title())
#     confirmed_users.append(current_user)

# print('\n The following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# print("---- Removendo todas as instancias de uma lista com o while ----")
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


# print("---- Armazenando dados de um input em um dicionario----")
responses = {}

'''
- Define uma flag para indicar que a enquete está ativa
'''
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

print('\--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')