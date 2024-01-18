## Podemos modificar os atributos de uma instância diretamente
## ou escrever métodos que atualizem os atributos.

class Car():
    '''
    Objetivo:
    Uma tentativa simples de representar um carro.
    '''
    
    ## Podemos atribuir valores padrões a um atributo
    ## caso isso seja feito, não precisamos especificar um parametro.
    def __init__(self, make, model, year):
        '''
        Objetivo:
        Inicializa os atributos que descrever um carro.
        '''

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''
        Objetivo:
        Devolve um nome descriivo, formatado de modo elegante.
        '''

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        '''
        Objetivo:
        Exibe uma frase que mostra milhagem do carro.
        '''

        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    def update_odometer(self, mileage):
        '''
        Objetivo:
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro.
        '''
        
        ## Lógica para impedir que seja passado um valor menor do que já está armazenado.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''
        Objetivo:
        Soma a quatnidade especificada ao valor de leitura do hodômetro.
        '''
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
        
    

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Define de forma manual e direta o novo valor do atributo.
#my_new_car.odometer_reading = 23 

# Define de forma mais automatica por meio de método o valor do atributo.
my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_new_car.update_odometer(45)
my_new_car.read_odometer()

# Testando o incremental do metodo criado.
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

