## Quando se cria uma classe a partir de outra já existente
## essa nova classe (classe-filha) herda todos os metodos e atributos
## da classe original (classe-pai) isso recebe o nome de Herança.

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
        self.gas = 78

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

    def fill_gas_tank(self):
        '''
        Objetivo:
        Verificar qual a porcentagem de gasolina no tanque do carro.
        '''
        print('This car has ' + str(self.gas) + '% gasoline')
    
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


## Quando criamos a classe-filha, ela deve estar no mesmo arquivo
## que a classe-pai, e após a classe-pai.
            
class Battery():
    '''
    Objetivo:
    Uma tentativa simples de modelar uma bateria para um carro
    '''

    def __init__(self, battery_size=70):
        '''
        Objetivo:
        Inicializa os atributos da bateria.
        '''

        self.battery_size = battery_size
    
    def describe_battery(self):
        '''
        Objetivo:
        Exibe uma frase que descreve a capacidade da bateria.
        '''

        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    
    def get_range(self):
        '''
        Objetivo:
        Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria.
        '''

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

class EletricCar(Car): ## Deve ser incluido o nome da classe-pai entre os parenteses.
    '''
    Objetivo:
    Representa aspectos específicos de veículos elétricos.
    '''

    def __init__(self, make, model, year):
        '''
        Objetivo:
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        '''

        ## A função super(), ajuda o python a fazer ligação entre
        ## a classe-pai e fila, chamando o __init__() da classe-pai
        ## e concedendo acesso a todos os atributos.

        ## super -> superclasse -> classe-pai
        ## subclasse -> classe-filha
        

        super().__init__(make, model, year)
        
        ## Utilização de uma instancia da classe batery dentro da classe eletric car.
        ## Essa linha diz ao python para criar uma nova instancia da classe Baterry,
        ## armazenando essa instancia no atributo self.battery, acontecendo sempre
        ## que o metodo __init__ for chamado.
        self.battery = Battery() 
    
    def fill_gas_tank(self):
        '''
        Objetivo:
        Carros elétricos não têm tanque de gasolina.
        '''

        print("This car doesn't need a gas tank!")

my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()