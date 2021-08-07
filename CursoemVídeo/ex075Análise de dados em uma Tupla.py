tupla = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Você digitou: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na {tupla.index(3)+1}ª posição')
print('Os números Pares foram: ', end=' ')
for a in tupla:
    if a % 2 == 0:
        print(a, end=' ')

