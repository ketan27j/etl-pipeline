from .log_utils import log_message

def get_postgres_connection(host, database, user, password):
    global _connection
    import psycopg2
    if _connection is None:
        try:
            _connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
        except Exception as error:
            log_message(f"Error connecting to PostgreSQL database: {error}", level='ERROR')
            _connection = None
    return _connection

def fetch_data_from_table(query, params=None):
    connection = get_postgres_connection()
    if connection is None:
        log_message("No database connection available.", level='ERROR')
        return None
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        cursor.close()
        return data
    except Exception as error:
        log_message(f"Error fetching data from table: {error}", level='ERROR')
        return None
