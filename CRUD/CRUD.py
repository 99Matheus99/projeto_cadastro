import pandas as pd
import os
import re
def limpa_tela(): # limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
def lista(): # mostra todas as pessoas cadastradas
    limpa_tela()
    if len(df) == 0:
        print('Não há pessoas cadastradas.')
    else:
        print(df)
    input('\nPressione ENTER para sair...') # serve como um "aguarde"
def cadastra(): # cadastra uma pessoa nova
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
            altura = float(altura)
            break
        else:
            print('Erro... entrada inválida')
    while True:
        peso = input('peso: ')
        # pego qualquer número inteiro antes e depois do ponto
        # esse número antes do ponto deve aparecer no máximo 3 vezes, e depois do ponto, 2 vezes
        if re.match(r'^[0-9]{2,3}\.[0-9]{1,2}$', peso):
            peso = float(peso)
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
            df_temp = df[df['nome'].str.contains(nome, case=False)] # crio um data frame com qualquer palavra que ele ache que possui no df
            if len(df_temp) == 0:
                print('O valor digitado não exite nos registros')
            else:
                print(df_temp)
                return df_temp.index
        else:
            print('Erro...Entrada inválida')
        # COLOCAR FUNÇÃO PRA SAIR!
def edita(): # edita a pessoa escolhida
    limpa_tela()
    indice_aux = consulta()
    escolha_aux = input('Digite o campo a ser alterado: ').lower()
    if escolha_aux == 'nome':
        while True:
            var_aux = input('Digite o novo nome: ')
            if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', var_aux):
                df.iloc[[indice_aux[0]], [0]] = var_aux # seleciono a linha que quero, e o valor a ser editado
                break
            else:
                print('Erro... nome inválido')
    elif escolha_aux == 'cpf':
        while True:
            var_aux = input('Digite o novo cpf: ')
            if re.match(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', var_aux):
                df.iloc[[indice_aux[0]], [1]] = var_aux
                break
            else:
                print('Erro... cpf inválido')
    elif escolha_aux == 'nascimento':
        while True:
            var_aux = input('Digite o novo nascimento: ')
            if re.match(r'^[0-9]{1,2}[-.\/][0-9]{1,2}[-.\/][0-9]{4}$', var_aux):
                df.iloc[[indice_aux[0]], [2]] = var_aux
                break
            else:
                print('Erro... nascimento inválido')
    elif escolha_aux == 'altura':
        while True:
            var_aux = input('Digite a nova altura: ')
            if re.match(r'^\d{1}\.\d{0,2}$', var_aux):
                df.iloc[[indice_aux[0]], [3]] = float(var_aux)
                break
            else:
                print('Erro... altura inválido')
    elif escolha_aux == 'peso':
        while True:
            var_aux = input('Digite o novo peso: ')
            if re.match(r'^\d{1}\.\d{0,2}$', var_aux):
                df.iloc[[indice_aux[0]], [4]] = float(var_aux)
                break
            else:
                print('Erro... peso inválido')
    df.to_json('Bd.json', force_ascii=False, orient='records') # salvo logo em seguida
    print('Dados alterados com sucesso!')
    input('\nPressione ENTER para sair...') 
def exclui(): # exclui a pessoa escolhida
    aux_esc = ''
    limpa_tela()
    indice_aux = consulta()
    aux_esc = input('Deseja deletar?(S/N) ').strip().upper()
    if aux_esc in 'SSIM':
        print('Dados excluídos com sucesso')
        input('\nPressione ENTER para sair...')
        return df.drop(indice_aux)
    else:
        input('\nPressione ENTER para sair...')
        return df # se ele desistir, retorno o próprio df
def converte_excel(): # salva o Df em um arquivo xlsx
    limpa_tela()
    df.to_excel('Bd.xlsx', engine='openpyxl') # salva em xlsx
    print('Arquivo gerado com sucesso...')
    input('\nPressione ENTER para sair...')
# -- INÍCIO DO CÓDIGO PRINCIPAL --
try:
    df = pd.read_json('Bd.json') # abre o arquivo
except FileNotFoundError: # caso o arquivo não exista, ele cria o arquivo
    df = pd.DataFrame(columns=['nome', 'cpf', 'nascimento', 'altura', 'peso'])
    df.to_json('Bd.json')
while True:
    limpa_tela()
    print('--------------------------')
    print(f'Pessoas cadastradas: {len(df)}')
    print('--------------------------')
    print('1 - listar pessoas')
    print('2 - cadastrar pessoas')
    print('3 - consultar pessoas')
    print('4 - Editar pessoas')
    print('5 - Excluir pessoas')
    print('6 - Exportar p/ excel')
    print('0 - sair')
    print('--------------------------')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        lista()
    elif escolha == 2:
        cadastra()
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