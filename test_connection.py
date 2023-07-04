# https://www.psycopg.org/docs/usage.html
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

# Connect to existing database
conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("SELECT * FROM Exercises;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
cur.close()
conn.close()