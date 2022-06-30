from valida import remove_caracteres, remove_digitos, calcula_primeiro_digito, calcula_segundo_digito, verifica_cnpj

cnpj = input('Digite o CNPJ: ')
new_cnpj = remove_caracteres(cnpj)
temp_cnpj = remove_digitos(new_cnpj)
primeiro_digito = calcula_primeiro_digito(temp_cnpj)
segundo_digito = calcula_segundo_digito(primeiro_digito)
verificacao = verifica_cnpj(new_cnpj, segundo_digito)
print(verificacao)
