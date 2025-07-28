import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import numpy
from validacoes import media_notas 
#ANALIZANDO DADOS
def calcular_media_notas(cursor):    
    cursor.execute("SELECT nome, turma, notas FROM alunos")
    alunos = cursor.fetchall()
    aprovados = []
    reprovados = []
    recuperacao = []

    desempenho = {}

    for nome, turma, notas_str in alunos:
        media = media_notas(notas_str)

        if turma not in desempenho:
            desempenho[turma] = {'aprovados': 0, 'recuperacao': 0, 'reprovados': 0} #inicia um objeto da turma iniciando os contadores em 0
        if media >= 7:
            aprovados.append((nome, turma, media))
            desempenho[turma]['aprovados'] += 1  #soma 1 ao contador aprovados
        elif media >= 5:
            recuperacao.append((nome, turma, media))
            desempenho[turma]['recuperacao'] += 1  #soma 1 ao contador recuperacao
        elif media <= 4.9:
            reprovados.append((nome, turma, media))
            desempenho[turma]['reprovados'] += 1  #soma 1 ao contador reprovados

    #definindo maior turma com aprovados
    turma_mais_aprovados = max(desempenho.items(), key=lambda t: t[1]['aprovados']) #retorna lista com index 0 = turma; index 1 = objeto de contador
    #definindo maior turma com recuperação
    turma_mais_recuperacao = max(desempenho.items(), key=lambda t: t[1]['recuperacao'])
    #definindo maior turma com reprovados
    turma_mais_reprovados = max(desempenho.items(), key=lambda t: t[1]['reprovados'])

    #exibindo lista de alunos por desempenho            
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

    #exibindo lista de turmas por desempenho
    print("\nDesempenho por turma: ")
    print("-" * 35)
    print(f"Turma com mais aprovados: {turma_mais_aprovados[0]} ({turma_mais_aprovados[1]['aprovados']} alunos)")
    print(f"Turma com mais recuperacao: {turma_mais_recuperacao[0]} ({turma_mais_recuperacao[1]['recuperacao']} alunos)")
    print(f"Turma com mais reprovados: {turma_mais_reprovados[0]} ({turma_mais_reprovados[1]['reprovados']} alunos)")
    print("-" * 35)

    #gerando grafico de desempenho
    situacoes = ['Aprovados', 'Recuperacao', 'Reprovados']
    quantidades = [len(aprovados), len(recuperacao), len(reprovados)]
    cores = ['green', 'orange', 'red']

    #configurando grafico
    plt.figure(figsize=(8, 5))
    plt.bar(situacoes, quantidades, color=cores)
    plt.title('Desempenho dos alunos')
    plt.xlabel('Situacao')
    plt.ylabel('Quantidade de alunos')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    #formatando eixo y
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1.0))
    plt.tight_layout() #ajusta o layout para evitar corte de labels
    
    #exibindo grafico
    plt.show()
   
#TRANSFORMANDO EM CSV
def exportar_relatorio_para_csv(cursor, nome_arquivo="relatorio_alunos.csv"):
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()

    colunas = ["Nome", "Email", "Turma", "Notas"]
    df = pd.Dataframe(dados, columns=colunas)

    df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
    print(f"\nRelatório exportado com sucesso para: {nome_arquivo}")
