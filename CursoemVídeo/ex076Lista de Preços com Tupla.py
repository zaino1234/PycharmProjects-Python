produtos_preco = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
                  'Transferidor', 4, 'Compasso', 9.99, 'Mochila', 120.32, 'Livro', 34.90)
print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*45)
for a in range(0, len(produtos_preco)):
    if a % 2 == 0:
        print(f'{produtos_preco[a]:.<33}', end='')
    else:
        print(f'R$ {produtos_preco[a]:>7.2f}')
print('-'*45)