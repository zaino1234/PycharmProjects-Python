valores = [0]
contador = 0
for a in range(1, 6):
    valores.append(int(input(f'Digite um valor para a posição {contador}: ')))
    contador += 1
print(f'Lista de valore: {valores}')

print(f'O maior valor digitado foi{max (valores)} na posição')
print(f'O maior valor digitado foi{min(valores)} na posição')
