import dj_database_url
import psycopg2
import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env()

user = env.str('DJANGO_DB_USER')
password = env.str('DJANGO_DB_PASSWORD')

# URL de tu base de datos PostgreSQL
url = f'postgres://{user}:{password}@localhost:5432/coffeeshop'

# Parsear la URL con dj_database_url
config = dj_database_url.parse(url)

# Conectar usando psycopg2 con los datos que generó dj_database_url
try:
    conn = psycopg2.connect(
        dbname=config['NAME'],
        user=config['USER'],
        password=config['PASSWORD'],
        host=config['HOST'],
        port=config['PORT']
    )
    print("✅ Conexión exitosa")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
