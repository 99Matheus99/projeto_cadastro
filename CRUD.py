import pandas as pd
import os
import re
def limpa_tela(): # limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
def listamento(): # mostra todas as pessoas cadastradas
    limpa_tela()
    print(df)
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
def cadastramento(): # cadastra uma pessoa nova
    limpa_tela()
    nome = nascimento = ''
    cpf = altura = peso = 0
    while True:
        nome = input('Nome: ')
        if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
            break
        else:
            print('Erro... Entrada inválida')
    nascimento = input('data de nascimento: ')
    altura = float(input('altura: '))
    peso = float(input('peso: '))
    df.loc[len(df)] = [nome, cpf, nascimento, altura, peso] # caso localize uma linha que não existe, ele cria uma nova
    df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
def consulta(): # consulta a pessoa no banco de dados
    limpa_tela()
    while True:
        nome = input('Digite o nome exato a ser pesquisado: ')
        if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome): # aceita qualquer letra maiúscula, minúscula, com acentos, espaço em branco e com ponto no final
            if nome in df['nome'].values:
                print(df[df['nome'] == nome]) # mostra o valor na linha do índice do nome digitado
                indice = df.index[df['nome'] == nome].tolist() # guardo o índice da linha
                break
            else:
                print('O valor digitado não exite nos registros')
        else:
            print('Erro...Entrada inválida')
def edita(): # edita a pessoa escolhida
    limpa_tela()
    consulta()
    nome = nascimento = ''
    cpf = altura = peso = 0
    indice = 0
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
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
def exclui(): # exclui a pessoa escolhida
    limpa_tela()
    nome = input('Digite o nome que deseja excluir: ')
    if nome in df['nome'].values:
        print(df[df['nome'] == nome]) # mostra o valor na linha do índice do nome digitado
        indice = df.index[df['nome'] == nome].tolist() # guardo o índice da linha
        aux = input('Tem certeza da escolha? ').strip()
        if aux in 's':
            return df.drop(indice)
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
def converte_excel(): # salva o Df em um arquivo xlsx
    limpa_tela()
    df.to_excel('Bd.xlsx', engine='openpyxl') # salva em xlsx
    print('Arquivo gerado com sucesso...')
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
df = pd.read_json('Bd.json') # abre o arquivo
while True:
    limpa_tela() # limpa a tela
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
        listamento()
    elif escolha == 2:
        cadastramento()
    elif escolha == 3:
        consulta()
        input('\nPressione ENTER para sair...') # serve como um "aguarde"
    elif escolha == 4:
        edita()
    elif escolha == 5:
        df = exclui() 
        df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    elif escolha == 6:
        converte_excel()
    elif escolha == 0:
        break