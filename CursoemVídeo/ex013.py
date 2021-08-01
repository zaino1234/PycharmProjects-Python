print('x'*40)
print(f'{"NOVOS SALÁRIOS":^40}')
print('x'*40)
salario = float(input('Qual é o salário atual? '))
aum15 = salario + (salario*15/100)
print(f'Um funcionário que ganhava R${salario}, com 15%'
      f' de aumento, passa a receber R${aum15:.2f}')
