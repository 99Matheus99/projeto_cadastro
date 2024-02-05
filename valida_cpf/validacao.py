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

# PEGA O CPF
cpf = input('Digite o CPF: ')
cpf = list(cpf)
cpf = ''.join(filter(str.isdigit, cpf)) # tira o que não é dígito

validacao = valida_cpf()

if validacao == True:
    print('O cpf é válido!')
else:
    print('O cpf é inválido!')