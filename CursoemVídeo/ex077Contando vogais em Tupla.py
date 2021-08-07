palavra_tupla = ('aprender', 'programar', 'estudar', 'python', 'mercado', 'trabalho',
         'programador', 'futuro', 'agora')
for a in palavra_tupla:
    print(f'\nPara a palvra {a.upper()} temos: ', end=' ')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
