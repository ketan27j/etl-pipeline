from .common.utils import get_postgres_connection
from common import DB_CONFIG

# Initialize the database connection
get_postgres_connection(
    host=DB_CONFIG['host'],
    database=DB_CONFIG['database'],
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password']
)
