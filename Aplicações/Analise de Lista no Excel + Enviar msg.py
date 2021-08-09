import pandas as pd# Integração do python excel
import openpyxl as op
import twilio as tw# Integração do python com sms
from twilio.rest import Client

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():# indica a coluna escolhida na tabela tabela_vendas ['Vendas']
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'O vendedor {vendedor} vendeu R$ {vendas} no mês de {mes}.')

        # pega o account_sid no site auth_token
        account_sid = "AC8cd2b2da3bdbe71b6a10a4c85cd5a69c"
        auth_token  = "38bd46ce4144b9b3dcd1aea08713e4e3"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+xxxxxxx",
            from_="+15046081225",
            body=f'O vendedor {vendedor} vendeu R$ {vendas} no mês de {mes}.')
        print(message.sid)
