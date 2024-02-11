import re
import sys


def corrigindo_cpf(param):
    new_cpf = re.sub(r'[^0-9]', '', param)
    if len(new_cpf) > 11 or len(new_cpf) < 11:
        print('CPF inválido')
        sys.exit()
    return new_cpf


def entrada_sequencial(param):
    new_cpf = param == param[0] * len(param)
    if cpf:
        print('CPF inválido')
        sys.exit()

    return new_cpf


cpf = corrigindo_cpf(input('digite seu cpf: '))
entrada_sequencial(cpf)

nove_digito = cpf[:9]

resultado_1 = 0


contador_regressivo = 10

# Calculo do primeiro dígito do CPF

for i in nove_digito:
    resultado_1 += int(i) * contador_regressivo

    contador_regressivo -= 1


digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digito = cpf[:10]

resultado_2 = 0


contador_regressivo = 11

# alculo do segundo dígito do CPF

for i in dez_digito:
    resultado_2 += int(i) * contador_regressivo

    contador_regressivo -= 1


digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'{cpf_gerado} é valido')
else:
    print('CPF invalido')
