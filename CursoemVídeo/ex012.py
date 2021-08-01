print('-'*40)
print(f'{"5% de DESCONTO":^40}')
print('-'*40)
valorpro = float(input('Qual é o preço do produto? R$ '))
des5 = valorpro - valorpro*5/100
print(f'O produto que custava R$ {valorpro},'
      f' na promoção com desconto de 5% vai custar R${des5}')
f