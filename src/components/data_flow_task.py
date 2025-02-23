from common import get_postgres_connection, fetch_data_from_table, log_message
from config import DB_CONFIG
import psycopg2.extras

def filter_columns(data, columns):
    filtered_data = []
    for row in data:
        filtered_row = {col: row[col] for col in columns}
        filtered_data.append(filtered_row)
    return filtered_data

def data_flow_task(source_query, destination_table, columns):
    connection = get_postgres_connection(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    
    if connection is None:
        log_message("Failed to establish database connection.", level='ERROR')
        return
    
    data = fetch_data_from_table(source_query)
    if data is None:
        log_message("No data fetched from source.", level='ERROR')
        return
    
    filtered_data = filter_columns(data, columns)
    
    try:
        cursor = connection.cursor()
        insert_query = f"INSERT INTO {destination_table} ({', '.join(columns)}) VALUES %s"
        psycopg2.extras.execute_values(cursor, insert_query, [tuple(row[col] for col in columns) for row in filtered_data])
        connection.commit()
        cursor.close()
        log_message(f"Data successfully inserted into {destination_table}.")
    except Exception as error:
        log_message(f"Error inserting data into {destination_table}: {error}", level='ERROR')
