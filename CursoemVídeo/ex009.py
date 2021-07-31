num = int(input('Digite um valor para ver sua tabuada: '))
print('-'*15)
for a in range(1, 11):
    print(f'{num:^2} x {a:^2} = {a * num:^2}')
print('-'*15)