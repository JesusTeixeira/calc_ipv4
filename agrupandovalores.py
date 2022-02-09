from itertools import groupby, tee
alunos = [
    {'nome': 'jd', 'nota': 'A'},
    {'nome': 'amanda', 'nota': 'S'},
    {'nome': 'brunao', 'nota': 's'},
    {'nome': 'otton', 'nota': 'A'},
    {'nome': 'silas', 'nota': 'C'},
    {'nome': 'Paulo', 'nota': 'S'},
    {'nome': 'Tamara', 'nota': 'S'},
    {'nome': 'Bianca', 'nota': 'C'},
    {'nome': 'Patricia', 'nota': 'F'},
    {'nome': 'Kelly', 'nota': 'F'},
    {'nome': 'Erico', 'nota': 'F'},
    {'nome': 'Arthur', 'nota': 'F'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)


for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')
    
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()