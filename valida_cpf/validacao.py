# PEGA O CPF
cpf = input('Digite o CPF: ')
cpf = list(cpf)
cpf = ''.join(filter(str.isdigit, cpf)) # tira o que não é dígito

# PRIMEIRO DIGITO VERIFICADOR
soma = digito1 = 0
for n in range(0,9):
    soma += int(cpf[n]) * (10 - n)

resto = soma % 11
if(resto < 2):
    digito1 = 0
else:
    digito1 = 11 - resto