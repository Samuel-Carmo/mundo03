def notas(*n, sit=False):
    """
    ->unção para analizar notas e a situação de varios alunos.
    :param n: uma ou mais notas dos alunos(aceita várias)
    :param sit: valor opicional, indica se deve ou não adicionar a asituação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = {}
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    d = 0
    for c in n:
        d += c
    resp['média'] = d / resp['total']
    if sit:
        if resp['média'] < 5:
            resp['situação'] = 'RUIM'
        if resp['média'] >= 5 <7:
            resp['situação'] = 'RAZOÁVEL'
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
    return resp


resp = notas(5.5, 2.5, 10, 2.5, sit=True)
print(resp)