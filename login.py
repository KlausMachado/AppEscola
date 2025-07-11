import sqlite3
from validacoes import validar_email


with sqlite3.connect("usuarios.db") as conn:
    cursor = conn.cursor()
    
    def conectar_banco(nome_banco="usuarios.db"):
        return sqlite3.connect(nome_banco)
            
    def criar_tabela_usuarios():
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """)
    
    def cadastrar_usuario():
        nome = input("Usuario: ").title().strip()
        while True:
            email = input("Email: ").strip()
            
            if not validar_email(email):
                print("Email invalido. Digite novamente.")
                continue
            
            cursor.execute("SELECT * FROM usuarios WHERE email =?", (email,))
            if cursor.fetchone():
                print("Este e-mail já está cadastrado. Digite outro.")
                continue
            break
        senha = input("Senha: ").strip()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        print(f"\nUsuario {nome} inserido com sucesso!")
    
    def login_usuario():
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
            
        cursor.execute("SELECT nome FROM usuarios WHERE email=? AND senha=?", (email, senha))
        resultado = cursor.fetchone()

        if resultado:
            print(f"Bem vindo(a), {resultado[0]}")
            return True
        else:
            print("Usuario não encontrado")
            return False
            
            
#------dados de teste usuario-------
    def inserir_dados_teste_usuarios():
        dados = [
            ("Usuario 1", "usuario1@email.com", "123"),
            ("Usuario 2", "usuario2@email.com", "123"),
            ("Usuario 3", "usuario3@email.com", "123"),
            ("Usuario 4", "usuario4@email.com", "123")
        ]
        for usuario in dados:
            try:
                cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (usuario))
            except sqlite3.IntegrityError:
                continue
