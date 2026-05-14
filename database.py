import sqlite3
from cliente import Cliente

def conectar():
    return sqlite3.connect('clientes.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
                   (cliente.nome, cliente.email, cliente.telefone))
    conn.commit()
    cliente.id = cursor.lastrowid
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email, telefone FROM clientes')
    rows = cursor.fetchall()
    conn.close()
    return [Cliente(nome=row[1], email=row[2], telefone=row[3], id=row[0]) for row in rows]

def buscar_cliente_por_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email, telefone FROM clientes WHERE id = ?', (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Cliente(nome=row[1], email=row[2], telefone=row[3], id=row[0])
    return None

def atualizar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?',
                   (cliente.nome, cliente.email, cliente.telefone, cliente.id))
    conn.commit()
    conn.close()

def deletar_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def buscar_cliente(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email, telefone FROM clientes WHERE nome LIKE ?', ('%' + nome + '%',))
    rows = cursor.fetchall()
    conn.close()
    return [Cliente(nome=row[1], email=row[2], telefone=row[3], id=row[0]) for row in rows]  

def buscar_cliente(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE nome LIKE ?",
        ('%' + nome + '%',)
    )

    clientes = cursor.fetchall()

    conn.close()

    return clientes
