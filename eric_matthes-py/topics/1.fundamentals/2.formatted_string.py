'''
Trabalhando com String
- title
- Lower Case
- Upper Case
- Concatenação
- Tabulação
- Strip (Remoção de espaços)
- Função str() (Transformação em string)
'''

print("---- Title, Upper e Lower Case ----")
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())


print("---- Concatenação ----")
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)


print("---- Concatenação + Funções ----")
print("Hello, " + full_name.title() + '!')


print("---- Tabulação ----")
print('Lista de compras: \n\tArroz\n\tFeijão\n\tCarne')


print("---- Strip ----")
espaco_direita = 'Espaço a direita '
espaco_direita = espaco_direita.rstrip()
print(espaco_direita)

espaco_esquerda = ' Espaço a esquerda'
espaco_esquerda = espaco_esquerda.lstrip()
print(espaco_esquerda)

espaco_ambos_lados = ' Espaço em ambos os lados '
espaco_ambos_lados = espaco_ambos_lados.strip()
print(espaco_ambos_lados)


print("---- str() ----")
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)
