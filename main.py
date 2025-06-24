import sqlite3
import re #para validar email

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

#FUNÇÕES CRUD:
#INSERINDO ALUNO
def inserindo_aluno(cursor, conn):
    while True:            
        nome = input("Digite o nome do aluno: ").title().strip()
        #VALIDANDO EMAIL
        while True:
            email = input("Digite o email do aluno: ")
            if not validar_email(email):
                print("Email invalido. Digite novamente.")
                continue
            cursor.execute("SELECT * FROM alunos WHERE email =?", (email,))
            if cursor.fetchone():
                print("Este e-mail já está cadastrado. Digite outro.")
                continue
            break                                                
        turma = input("Qual a turma do aluno: ").strip().title()
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve ser um inteiro entre 0 e 10.")
                                
                except ValueError:
                    print("Digite um número valido.")
                            
        notas_str = ",".join(map(str, notas))
        cursor.execute("INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)", (nome, email, turma, notas_str))
        conn.commit()
        print(f"\nAluno {nome} inserido com sucesso!")

        continuar = input("Deseja adicionar outro aluno? (s/n)").lower()
        if continuar != 's':
            break
        
#EXIBINDO DADOS
def exibindo_lista(cursor):       
    cursor.execute("SELECT * FROM alunos") 
    aluno = cursor.fetchall()
    for id, nome, email, turma, notas in aluno:
        print(f"Aluno {id}:\n{nome}; \n{email}; \nTurma: {turma} \nNotas: {notas};\n")

