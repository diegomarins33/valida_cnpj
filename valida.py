import re


def remove_caracteres(cnpj):
    return list(re.sub(r'[^0-9]', '', cnpj))


def remove_digitos(new_cnpj):
    cnpj_original = []
    for v in new_cnpj:
        cnpj_original.append(v)
    cnpj_original.pop()
    cnpj_original.pop()
    return cnpj_original


def calcula_primeiro_digito(temp_cnpj):
    cnpj_convertido = [int(val) for val in temp_cnpj]
    cont = 0
    lista_calculo = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    new_lista = []
    for i in lista_calculo:
        r = i * cnpj_convertido[cont]
        new_lista.append(r)
        cont += 1
    soma = sum(new_lista)
    numero = 11 - (soma % 11)
    numero = numero if numero <= 9 else 0
    cnpj_convertido.append(numero)
    return cnpj_convertido


def calcula_segundo_digito(primeiro_digito):
    cont = 0
    lista_calculo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    new_lista = []
    for i in lista_calculo:
        r = i * primeiro_digito[cont]
        new_lista.append(r)
        cont += 1
    soma = sum(new_lista)
    numero = 11 - (soma % 11)
    segundo_digito = list.copy(primeiro_digito)
    numero = numero if numero <= 9 else 0
    segundo_digito.append(numero)
    return segundo_digito


def verifica_cnpj(new_cnpj, segundo_digito):
    str_new_cnpj = [int(val) for val in new_cnpj]
    if str_new_cnpj == segundo_digito:
        return 'CNPJ Válido!'
    else:
        return 'CNPJ Inválido!'
