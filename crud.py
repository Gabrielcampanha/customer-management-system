import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        port=int(os.environ.get('MYSQL_PORT', 3306))
    )

# CREATE
def create_customer(nome, idade):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO customers (nome, idade) VALUES (%s, %s)'
            cursor.execute(sql, (nome, idade))
        conn.commit()

# READ
def get_customers():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM customers')
            result = cursor.fetchall()

            return [
                {"id": row[0], "nome": row[1], "idade": row[2]}
                for row in result
            ]

# UPDATE
def update_customer(id, idade):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            sql = 'UPDATE customers SET idade=%s WHERE id=%s'
            cursor.execute(sql, (idade, id))
        conn.commit()

# DELETE
def delete_customer(id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            sql = 'DELETE FROM customers WHERE id=%s'
            cursor.execute(sql, (id,))
        conn.commit()

def clear_table():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE customers')
        conn.commit()

def get_customers_by_range(inicio, fim):
    conn = get_connection()

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, nome, idade FROM customers WHERE id BETWEEN %s AND %s",
                (inicio, fim)
            )

            rows = cursor.fetchall()

            return [
                {"id": r[0], "nome": r[1], "idade": r[2]}
                for r in rows
            ]
        
def create_customers_bulk(clientes):
    conn = get_connection()

    with conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO customers (nome, idade)
                VALUES (%s, %s)
            """

            valores = [(c['nome'], c['idade']) for c in clientes]

            cursor.executemany(sql, valores)

        conn.commit()