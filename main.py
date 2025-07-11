import sqlite3
from database import criar_tabela_alunos, inserir_dados_teste_alunos
from crud import(
    inserindo_aluno,
    alterando_aluno,
    deletar_aluno,
    listar_alunos,
    buscar_aluno_por_nome,
    buscar_por_turma
    )
from relatorios import calcular_media_notas 
from login import (
    cadastrar_usuario, 
    login_usuario, 
    criar_tabela_usuarios, 
    inserir_dados_teste_usuarios 
    )

#AUTENTICAÇÃO DE USUARIO
criar_tabela_usuarios()
inserir_dados_teste_usuarios()

def autenticar_usuario():
    while True:
        print("\n===Sistema de Login===")
        print("1- Cadastrar novo usuario")
        print("2- Fazer login")
        print("3- SAIR")
        try:
            opcao = int(input("Escolha uma opção: "))
            print("Executando...")
            if opcao in [1, 2]:
                if opcao == 1:
                    print("\n------Iniciando cadastro--------")
                    cadastrar_usuario()
                elif opcao == 2:
                    print("\n------Login-----")
                    if login_usuario():
                        return True
                elif opcao == 3:
                    print("Encerrando sistema...")
                    return False
            else:
                print("opção invalida")
        
        except ValueError:
            print("\nA opção deve ser um numero.")
            print("Tente novamente")


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
        print("8- Exportar relatorio geral em CSV")
        print("9- SAIR")
        print("-" * 30)
        try:
            escolha = int(input("\nQual ação deseja realizar? "))
            if escolha in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
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
                elif escolha == 9:
                    print("\nEncerrrando programa....")
                    break
                
                elif escolha == 8:
                    print("Exportando relatorio...")
                    exportar_relatorio_para_csv(cursor)
                    print("-" * 26)
                    
            else:
                print("Opção invalida.")
        except ValueError:
                print("\nA escolha deve ser um numero.")
                print("Tente novamente.")
                

        continuar = input("\nDeseja realizar outra ação? (s/n)").lower()
        if continuar != 's':
            print("\nEncerrrando programa....")
            break
if __name__ == "__main__":
    if autenticar_usuario():
        with sqlite3.connect("cadastroAluno.db") as conn:
            cursor = conn.cursor()
            criar_tabela_alunos(cursor)
            inserir_dados_teste_alunos(cursor)
            conn.commit()
            menu(cursor, conn)
