import sqlite3
import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_X2UbYgofR9yB@ep-plain-pond-ad5snu6t-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn