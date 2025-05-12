import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="Mineradora"
    )

def inserir(entidade, dados):
    conn = conectar()
    cursor = conn.cursor()

    if entidade == "Maquinas":
        cursor.execute("INSERT INTO maquinas (nome_maquina, capacidade_operacional, custo_aluguel_dia, custo_transporte) VALUES (%s, %s, %s, %s)", dados)
    elif entidade == "Materiais":
        cursor.execute("INSERT INTO materiais (nome_material, tipo, dureza) VALUES (%s, %s, %s)", dados)
    elif entidade == "Clientes":
        cursor.execute("INSERT INTO clientes (nome_cliente, cpf) VALUES (%s, %s)", dados)

    conn.commit()
    conn.close()

def consultar(entidade):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM {entidade.lower()}")
    resultados = cursor.fetchall()

    conn.close()
    return resultados

def excluir(entidade, id_item):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {entidade.lower()} WHERE id = %s", (id_item,))
    conn.commit()
    conn.close()

def editar(entidade, id_item, novos_dados):
    conn = conectar()
    cursor = conn.cursor()

    if entidade == "Maquinas":
        cursor.execute("""
            UPDATE maquinas SET nome_maquina=%s, capacidade_operacional=%s, custo_aluguel_dia=%s, custo_transporte=%s WHERE id=%s
        """, (*novos_dados, id_item))
    elif entidade == "Materiais":
        cursor.execute("""
            UPDATE materiais SET nome_material=%s, tipo=%s, dureza=%s WHERE id=%s
        """, (*novos_dados, id_item))
    elif entidade == "Clientes":
        cursor.execute("""
            UPDATE clientes SET nome_cliente=%s, cpf=%s WHERE id=%s
        """, (*novos_dados, id_item))

    conn.commit()
    conn.close()
