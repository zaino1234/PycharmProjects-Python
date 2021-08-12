print(f'{"Adicionar e Mudar Elementos em uma lista":=^100}')
lista_teste = ['A', 'B', 'C']
lista_teste[0] = 'D'#Munda o elemento indicado na seleção
lista_teste.append('E')#Adiciona um novo elemento no final da lista
lista_teste.insert(3, 'F')#Adiciona um novo elemento indicado na seleção
print(lista_teste)

print(f'{"Deletar Elementos de Uma Lista":=^100}')
del lista_teste[0]#Elimina o elemento indice 2 da lista
print(lista_teste)
print('-'*100)
lista_teste.pop()#Geralmete é usado para eliminar o último elemento da lisa, também pode ser
                    # para excluir o elemento selecionado
print(lista_teste)
print('-'*100)
lista_teste.remove('C')#Remove o elemento indicado pelo valor
print(lista_teste)

print(f'{"Criando lista atraves de range()/ e análise/configurando listas":=^100}')
valores = list(range(4, 7))#Cria uma lista de acorda com range escolhido
print(valores)
valores_1 = [8, 5, 9, 12, 2, 1, 0]
valores_1.sort()#Coloca os elementos em ordem crescente
print(valores_1)
valores_1.sort(reverse=True)#Coloca os elementos em ordem decrescente
print(valores_1)
print(len(valores_1))#Determina a quantidade elementos
print('-'*100)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei o final da lista')
print('-'*100)

a = [2, 3, 4, 7]
b = a[:]#Cria uma copia dos VALORES DE A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')




