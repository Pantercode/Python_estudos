filmes = {
    'drama': ['Cidadão kane', 'O Poderoso Chefão'],
    'comédia': ['Tempos Modernos','American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}
with open('filmes.html','w', encoding='utf-8')as pagina:
    pagina.write("""
    <DOCTYPE html>
    <html lang='pt-Br'>
    <head>
    <meta charset='utf-8'>
    <title>Filmes</title>
    </head>
    </body>
    """)
    for c, v in filmes.items():
        pagina.write(f'<h1>{c}</h1>\n')
        for e in v:
            pagina.write(f'<h2>{c}</h2>\n')
            pagina.write((f'<body></html>'))