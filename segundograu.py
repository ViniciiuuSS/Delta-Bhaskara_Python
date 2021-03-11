#CALCULA O DELTA
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
b = b ** 2
c = (a * c)
delta = b - (4 * c)
print('Delta = {}'.format(delta))

#CALCULA O X1
b = float(input('Digite o valor de B: '))
delta = float(input('Qual valor de delta: '))
a = float(input('Digite o valor de A: '))
b = (-b - (delta**(1/2)))
a = 2*a
x1 = b/a

#CALCULA O X2
b = float(input('Digite o valor de B: '))
delta = float(input('Qual valor de delta: '))
a = float(input('Digite o valor de A: '))
b = (-b + (delta**(1/2)))
a = 2*a
x2 = b/a
#MOSTRA O RESULTADO ENTRE X1 E X2
print('S = ({},{})'.format(x1,x2))
