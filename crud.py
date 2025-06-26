from utils import validar_email, validar_nota, media_notas

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
        for i in range(3):
            while True:
                entrada = input(f"Digite a nota {i + 1} (0 a 10): ")
                nota = validar_nota(entrada)
                if nota is not None:
                    notas.append(nota)
                    break
                            
        notas_str = ",".join(map(str, notas))
        cursor.execute("INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)", (nome, email, turma, notas_str))
        conn.commit()
        print(f"\nAluno {nome} inserido com sucesso!")

        continuar = input("Deseja adicionar outro aluno? (s/n)").lower()
        if continuar != 's':
            break
        
#EXIBINDO DADOS
def listar_alunos(cursor):       
    cursor.execute("SELECT * FROM alunos") 
    aluno = cursor.fetchall()
    for id, nome, email, turma, notas in aluno:
        print(f"Aluno {id}:\n{nome}; \n{email}; \nTurma: {turma} \nNotas: {notas};\n")

def buscar_aluno_por_nome(cursor):
    nome = input("Digite o nome do aluno que deseja buscar: ").title().strip()
    cursor.execute("SELECT nome, turma, notas FROM alunos WHERE nome=?", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        media = media_notas(resultado[2])
        print(f"\n{resultado[0]} - Notas: {resultado[2]} | Média: {media:.1f} | Turma: {resultado[1]}") 
    else:
        print("Aluno não encontrado")
        
def buscar_por_turma(cursor):
    turma = input("Qual turma deseja buscar? ").title().strip()
    cursor.execute("SELECT * FROM alunos WHERE turma=?", (turma,))
    resultado = cursor.fetchall()
    if resultado:
        for id, nome, email, turma, notas_str in resultado:
            media = media_notas(notas_str)
            print(f"\nAluno {id}:\n{nome}; \n{email}; \nTurma: {turma} \nNotas: {notas_str};\nMedia: {media:.1f}")
    else:
        print("\nTurma não encontrada!")

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
        
        nova_turma = input("Digite a nova turma do aluno (pressione enter para manter nome atual): ").strip().title()
        
        notas_antigas = list(map(float, aluno[4].split(",")))
        notas = []
        for i in range(3):
            while True:
                entrada = input(f"Digite a nova nota {i + 1} (0 a 10) ou pressione enter para manter [{notas_antigas[i]}]: ").strip()
                if entrada == "":
                    notas.append(notas_antigas[i])
                    break
                nota = validar_nota(entrada)
                if nota is not None:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Tente novamente.")
                
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
def deletar_aluno(cursor, conn):
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
