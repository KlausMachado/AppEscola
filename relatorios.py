from utils import media_notas
#ANALIZANDO DADOS
def calcular_media_notas(cursor):    
    cursor.execute("SELECT nome, turma, notas FROM alunos")
    alunos = cursor.fetchall()
    aprovados = []
    reprovados = []
    recuperacao = []
    for nome, turma, notas_str in alunos:
        media = media_notas(notas_str)
        if media >= 7:
            aprovados.append((nome, turma, media))
        elif media >= 5:
            recuperacao.append((nome, turma, media))
        elif media <= 4.9:
            reprovados.append((nome, turma, media))
                
    print("\nLista de aprovados: ")
    print(f"{'Nome':<19}{'Media':>4}{'Turma':>10}")
    print("-" * 35)
    for nome, turma, media in aprovados:            
        print(f"{nome:<20}{media:>2.1f}{turma:>10}")
    print("-" * 35)    
    print("\nLista de reprovados: ")
    print(f"{'Nome':<19}{'Media':>2}{'Turma':>10}")
    print("-" * 35)
    for nome, turma, media in reprovados:
        print(f"{nome:<20}{media: >2.1f}{turma:>10}")
    print("-" * 35)            
    print("\nLista de recuperacao: ")
    print(f"{'Nome':<19}{'Media':>2}{'Turma':>10}")
    print("-" * 35)
    for nome, turma, media in recuperacao:
        print(f"{nome:<20}{media: >2.1f}{turma:>10}")
