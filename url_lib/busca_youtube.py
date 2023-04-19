def busca_youtube(link):
    import urllib.request
    import ssl
    minha_url = link

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
