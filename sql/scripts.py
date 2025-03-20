import sqlite3

def criar_banco():
    try:
        # Conectar ao banco de dados (ou criar se não existir)
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()
        
        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        
        # Confirmar e fechar conexão
        conexao.commit()
        conexao.close()
        print("Banco de dados criado com sucesso!")
    
    except sqlite3.Error as erro:
        print(f"Erro ao criar o banco de dados: {erro}")

def popular_banco():
    try:
        conexao = sqlite3.connect("cadastro.db")
        cursor = conexao.cursor()
        
        usuarios = [
            ("Alice", "alice@email.com", "senha123"),
            ("Bob", "bob@email.com", "senha456"),
            ("Carlos", "carlos@email.com", "senha789")
        ]
        
        cursor.executemany("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", usuarios)
        
        conexao.commit()
        conexao.close()
        print("Banco de dados populado com sucesso!")
    
    except sqlite3.Error as erro:
        print(f"Erro ao popular o banco de dados: {erro}")

# Chamando as funções
criar_banco()
popular_banco()
