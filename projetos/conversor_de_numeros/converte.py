
# conversor de sistemas numeros

# a função recebe os parâmetros num para qualquer número e formato para o tipo.
def converte_numero(num, formato='b'):
    if num == '':
        raise ValueError('Insira um valor que preste!')

    # decimal 0 1 2 3 4 5 6 7 8 9
    # octal 0 1 2 3 4 5 6 7
    # hexadecimal 0 1 2 3 4 5 6 7 8 9 A B C D F
    # binário 0 1

    # comparam qual será o tipo numérico processado
    formato = formato.lower()
    valor_de_tipo = 0
    if formato in ('decimal', 'dec', 'd'):
        valor_de_tipo = 10
    elif formato in ('binario', 'bin', 'b'):
        valor_de_tipo = 2
    elif formato in ('octal', 'oct', 'o'):
        valor_de_tipo = 8
    # contem erros ao processar
    elif formato in ('hexadecimal', 'hex', 'h') or formato[:4] in 'hex':
        valor_de_tipo = 16

    # essa lógica funciona até octa
    valor_invertido = ''
    while 0 < num:
        unidade = num % valor_de_tipo if valor_de_tipo != 0 else 0
        valor_invertido = valor_invertido + str(unidade)
        tira_metade = num // valor_de_tipo if valor_de_tipo != 0 else 0
        num = tira_metade
        if num < 1:
            saida = valor_invertido[::-1]
            if valor_de_tipo == 2:
                return '0b' + saida, 'binário'
            elif valor_de_tipo == 8:
                return '0o' + saida, 'octal'
            elif valor_de_tipo == 10:
                return '0d' + saida, 'decimal'
            elif valor_de_tipo == 16:
                return '0h' + saida, 'hexadecimal'
            else:
                return saida, formato
    else:
        return num, formato


def formata_hexadecimal(numero):
    if ('A' or 'B' or 'C' or 'D' or 'F') in str(numero).upper():
        # é hexadecimal
        pass


def main():

    # Entrada
    x_in, y_in = int(input('Número: ')), str(input('Tipo: ')).strip()

    # Processamento
    x_out, y_out = converte_numero(x_in, y_in)
    saida_numero = x_out

    # Saída
    print(f'{saida_numero}({y_out}) = {hex(x_in)} = {len(saida_numero) - 3}n')

    # Armazenamento


if __name__ == '__main__':
    main()
