import calculadora


print('Que operacion quiere hacer?')
print('1 - Sumar')
print('2 - Restar')
print('3 - Multiplicar')
print('4 - Dividir')
op = input('Ingrese una opcion: ')

match op:
    case '1':
        operar = 'suma'
    case '2':
        operar = 'resta'
    case '3':
        operar = 'multiplicar'
    case '4':
        operar = 'dividir'

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

calculadora.calcular(num1, num2, operar)