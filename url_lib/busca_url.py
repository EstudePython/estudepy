def busca_url(link):
    import urllib.request
    import ssl

    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(urllib.request.Request(
        url=link,
        headers={'User-Agent': 'Mozilla/5.0'}
    ), context=contexto_ssl)

    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<body>'
    marcador_final = '</body>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return pagina[inicio:final].strip()


print(busca_url('https://www.google.com'))
