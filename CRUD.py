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
        # pego basicamente qualquer letra maiúscula, minúscula, com acentos, espaço em branco e com ponto no final
        if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
            break
        else:
            print('Erro... nome inválido')
    while True:
        cpf = input('Digite o CPF: ')
        # pego qualquer em uma repetição do padrão do CPF, separado por "." e no final por "-"
        if re.match(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf):
            break
        else:
            print('Erro... CPF inválido')
    while True:
        nascimento = input('data de nascimento: ')
        # aqui pego qualquer número inteiro, separado por "/", "." ou "-"
        if re.match(r'^[0-9]{1,2}[-.\/][0-9]{1,2}[-.\/][0-9]{4}$', nascimento):
            break
        else:
            print('Erro... data inválida')
    while True:
        altura = input('altura: ')
        # aqui pego qualquer número inteiro com 1 casa decimal antes do ponto e 2 casas depois do ponto
        if re.match(r'^\d{1}\.\d{0,2}$', altura):
            break
        else:
            print('Erro... entrada inválida')
    while True:
        peso = input('peso: ')
        # pego qualquer número inteiro antes e depois do ponto
        # esse número antes do ponto deve aparecer no máximo 3 vezes, e depois do ponto, 2 vezes
        if re.match(r'^[0-9]{2,3}\.[0-9]{1,2}$', peso):
            break
        else:
            print('Erro... entrada inválida')
    df.loc[len(df)] = [nome, cpf, nascimento, altura, peso] # caso localize uma linha que não existe, ele cria uma nova
    df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    print('Dados registrados!')
    input('\nPressione ENTER para sair...')
def consulta(): # consulta a pessoa no banco de dados
    limpa_tela()
    while True:
        nome = input('Digite o nome exato a ser pesquisado: ')
        if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome): # aceita qualquer letra maiúscula, minúscula, com acentos, espaço em branco e com ponto no final
            if nome in df['nome'].values:
                print(df[df['nome'] == nome])
                indice = df.index[df['nome'] == nome].tolist()
                return indice # retorno o índice para quem quiser usar
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
    input('\nPressione ENTER para sair...') 
def exclui(): # exclui a pessoa escolhida
    aux_esc = ''
    limpa_tela()
    indice_aux = consulta()
    aux_esc = input('Deseja deletar?(S/N) ').strip().upper()
    if aux_esc in 'SSIM':
        return df.drop(indice_aux)
    input('\nPressione ENTER para sair...')
def converte_excel(): # salva o Df em um arquivo xlsx
    limpa_tela()
    df.to_excel('Bd.xlsx', engine='openpyxl') # salva em xlsx
    print('Arquivo gerado com sucesso...')
    input('\nPressione ENTER para sair...')
# -- INÍCIO DO CÓDIGO PRINCIPAL --
df = pd.read_json('Bd.json') # abre o arquivo
while True:
    limpa_tela()
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
        input('\nPressione ENTER para sair...')
    elif escolha == 4:
        edita()
    elif escolha == 5:
        df = exclui() 
        df.to_json('Bd.json', force_ascii=False, orient='records')
    elif escolha == 6:
        converte_excel()
    elif escolha == 0:
        break