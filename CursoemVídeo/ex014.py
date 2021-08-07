print('=-'*20)
print(f'{"CONVERSOR DE TEMPERATURA":^40}')
print('=-'*20)
opcao = int(input('''[ 1 ] Celsius (°C) para Fahrenheit(°F)
[ 2 ] Fahrenheit(°F) para Celsius (°C)
Escola uma opção: '''))
if opcao == 1:
    TC = float(input('Digite a temperatura: °C '))
    TF = ((TC * 9 / 5) + 32)
    print(f'{TC}°C = {TF}°F')
if opcao == 2:
    TF = float(input('Digite a temperatura: °F '))
    TC = ((TF - 32)*5)/9
    print(f'{TF}°F = {TC}°C')
