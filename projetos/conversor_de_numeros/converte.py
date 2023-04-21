# conversor de numeros

def inverte_str(n):
    # inverte aqui usando str[::-1]
    return n[::-1]


# a função recebe os parâmetros num para qualquer número e formato para o tipo.
def converte_numero(num, formato='d'):

    # decimal 0 1 2 3 4 5 6 7 8 9
    # octal 0 1 2 3 4 5 6 7
    # hexadecimal 0 1 2 3 4 5 6 7 8 9 A B C D F
    # binário 0 1

    teste = 123

    def converte_para_binario(num):
        saida = ''
        while 0 < num:
            binario = num % 2
            saida = str(saida) + str(binario)
            tira_metade = num // 2
            num = tira_metade

            if num < 1:
                inverte_str(saida)
                return int(saida)

    converte_para_binario(teste)


converte_numero(10)
