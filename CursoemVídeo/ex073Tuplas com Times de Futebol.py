tabela_brasileirao = ('Palmeiras', 'Atlético-MG', 'Bragantino', 'Fortaleza','Flamengo',
                      'Athletico-PR', 'Ceará', 'Santos', 'Atlético-GO', 'Bahia',
                      'Corinthians', 'Fluminense', 'Juventude', 'Sport', 'Internacional',
                      'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
print(f'Lista de Times{tabela_brasileirao}')
print('-'*100)
print(f'Os 5 primeiros times: {tabela_brasileirao[0:5]}')
print('-'*100)
print(f'Os 4 últimos colocados: {tabela_brasileirao[-4:]}')
print('-'*100)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('-'*100)
print(f'O Chapecoense está na {tabela_brasileirao.index("Chapecoense")+1}ª posição.')
