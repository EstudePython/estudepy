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
    marcador_inicio = '<span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap" role="text">'
    marcador_final = '</span>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return pagina[inicio:final].strip()


print(busca_youtube(
    'https://www.youtube.com/watch?v=FNqdV5Zb_5Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=8'))
