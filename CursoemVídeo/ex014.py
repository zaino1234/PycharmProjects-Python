print('=-'*20)
print(f'{"CONVERSOR DE TEMPERATURA":^40}')
print('=-'*20)
opcao = int(input('''[ 1 ] Celsius (°C) para Fahrenheit(°F)
[ 2 ] Fahrenheit(°F) para Celsius (°C)
Escola uma opção: '''))
if opcao == 1:
    TC = float(input('Digite a temperatura: °C '))
    Tf = ((TC * 9 / 5) + 32)
    print(f'{TC:.1f}°C = {Tf:.1f}°F')
if opcao == 2:
    tff = float(input('Digite a temperatura: °F '))
