# conversor de sistemas numeros

# a função recebe os parâmetros num para qualquer número e formato para o tipo.
def converte_numero(num, formato=2):
    if num == '':
        raise ValueError('Insira um valor que preste!')

    # decimal 0 1 2 3 4 5 6 7 8 9
    # octal 0 1 2 3 4 5 6 7
    # hexadecimal 0 1 2 3 4 5 6 7 8 9 A B C D F
    # binário 0 1

    # comparam qual será o tipo numérico processado
    if formato == 'd':
        formato = 10
    elif formato == 'b':
        formato == 2
    elif formato == 'o':
        formato == 8
    elif formato == 'h':
        formato == 16

    saida = ''
    while 0 < num:
        unidade = num % formato
        saida = str(saida) + str(unidade)
        tira_metade = num // formato
        num = tira_metade
        if num < 1:
            numero = int(saida[::-1])
            return numero, formato

    return num, formato


# x, y = int(input('Número: ')), int(input('Tipo: '))
# Debug
x, y = 396, 16

x, y = converte_numero(x, y)

u = c = ''
if y == 2:
    u = 'binário'
    c = str(x).zfill(8)
elif y == 8:
    u = 'octal'
elif y == 10:
    u = 'decimal'
elif y == 16:
    u = 'hexadecimal'
else:
    u = 'Sei lá'


print(f'{c if y == 2 else x} {u}')
