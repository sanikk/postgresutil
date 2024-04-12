from psycopg2 import OperationalError
from psycopg2.sql import SQL, Identifier
from dotenv import load_dotenv
from os import getenv
from sql_filler.db_connection import get_connection


load_dotenv()


def test_connection(dbname=None, username=None):
    try:
        conn = get_connection(dbname=dbname, username=username)
        if conn:
            conn.close()
            return True
    except OperationalError:
        pass
    return False


#def insert_independent(table_name, column_list, values):
#    conn, cur = get_connection()
#
#    columns_sql = ", ".join(column_list)
#    sql = f"INSERT INTO %s ({','.join(column_list)}) VALUES ({','.join(['%s' for a in column_list])})"
#    cur.execute(sql, (table_name, *values,))
#    conn.commit()
#    cur.close()
#    conn.close()


def inserter(table=None, values=None):
    if not table:
        return
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO {} VALUES (%s)"
            cur.execute(SQL(sql).format(Identifier(table)), values)


def list_tables(user):
    conn, cur = get_connection()
    sql = "SELECT tablename from pg_catalog.pg_tables WHERE tableowner=%s"
    cur.execute(sql, (user,))
    return cur.fetchall()

def get_foreign_keys(user):
    conn, cur = get_connection()
    sql = 'se'
