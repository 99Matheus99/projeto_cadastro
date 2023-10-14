import pandas as pd
def listamento():
    print('\n')
    print(df)
def cadastramento(): 
    nome = nascimento = ''
    cpf = altura = peso = 0
    nome = input('Nome: ')
    cpf = int(input('CPF: '))
    nascimento = input('data de nascimento: ')
    altura = float(input('altura: '))
    peso = float(input('peso: '))
    df.loc[len(df)] = [nome, cpf, nascimento, altura, peso] # caso localize uma linha que não existe, ele cria uma nova
    df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida

df = pd.read_json('Bd.json') # abre o arquivo
while True:
    print('--------------------------')
    print('1 - listar')
    print('2 - cadastrar')
    print('3 - consultar')
    print('4 - Editar')
    print('5 - Excluir')
    print('6 - Exportar p/ excel')
    print('0 - sair')
    print('--------------------------')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        listamento() # mostra todas as pessoas cadastradas
        input('Aperte para sair...') # serve como um "aguarde" 
    elif escolha == 2:
        cadastramento() # cadastra uma pessoa nova
        input('Aperte para sair...')
    elif escolha == 0:
        break