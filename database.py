import sqlite3
def conectar_banco(nome_banco="cadastroAluno.db"):
    return sqlite3.connect(nome_banco)
    
def criar_tabela(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            turma TEXT NOT NULL,
            notas TEXT NOT NULL
        )
    """)

def inserir_dados_iniciais(cursor):
    dados = [
        ("João", "joao@email.com", "A1", "8,5,10"),
        ("Maria", "maria@email.com", "B1", "1,10,10"),
        ("Jose", "jose@email.com", "C1", "8.1,5.9,10"),
        ("Ana", "ana@email.com", "A1", "7.7,7.5,10"),
        ("Teste", "teste@email.com", "B1", "2,2,2"),
        ("Teste2", "teste2@email.com", "C1", "5,5,5")
    ]
    for aluno in dados:
        try:
            cursor.execute("INSERT INTO alunos (nome, email, turma, notas) VALUES (?, ?, ?, ?)", (aluno))
        except sqlite3.IntegrityError:
            continue
