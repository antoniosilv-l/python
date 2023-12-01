##
## A função input serve para receber dados que um usuario digitar.

print('----')
print('Exemplo de input de dados.')

#message  = input('Tell me something, and i will repeat it back to you: ')
#print(message)

#name = input('Please enter your name: ')
#print('Hello, ' + name + '!')

prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is yout first name? '

#name = input(prompt)
#print('\nHello, ' + name + '!')

#height = input('How tall are you, in inches? ')
#height = int(height)

#if height >= 36:
#    print("\nYou're tall enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")

##
## Testando se um variavel é impar ou par.
## Utilizamos um operador de módulo (%), ele divide um número por outro e devolve o resto.

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#
#if number % 2 == 0:
#    print('\nThe number ' + str(number) + ' is even.')
#else:
#    print('\nThe number ' + str(number) + ' is odd.')

#
# O laço while irá continuar executando durante um tempo, ou enquanto uma determinada
# condição for verdadeira

#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1

prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

## Utilização de uma variavel booleano para continuar ou parar o programa.

#active = True
#while active:
#    message = input(prompt)
#
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

## Usando o break para encerrar o programa e sair do laço.
## Também é possivel usar o break dentro de um for.

#prompt = "\nPlease enter the name of a city you have visited: "
#prompt += "\n(Enter 'quit' when you are finished.) "
#
#while True:
#    city = input(prompt)
#
#    if city =='quit':
#        break
#    else:
#        print("I'd love to go to " + city.title() + "!")

## Utilizando o continue para retornar o inicio

current_number = 0
while current_number < 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue

    print(current_number)