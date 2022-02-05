#Calculando frete de uma viagem com desconto acima de 200km

km = float(input('\033[31mQuantos KM até seu destino ? \033[m'))
if km <= 200:
    n1 = km * 0.50
    print('sua viagem custará \033[1:35mR${}\033[m'.format(n1))
else:
    n2 = km * 0.45
    print('Sua viagem custará \033[1:35mR${}\033[m'.format(n2))
