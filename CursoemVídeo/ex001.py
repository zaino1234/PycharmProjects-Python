from random import randint
n = randint(1, 10)
while True:
    escola = int(input('Escola um número ente 0 a 10: '))
    if n == escola:
        print(f'Parabéns!!!'
              f'Sua resposta foi correta...'
              f' eu tinha escolhido {n}')
        break
    if n > escola:
        print(f'Maior')
    if n < escola:
        print(f'Menor')
