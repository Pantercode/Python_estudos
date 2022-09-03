for c in range(1,101):
    with open('pagina.html',"w", encoding="utf-8") as pagina:
        pagina.write('<DOCTYPE html>\n')
        pagina.write('<html lang=\>"pt-BR"\n')
        pagina.write('<head>\n')
        pagina.write('<meta charset=\"utf-8\">\n')
        pagina.write('<title>Titulo da Página</title>\n')
        pagina.write('</head>\n')
        pagina.write('<body>\n')
        pagina.write('Olá')
        for c in range(10):
            pagina.write(f'<p>{c}</p>\n')
            pagina.write('</body>\n')
            pagina.write('</html\>\n')