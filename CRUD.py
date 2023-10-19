import pandas as pd
def listamento():
    print('\n')
    print(df)
    input('Aperte para sair...') # serve como um "aguarde"
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
    input('Aperte para sair...')
def consulta():
    nome = input('Digite o nome exato a ser pesquisado: ')
    if nome in df['nome'].values:
        print(df[df['nome'] == nome]) # mostra o valor na linha do índice do nome digitado
    input('Aperte para sair...')
def edita():
    nome = nascimento = ''
    cpf = altura = peso = 0
    indice = 0
    nome = input('Digite o nome exato a ser editado: ')
    if nome in df['nome'].values:
        print(df[df['nome'] == nome]) # mostra o valor na linha do índice do nome digitado
        indice = df.index[df['nome'] == nome].tolist() # guardo o índice da linha
    nome = input('novo nome: ')
    df.iloc[[indice], [0]] = nome # seleciono a linha que quero, e o valor a ser editado
    cpf = int(input('novo CPF: '))
    df.iloc[[indice], [1]] = cpf 
    nascimento = input('nova data de nascimento: ')
    df.iloc[[indice], [2]] = nascimento
    altura = float(input('nova altura: '))
    df.iloc[[indice], [3]] = altura
    peso = float(input('novo peso: '))
    df.iloc[[indice], [4]] = peso
    df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    input('Aperte para sair...')
def exclui():
    nome = input('Digite o nome que deseja excluir: ')
    if nome in df['nome'].values:
        print(df[df['nome'] == nome]) # mostra o valor na linha do índice do nome digitado
        indice = df.index[df['nome'] == nome].tolist() # guardo o índice da linha
        aux = input('Tem certeza da escolha? ').strip()
        if aux in 's':
            return df.drop(indice)
    input('Aperte para sair...')
df = pd.read_json('Bd.json') # abre o arquivo
while True:
    print('--------------------------')
    print(f'Pessoas cadastradas: {len(df)}')
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
    elif escolha == 2:
        cadastramento() # cadastra uma pessoa nova
    elif escolha == 3:
        consulta() # consulta a pessoa no banco de dados
    elif escolha == 4:
        edita() # edita a pessoa escolhida
    elif escolha == 5:
        df = exclui() # exclui a pessoa escolhida
        df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    elif escolha == 6:
        df.to_excel('Bd.xlsx', engine='openpyxl')
    elif escolha == 0:
        break