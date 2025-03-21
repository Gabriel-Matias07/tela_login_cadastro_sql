from flask import Flask, request, jsonify
import sqlite3 as sql


app = Flask(__name__)
def criar_banco():
    try:
        # Conectar ao banco de dados (ou criar se não existir)
        conexao = sql.connect("cadastro.db")
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
    
    except sql.Error as erro:
        print(f"Erro ao criar o banco de dados: {erro}")

def popular_banco():
    try:
        conexao = sql.connect("cadastro.db")
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
    
    except sql.Error as erro:
        print(f"Erro ao popular o banco de dados: {erro}")

# Rota para adicionar usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')

    conn = sql.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuário adicionado com sucesso!'})

# Rota para listar usuários
@app.route('/users', methods=['GET'])
def get_users():
    conn = sql.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM usuarios")
    users = cursor.fetchall()
    conn.close()

    # Converter para um formato adequado para o frontend
    users_list = [{"id": row[0], "name": row[1]} for row in users]

    return jsonify(users_list)

