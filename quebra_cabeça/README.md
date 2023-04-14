## Horoscopo.py

### Analizando horoscopo.py

```python
## esta função é resposável por separar uma data no formato DDMMAAAA para DD, MM, AAAA.
def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a

## A função "signo()" recebe dois parâmetros, um é o "dia" e o outro é "mes".
def signo(dia, mes):
    ## testa se "mes" vale o mesmo que 3
    if mes == 3:
        # É executada se passar no teste, retorna 'Peixes' se "dia" < 21 e 'Áries' do contrário.
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sargitário'
    if mes == 12:
        return 'Sargitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

## A função "remover_ascentos" recebe um parâmetro e formata-o para para que se houver ascentos, sejam removidos.
def remover_acentos(texto):
    from unicodedata import normalize
    texto = str(texto)
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

## A função "horoscopo" usa uma biblioteca que acessa um conteúdo de um url de um site de horoscopo e retira do url uma mensagem conforme o parâmetro passado.
def horoscopo(signo_desejado):
    import urllib.request, ssl
    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(requisicao, context=contexto_ssl)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '<a class="webshare-link">Compartilhar</a>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ':' + pagina[inicio:final].strip()

## Esta função é responsável por executar as instruções responsáveis pelo input e output de dados
def main():
    # Entrada de dados
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))

    # Processamento
    dia, mes, ano = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saída de dados
    print(horoscopo_de_hoje)

## A função está dentro do módulo __main__ e será executada primeiro, assim chamando a função "main()"
if __name__ == '__main__':
    main()
```
