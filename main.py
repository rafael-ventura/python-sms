# pandas, openpyxl, twilio
import pandas as pd
from twilio.rest import Client

account_sid = "AC34a9d71f86088efc5fb0d2cbdf99a8b3"
auth_token = "yourAuthToken"
client = Client(account_sid, auth_token)
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabelas = pd.read_excel(f'{mes}.xlsx')

    if (tabelas['Vendas'] > 55000).any():

        vendedor = tabelas.loc[tabelas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelas.loc[tabelas['Vendas'] > 55000, 'Vendas'].values[0]
        try:
            message = client.messages.create(
                to="+YourNumber",
                from_="+YourTwilioNumber",
                body=
                f"No mes {mes}, O Vendedor {vendedor} bateu a meta com {vendas}R$ de vendas."
            )
            print(f'mensagem enviada no id{message.sid}')
        except NameError:
            print('Não foi possivel enviar a mensagem')
            print(NameError)
