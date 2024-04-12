from sql_filler.db_connection import get_connection, test_connection
import re


class PostgresService:
    def __init__(self):
        self._dbname = None
        self._username = None

    # public methods
    # Connection
    def try_connection(self, dbname=None, username=None):
        if self._test_connection(dbname=dbname, username=username):
            return True
        return False

    def disconnect(self):
        self._dbname = None
        self._username = None

    def is_connected(self):
        return self._dbname is not None and self._username is not None

    def get_connection_credentials(self):
        return self._dbname, self._username

    # tableFrame
    def get_table_names(self):
        if self.is_connected():
            # select * from pg_catalog.pg_tables
            # schemaname |      tablename       | tableowner | tablespace | hasindexes | hasrules | hastriggers | rowsecurity
            # ------------+----------------------+------------+------------+------------+----------+-------------+-------------
            #  public     | account              | karpo      |            | t          | f        | t           | f
            sql_string = "SELECT tablename from pg_catalog.pg_tables WHERE tableowner=%s"
            if self._username and self._clean_sql_string(sql_string):
                with self._get_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(sql_string, (self._username,))
                        return cur.fetchall()
        return []

    # Tab methods
    def get_information_schema_columns(self):
        sql_string = 'SELECT * FROM information_schema.columns WHERE table_schema=\'public\''
        if self._clean_sql_string(sql_string):
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_string, (self._username,))
                    return cur.fetchall()

    def get_tab2_info(self):
        sql_string = """SELECT ic.table_name, ic.column_name, ic.ordinal_position, ic.column_default, ic.data_type
            FROM information_schema.columns ic
            WHERE columns.table_schema=\'public\'
        """
        if self._clean_sql_string(sql_string):
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_string, (self._username,))
                    return cur.fetchall()
        validation = ('is_nullable, character_maximum_length, character_octet_length, numeric_precision, '
                     'numeric_precision_radix, numeric_scale, datetime_precision, interval_type, interval_precision')
        return ''

    # internal methods

    def _test_connection(self, dbname=None, username=None):
        if test_connection(dbname=dbname, username=username):
            self._dbname = dbname
            self._username = username
            return True
        return False

    def _get_connection(self):
        if self._dbname and self._username:
            return get_connection(dbname=self._dbname, username=self._username)
        return None

    def _clean_sql_string(self, string: str):
        # allowed characters a-z, A-Z, 0-9, _, :, (, ), ., %
        # a-z0-9_ allowed in table names
        # you need : for casting, () for obv. reasons
        # /s tabs, newline
        exp = r'^[a-zA-Z0-9_():\.\=\%\s]+$'
        return re.match(exp, string)
