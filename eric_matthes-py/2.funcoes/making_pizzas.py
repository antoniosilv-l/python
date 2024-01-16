## Módulos, são arquivos python que contém blocos de funções
## é extremamente valido quando você quer evitar de reprtir funções
## ou até compartilhar funções com outras pessoas.

## Módulos podem ser importados de duas formas, ou todas as funções
## ou apenas a função que queremos utilizar.

## Podemos ainda atribuir apelidos (alias) a importações totais ou de funções.
## Evitando que o código ou nome entre em conflito.
## Ou também podemos importar tudo que tem dentro do módulo.

#from modulos.pizza import * ## Importando todas as funções sem a necessidade de utilizar a notação de '.'
#import modulos.pizza as pizza ## Importando todos as funções criadas.
from modulos.pizza import make_pizza_pls as mp ## Importando apenas a função desejada.

#pizza.make_pizza_pls(16, 'pepperoni')
#pizza.make_pizza_pls(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')