import os
import re
def valida_cpf():
    # PRIMEIRO DIGITO VERIFICADOR
    soma = digito1 = 0
    for n in range(0,9):
        soma += int(cpf[n]) * (10 - n)
    resto = soma % 11
    if(resto < 2):
        digito1 = 0
    else:
        digito1 = 11 - resto

    # SEGUNDO DIGITO VERIFICADOR
    soma = digito2 = 0
    for n in range(0,10):
        soma += int(cpf[n]) * (11 - n)
    resto = soma % 11
    if(resto < 2):
        digito2 = 0
    else:
        digito2 = 11 - resto

    # PARTE DA ANÁLISE
    if digito1 == int(cpf[9]) and  digito2 == int(cpf[10]):
        return True
    else:
        return False
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela do prompt
# PEGA O CPF
while True:
    cpf = input('Digite o CPF: ')
    # pego qualquer em uma repetição do padrão do CPF, separado por "." e no final por "-"
    if re.match(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf):
        break
    else:
        print('Erro... cpf deve conter formato xxx.xxx.xxx-xx')
cpf = list(cpf)
cpf = ''.join(filter(str.isdigit, cpf)) # tira o que não é dígito

validacao = valida_cpf()

if validacao == True:
    print('\033[1;32m cpf é válido!\033[m') # texto em negrito, cor verde
else:
    print('\033[1;31m cpf é inválido!\033[m') # texto em negrito, cor vermelho