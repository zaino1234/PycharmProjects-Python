from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Listagem de números gerados:', end=' ')
for a in lista:
      print(f'{a}', end=' ')
print(f'\nO maior valor sorteado foi: {max(lista)}')
print(f'O menor valor sorteado foi: {min(lista)}')