def exibir_aluno(cursor):
    nome = input("Digite o nome do aluno que deseja buscar: ").title().strip()
    cursor.execute("SELECT nome, notas FROM alunos WHERE nome=?", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        notas = list(map(float, resultado[1].split(",")))
        media = sum(notas) / len(notas)
        print(f"\n{resultado[0]} - Notas: {notas} | Média: {media:.1f}") 
    else:
        print("Aluno não encontrado")

#ALTERANDO DADOS    
def alterando_aluno(cursor, conn):
    email = input("Digite o email do aluno que deseja atualizar: ").strip()
    cursor.execute("SELECT * FROM alunos WHERE email =?", (email,))
    aluno = cursor.fetchone()

    if aluno:
        print(f"Aluno encontrado: \nID: {aluno[0]}; Nome: {aluno[1]}; Email: {aluno[2]}; Turma: {aluno[3]}; Notas: {aluno[4]}")
        novo_nome = input("Digite o novo nome do aluno (pressione enter para manter nome atual): ").strip().title()
        
        #validando novo email             
        novo_email = input("Digite o novo email do aluno (pressione enter para manter nome atual): ").strip()
        if not novo_email:
            novo_email = aluno[2]
        elif not validar_email(novo_email):
            print("Email invalido. Operação cancelada.")
            return
        
        nova_turma = input("Qual a turma do aluno: ").strip().title()
        
        notas = []
        for i in range(1, 4):
            entrada = input(f"Digite a nota {i} (0 a 10) ou pressione enter para manter: ").strip()
            if entrada == "":
                continue
            try:
                nota = float(entrada)
                if 0 <= nota <= 10:
                    notas.append(nota)
                else:
                    print("A nota deve ser um número entre 0 e 10.")
                    return
            except ValueError:
                print("Valor inválido. Atualização cancelada.")
                return
        #MANTER DADOS ANTIGOS SE USUSARIO DESEJAR:
        nome_final = novo_nome if novo_nome else aluno[1]
        email_final = novo_email if novo_email else aluno[2]
        turma_final = nova_turma if nova_turma else aluno[3]
        notas_final = ",".join(map(str, notas)) if notas else aluno[4]

        cursor.execute("""
            UPDATE alunos SET nome = ?, email = ?, turma = ?, notas = ?
            WHERE email = ? """, (nome_final, email_final, turma_final, notas_final, email))
        conn.commit()                                    
        print("\nAtualizando...")
        print("Dados atualizados com sucesso!")
    else:
        print("Aluno não encontrado")
        
#DELETANDO        
def deletando_aluno(cursor, conn):
    nome = input("Digite o nome do aluno: ").title().strip()
    cursor.execute("SELECT * FROM alunos WHERE nome =?", (nome,))
    aluno = cursor.fetchone()
    if aluno:
        print("\nDeletando...")
        cursor.execute("DELETE FROM alunos WHERE nome =?", (nome,))
        print(f"Aluno {nome} deletado com sucesso")
    else:
        print("Aluno não encontrado.")
    conn.commit()

#ANALIZANDO DADOS
def media_notas(cursor):    
    cursor.execute("SELECT nome, notas FROM alunos")
    alunos = cursor.fetchall()
    aprovados = []
    reprovados = []
    recuperacao = []
    for nome, notas_str in alunos:
        notas = list(map(float, notas_str.split(",")))
        media = sum(notas) / len(notas)
        if media >= 7:
            aprovados.append((nome, media))
        elif media >= 5:
            recuperacao.append((nome, media))
        elif media <= 4.9:
            reprovados.append((nome, media))
                
    print("\nLista de aprovados: ")
    print(f"{'Nome':<20}{'Media':>5}")
    print("-" * 26)
    for nome, media in aprovados:            
        print(f"{nome:<20}{media: >5.1f}")
    print("-" * 26)    
    print("\nLista de reprovados: ")
    print(f"{'Nome':<20}{'Media':>5}")
    print("-" * 26)
    for nome, media in reprovados:
        print(f"{nome:<20}{media: >5.1f}")
    print("-" * 26)            
    print("\nLista de recuperacao: ")
    print(f"{'Nome':<20}{'Media':>5}")
    print("-" * 26)
    for nome, media in recuperacao:
        print(f"{nome:<20}{media: >5.1f}")    


with sqlite3.connect("cadastroAluno.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            turma TEXT NOT NULL,
            notas TEXT NOT NULL
        )
    """)
    
    #INSERINDO DADOS
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("João", "joao@email.com", "A1", "8,5,10")
    )
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("Maria", "maria@email.com", "B1", "1,10,10")
    )
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("Jose", "jose@email.com", "C1", "8.1,5.9,10")
    )
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("Ana", "ana@email.com", "A1", "7.7,7.5,10")
    )
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("Teste", "teste@email.com", "B1", "2,2,2")
    )
    cursor.execute(
        "INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)",
        ("Teste2", "teste2@email.com", "C1", "5,5,5")
    )


#MENU:
def main(cursor, conn):
    while True:
        print("\nBem vindo ao arquivo da escola.")
        print("1- Exibir lista de alunos ")
        print("2- Inserir novo aluno")
        print("3- Deletar aluno")
        print("4- Alterar aluno")
        print("5- Calcular média dos alunos")
        print("6- Buscar aluno")
        print("7- SAIR")
        print("-" * 30)
        try:
            escolha = int(input("\nQual ação deseja realizar? "))
            if escolha in [1, 2, 3, 4, 5, 6, 7]:
                if escolha == 1:
                    print("\nAlunos cadastrados:")
                    exibindo_lista(cursor)
                    print("-" * 30)
                elif escolha == 2:
                    print("\nInserindo novo aluno:")
                    inserindo_aluno(cursor, conn)                            
                    print("-" * 30)
                elif escolha == 3:
                    print("\nDeletar aluno:")
                    deletando_aluno(cursor, conn)
                    print("-" * 30)
                elif escolha == 4:
                    print("\nAlterar aluno:")
                    alterando_aluno(cursor, conn)
                    print("-" * 30)
                elif escolha == 5:
                    print("\nCalculando média dos alunos:")
                    media_notas(cursor)
                    print("-" * 26)
                elif escolha == 6:
                    print("\nBuscar aluno")
                    exibir_aluno(cursor)
                    print("-" * 26)
                elif escolha == 7:
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
                
main(cursor, conn)
