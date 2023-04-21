def busca_youtube(link):
    import urllib.request
    import ssl

    requisicao = urllib.request.Request(
        url=link,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(requisicao, context=contexto_ssl)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<body>'
    marcador_final = '</body>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return pagina[inicio:final].strip()


print(busca_youtube(
    'https://www.youtube.com/watch?v=hdDHg1p3YVc'))
