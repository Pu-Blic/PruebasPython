

import datetime
# otra forma de importar la parte 'date' de la librería datetime
from datetime import date, timedelta

print (date.today())
print (datetime.date.today())


import miModulo
print(miModulo.sumar(3,1))

from miModulo import sumar
print(sumar(5,5))

from colorama import Fore, Back, Style, init
init(convert = True)
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


