from psycopg2 import connect, OperationalError
import re


def get_connection(dbname, username):
    """
    Return connection with params dbname and username.
    Validation of connection string happens here!

    :param dbname:
    :param username:
    :return: connection or None
    """
    if _clean_connection_string(dbname) and _clean_connection_string(username):
        try:
            conn = connect(f"dbname={dbname} user={username}")
        except OperationalError:
            # TODO log this
            print(f"Could not connect to {username}@{dbname} (dbmodule.py:get_connection)")
            return None
        return conn
    return None


def test_connection(dbname=None, username=None):
    try:
        conn = get_connection(dbname=dbname, username=username)
        if conn:
            conn.close()
            return True
    except OperationalError:
        pass
    return False


def _clean_connection_string(string: str):
    # allowed characters a-z, A-Z, 0-9, _
    # a-z0-9_ allowed in table names
    # you need : for casting, () for obv. reasons
    exp = r'^[a-zA-Z0-9_]+$'
    return re.match(exp, string)
