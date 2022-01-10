import re
from decoraVeloc import velocidade

REGRESSIVO_CNPJ = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
REGRESSIVO_CPF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


@velocidade
def validar(numero):
    numero = remover(numero)
    if len(numero) == 14:
        try:
            if check_sequencia(numero):
                return False
        except:
            return False

        try:
            novo_cnpj = calcula_digito(numero=numero, digito=1)
            novo_cnpj = calcula_digito(numero=novo_cnpj, digito=2)
        except Exception as e:
            return False

        if novo_cnpj == numero:
            return True
        else:
            return False
    elif len(numero) == 11:
        try:
            if check_sequencia(numero):
                return False
        except:
            return False

        try:
            novo_cpf = calcula_digito(numero=numero, digito=1)
            novo_cpf = calcula_digito(numero=novo_cpf, digito=2)
        except Exception as e:
            return False

        if novo_cpf == numero:
            return True
        else:
            return False


def calcula_digito(numero, digito):
    if digito == 1:
        regressivos = REGRESSIVO_CNPJ[1:] if len(numero) == 14 else REGRESSIVO_CPF[1:]
        novo_cnpj = numero[:-2]
    elif digito == 2:
        regressivos = REGRESSIVO_CNPJ if len(numero) == 14 else REGRESSIVO_CPF
        novo_cnpj = numero
    else:
        return None

    total = 0
    for índice, regressivo in enumerate(regressivos):
        total += int(numero[índice]) * regressivo
    digito = calcular(total)
    return f'{novo_cnpj}{digito}'


def remover(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def calcular(acumulador):
    digito_cnpj = 11 - (acumulador % 11)
    return digito_cnpj if digito_cnpj <= 9 else 0


def check_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False