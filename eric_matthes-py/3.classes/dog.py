## Classes representam entidades e situações
## essa é uma das ideias da programação orientada a objetos
## uma classe defini o comportamento geral que toda uma categoria
## de objetos pode ter.
## A chamada a uma classe recebe um nome de instancia.

## Por conversão quando tratamos de classes a primeira letra
## sempre deve ser maiuscula.
class Dog():
    '''
    Objetivo:
    Classe simples criada para modelagem de um cachorro.
    '''

    ## Uma função que faz parte de uma classe é um método.
    ## __init__ é um método especial que python executa
    ## automaticamente sempre que criamos uma nova instancia.
    ## os underscore previnem que utilizemos nomes default de metodos.

    ## Parametro self é obrigatorio na definição do método
    ## servindo de referencia a propria instancia de forma automatica
    ## dando acesso aos atributos e metodos da classe a instancia individual.

    ## Todas as variaveis com o prefixo self, ficarão disponiveis
    ## a todos os metodos da classe.
    ## variaveis como essas, são chamadas de atributos.
    def __init__(self, name, age):
        '''
        Objetivo: 
        Inicializar os atributos name e age.
        '''

        self.name = name
        self.age = age

    def sit(self):
        '''
        Objetivo:
        Simular um cachorro sentando em resposta a um comando.
        '''

        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''
        Objetivo:
        Simular um cachorro rolando em resposta a um comando.
        '''

        print(self.name.title() + ' rolled over!')


## Por conversão a chamada da classe atraves da instacia individual
## é escrita de forma minuscula, enquanto a classe possui a primeira
## letra maiuscula, dessa forma conseguimos entender melhor.
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + '.')
print('Your dog is ' + str(your_dog.age) + ' years old.')
your_dog.sit()
your_dog.roll_over()