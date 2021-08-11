from random import randint
n = randint(1, 10)
while True:
    escolha = int(input('Escolha um número ente 0 a 10: '))
    if n == escolha:
        print(f'Parabéns!!!'
              f'Sua resposta foi correta...'
              f' eu tinha escolhido {n}')
        break
    if n > escolha:
        print(f'Maior')
    if n < escolha:
        print(f'Menor')
