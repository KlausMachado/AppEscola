import sqlite3
from database import criar_tabela, inserir_alunos_iniciais
from crud import(
    inserindo_aluno,
    alterando_aluno,
    deletar_aluno,
    listar_aluno,
    buscar_aluno_por_nome,
    buscar_por_turma
    )
from relatorios import calcular_media_notas    

#MENU:
def menu(cursor, conn):
    while True:
        print("\nBem vindo ao arquivo da escola.")
        print("1- Exibir lista de alunos ")
        print("2- Inserir novo aluno")
        print("3- Deletar aluno")
        print("4- Alterar aluno")
        print("5- Calcular média dos alunos")
        print("6- Buscar aluno")
        print("7- Burcar turma")
        print("8- SAIR")
        print("-" * 30)
        try:
            escolha = int(input("\nQual ação deseja realizar? "))
            if escolha in [1, 2, 3, 4, 5, 6, 7, 8]:
                if escolha == 1:
                    print("\nAlunos cadastrados:")
                    listar_alunos(cursor)
                    print("-" * 30)
                elif escolha == 2:
                    print("\nInserindo novo aluno:")
                    inserindo_aluno(cursor, conn)                            
                    print("-" * 30)
                elif escolha == 3:
                    print("\nDeletar aluno:")
                    deletar_aluno(cursor, conn)
                    print("-" * 30)
                elif escolha == 4:
                    print("\nAlterar aluno:")
                    alterando_aluno(cursor, conn)
                    print("-" * 30)
                elif escolha == 5:
                    print("\nCalculando média dos alunos:")
                    calcular_media_notas(cursor)
                    print("-" * 35)
                elif escolha == 6:
                    print("\nBuscar aluno")
                    buscar_aluno_por_nome(cursor)
                    print("-" * 26)
                elif escolha == 7:
                    print("\nBuscar turma")
                    buscar_por_turma(cursor)
                    print("-" * 26)
                elif escolha == 8:
                    print("\nEncerrrando programa....")
                    break
            else:
                print("Opção invalida.")
        except ValueError:
                print("Opção invalida.")
                

        continuar = input("\nDeseja realizar outra ação? (s/n)").lower()
        if continuar != 's':
            print("\nEncerrrando programa....")
            break
if __name__ == "__main__":
    with sqlite3.connect("cadastroAluno.db") as conn:
        cursor = conn.cursor()
        criar_tabela(cursor)
        inserir_dados_iniciais(cursor)
        conn.commit()
        menu(cursor, conn)
