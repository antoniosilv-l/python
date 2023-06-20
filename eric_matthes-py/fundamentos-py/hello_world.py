##
## Primeiro Hello World da lingagem.

print("Hello Python World!")

##
## Trabalhando com Variáveis

message = 'Hello Python World! (Com Variáveis)'
print(message)

##

message = 'Hello Python Crash Course World!'
print(message)

##
## Trabalhando com Strings

name = 'ada lovelace'
print(name.title()) ## Deixa as primeiras letras maiúsculas.
print(name.upper()) ## Deixa as todas as letras maiúsculas.
print(name.lower()) ## Deixa as todas as letras minúsculas.

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name ## Concatenação de strings.
print(full_name)

print("Hello, " + full_name.title() + '!') ## Concatenação de strings e utilização de função.

print('Lista de compras: \n\tArroz\n\tFeijão\n\tCarne') ## Utilização de tabulação

espaco_direita = 'Espaço a direita '
espaco_direita = espaco_direita.rstrip() ## Remoção de espaço em branco a direita
print(espaco_direita)

espaco_esquerda = ' Espaço a esquerda'
espaco_esquerda = espaco_esquerda.lstrip() ## Remoção de espaço em branco a esquerda
print(espaco_esquerda)

espaco_ambos_lados = ' Espaço em ambos os lados '
espaco_ambos_lados = espaco_ambos_lados.strip() ## Remoção de espaço em branco em ambos lados
print(espaco_ambos_lados)