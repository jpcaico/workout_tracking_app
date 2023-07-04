import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

def render_user_table():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users")
        query_result = cursor.fetchall()
        
        # Create a DataFrame from the query result
        df = pd.DataFrame(query_result, columns=[desc[0] for desc in cursor.description])
        
        return df
    
    except (psycopg2.Error, pd.Error) as error:
        print("Error fetching data from the database:", error)
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


def register_user_db(name, age, weight, height, bodyfat):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Users (name, age, weight, height, bodyfat) VALUES (%s, %s, %s, %s, %s) RETURNING user_id",
                       (name, age, weight, height, bodyfat))
        user_id = cursor.fetchone()[0]
        conn.commit()
        print(f"User registered successfully with ID: {user_id}")
    except Exception as e:
        conn.rollback()
        print(f"Failed to register user: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def update_user_db(user_id, name, age, weight, height, bodyfat):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE Users SET name = %s, age = %s, weight = %s, height = %s, bodyfat = %s WHERE user_id = %s",
                       (name, age, weight, height, bodyfat, user_id))
        conn.commit()
        print("User updated successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to update user: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def delete_user_db(user_id):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
        conn.commit()
        print("User deleted successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to delete user: {str(e)}")
    finally:
        cursor.close()
        conn.close()
