from random import randint
n = randint(1, 10)
while True:
    escola = int(input('Escola um número ente 0 a 10: '))
    if n == escola:
        print(f'Parabéns!!!'
              f'Sua resposta foi correta...'
              f' eu tinha escolhido {n}')
        break
    resp = input('Quer tentar novamente? ').strip().upper()[0]
    if resp == 'S':
        if n > escola:
            print(f'Maior')
        if n < escola:
            print(f'Menor')
    if resp == 'N':
        print('Programa Finalizado!!!')
        break
