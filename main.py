#Nome: Bernardo Schlottag Muller

with open('arquivo1.txt', 'r') as tde: #apenas mudar o nome dos arquivos .txt para rodar o programa.
    linhas = tde.readlines() 

pularLinha = 0

while pularLinha < len(linhas):
    linha = linhas[pularLinha].strip()

    if linha == 'U':

        conjunto1 = [numeros.strip() for numeros in linhas[pularLinha + 1].split(',')] 
        conjunto2 = [numeros.strip() for numeros in linhas[pularLinha + 2].split(',')]

        uniao = conjunto1 + conjunto2

        print('União:', 'conjunto 1', '{', ', '.join(conjunto1), '}.', 'conjunto 2', '{', ', '.join(conjunto2), '}.', 'Resultado:', '{', ', '.join(uniao), '}.')

        pularLinha += 2

    elif linha == 'I':
        
        conjunto3 = [numeros.strip() for numeros in linhas[pularLinha + 1].split(',')] 
        conjunto4 = [numeros.strip() for numeros in linhas[pularLinha + 2].split(',')]

        intersecao = list(set(conjunto4) & set(conjunto3))

        print('Interseção:', 'conjunto 1', '{', ', '.join(conjunto3), '}.', 'conjunto 2', '{', ', '.join(conjunto4), '}.', 'Resultado:', '{', ', '.join(intersecao), '}.')

        pularLinha += 2

    elif linha == 'D':

        conjunto5 = [numeros.strip() for numeros in linhas[pularLinha + 1].split(',')] 
        conjunto6 = [numeros.strip() for numeros in linhas[pularLinha + 2].split(',')]

        diferenca = list(set(conjunto6) - set(conjunto5))
        diferenca2 = list(set(conjunto5) - set(conjunto6))

        print('Diferença:', 'conjunto 1', '{', ', '.join(conjunto5), '}.', 'conjunto 2', '{', ', '.join(conjunto6), '}.', 'Resultado:', '{', ', '.join(diferenca + diferenca2), '}.')

        pularLinha += 2

    elif linha == 'C':

        conjunto7 = [numeros.strip() for numeros in linhas[pularLinha + 1].split(',')] 
        conjunto8 = [numeros.strip() for numeros in linhas[pularLinha + 2].split(',')]

        produtoCartesiano = [(x, y) for x in conjunto7 for y in conjunto8]

        cartesianoFormatado =', '.join([f'({x}, {y})' for x, y in produtoCartesiano])

        print('Produto cartesiano:', 'conjunto 1', '{', ', '.join(conjunto7), '}.', 'conjunto 2', '{', ', '.join(conjunto8), '}.', 'Resultado:', cartesianoFormatado,'.')

        pularLinha += 2

    pularLinha += 1
        
    
    

    
