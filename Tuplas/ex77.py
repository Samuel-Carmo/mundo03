palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'Na palavra {c.upper()} nos temos', end=' ')
    for l in c:
        if l.lowee() in 'aeiou':
            print(l, end=' ')
    print()