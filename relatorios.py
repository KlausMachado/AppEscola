import pandas as pd
from utils import media_notas
#ANALIZANDO DADOS
def calcular_media_notas(cursor):    
    cursor.execute("SELECT nome, turma, notas FROM alunos")
    alunos = cursor.fetchall()
    aprovados = []
    reprovados = []
    recuperacao = []
    desempenho = {}
    for nome, turma, notas_str in alunos:
        if turma not in desempenho:
            desempenho[turma] = {"aprovados": 0, "recuperacao": 0, "reprovados": 0} #criando dicionario para cada turma

        media = media_notas(notas_str)
        if media >= 7:
            aprovados.append((nome, turma, media))
            desempenho[turma]["aprovados"] += 1  #adcionando aprovado no dicionario da determinada turma
        elif media >= 5:
            recuperacao.append((nome, turma, media))
            desempenho[turma]["recuperacao"] += 1
        elif media <= 4.9:
            reprovados.append((nome, turma, media))
            desempenho[turma]["reprovados"] += 1
                
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

    # definindo a turma com mais aprovados, reprovados e em recuperacao
    turma_mais_aprovados = max(desempenho.items(), key=lambda t: t[1]["aprovados"])
    turma_mais_reprovados = max(desempenho.items(), key=lambda t: t[1]["reprovados"])
    turma_mais_recuperacao = max(desempenho.items(), key=lambda t: t[1]["recuperacao"])

    #exibindo o desempenho por turma
    print("\nDesempenho por turma:")
    print("-" * 30)
    print(f"Turma com mais aprovados: {turma_mais_aprovados[0]} ({turma_mais_aprovados[1]['aprovados']} alunos)")
    print(f"Turma com mais em recuperação: {turma_mais_recuperacao[0]} ({turma_mais_recuperacao[1]['recuperacao']} alunos)")
    print(f"Turma com mais reprovados: {turma_mais_reprovados[0]} ({turma_mais_reprovados[1]['reprovados']} alunos)")
    print("-" * 30)

def exportar_relatorio_csv(cursor, nome_arquivo='relatorio_alunos.csv'):
    cursor.execute("SELECT nome, email, turma, notas FROM alunos")
    dados = cursor.fetchall()

    colunas = ['Nome', 'Email', 'Turma', 'Notas']
    df = pd.DataFrame(dados, columns=colunas)

    df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
    print(f"Relatório exportado para: {nome_arquivo}")
      
