import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")


def get_aerobic_activity_db():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT DISTINCT activity_name FROM AerobicActivities;")
        activity_names = cursor.fetchall()
        activity_names = [activity[0] for activity in activity_names]
        return activity_names
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error retrieving aerobic activities:", error)
    finally:
        cursor.close()
        conn.close()

def get_aerobic_activity_id_db(activity_name):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"SELECT DISTINCT activity_id FROM AerobicActivities WHERE activity_name = '{activity_name}';")
        activity_id = cursor.fetchone()[0]
        return activity_id
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error retrieving aerobic activities:", error)
    finally:
        cursor.close()
        conn.close()



def register_aerobic_workout_db(user_id, training_type, session_time, training_data):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        # Insert into Workouts table
        timestamp = datetime.now()
        cursor.execute("INSERT INTO Workouts (timestamp, training_type, session_time, user_id) VALUES (%s, %s, %s, %s) RETURNING workout_id",
                       (timestamp, training_type, session_time, user_id))
        workout_id = cursor.fetchone()[0]
        
        # Insert into AerobicTraining table
        for activity in training_data:
            activity_id = activity["activity_id"]
            training_type = activity["training_type"]
            is_hiit = activity["is_hiit"]
            avg_speed = activity["avg_speed"]
            max_speed = activity["max_speed"]
            lowest_speed = activity["lowest_speed"]
            resistance_level = activity["resistance_level"]
            rpe_overall = activity["rpe_overall"]
            
            cursor.execute("INSERT INTO AerobicTraining (workout_id, activity_id, training_type, is_hiit, avg_speed, max_speed, lowest_speed, resistance_level, rpe_overall) \
                            VALUES (%s, %s, %s ,%s, %s, %s, %s, %s, %s)",
                           (workout_id, activity_id, training_type, is_hiit, avg_speed, max_speed, lowest_speed, resistance_level, rpe_overall))
        
        conn.commit()
        print("Aerobic workout registered successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to register aerobic workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def update_aerobic_workout_db(workout_id, training_type=None, session_time=None, training_data=None):
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cursor = conn.cursor()

    try:
        # Update the Workouts table if training_type or session_time is provided
        if training_type or session_time:
            update_query = "UPDATE Workouts SET"
            update_values = []

            if training_type:
                update_query += " training_type = %s,"
                update_values.append(training_type)
            if session_time:
                update_query += " session_time = %s,"
                update_values.append(session_time)

            # Remove trailing comma
            update_query = update_query.rstrip(",")

            # Add the WHERE clause for the workout_id
            update_query += " WHERE workout_id = %s"
            update_values.append(workout_id)

            cursor.execute(update_query, tuple(update_values))

        # Update the AerobicTraining table if training_data is provided
        if training_data:
            # Delete existing entries for the workout_id
            cursor.execute("DELETE FROM AerobicTraining WHERE workout_id = %s", (workout_id,))

            # Insert new entries
            for activity in training_data:
                activity_id = activity["activity_id"]
                training_type = activity["training_type"]
                is_hiit = activity["is_hiit"]
                avg_speed = activity["avg_speed"]
                max_speed = activity["max_speed"]
                lowest_speed = activity["lowest_speed"]
                resistance_level = activity["resistance_level"]
                rpe_overall = activity["rpe_overall"]

                cursor.execute(
                    "INSERT INTO AerobicTraining (workout_id, activity_id, training_type, is_hiit, avg_speed, max_speed, lowest_speed, resistance_level, rpe_overall) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (workout_id, activity_id, training_type, is_hiit, avg_speed, max_speed, lowest_speed, resistance_level, rpe_overall))

        conn.commit()
        print("Aerobic workout updated successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to update aerobic workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def delete_aerobic_workout_db(workout_id):
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cursor = conn.cursor()

    try:
        # Delete from AerobicTraining table
        cursor.execute("DELETE FROM AerobicTraining WHERE workout_id = %s", (workout_id,))

        # Delete from Workouts table
        cursor.execute("DELETE FROM Workouts WHERE workout_id = %s", (workout_id,))

        conn.commit()
        print("Aerobic workout deleted successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to delete aerobic workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def render_workout_table():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM Workouts")
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



def render_aerobic_workout_table():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM AerobicTraining")
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



def get_weight_exercise_db():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT DISTINCT exercise_name FROM exercises;")
        exercise_names = cursor.fetchall()
        exercise_names = [exercise[0] for exercise in exercise_names]
        return exercise_names
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error retrieving aerobic activities:", error)
    finally:
        cursor.close()
        conn.close()

def get_weight_exercise_id_db(exercise_name):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"SELECT DISTINCT exercise_id FROM exercises WHERE exercise_name = '{exercise_name}';")
        activity_id = cursor.fetchone()[0]
        return activity_id
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error retrieving aerobic activities:", error)
    finally:
        cursor.close()
        conn.close()


def render_weight_workout_table():
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM WeightTraining")
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
    

def register_weight_workout_db(user_id, training_type, session_time, training_data):
    conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host
    )
    cursor = conn.cursor()
    
    try:
        # Insert into Workouts table
        timestamp = datetime.now()
        cursor.execute("INSERT INTO Workouts (timestamp, training_type, session_time, user_id) VALUES (%s, %s, %s, %s) RETURNING workout_id",
                       (timestamp, training_type, session_time, user_id))
        workout_id = cursor.fetchone()[0]
        
        # Insert into WeightTraining table
        for exercise in training_data:
            exercise_id = exercise["exercise_id"]
            sets = exercise["sets"]
            repetitions_per_set = exercise["repetitions_per_set"]
            weight = exercise["weight"]
            rest_time = exercise["rest_time"]
            rpe_exercise = exercise["rpe_exercise"]
            rpe_overall = exercise["rpe_overall"]
            
            cursor.execute("INSERT INTO WeightTraining (workout_id, exercise_id, sets, repetitions_per_set, weight, rest_time, rpe_exercise, rpe_overall) \
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (workout_id, exercise_id, sets, repetitions_per_set, weight, rest_time, rpe_exercise, rpe_overall))
        
        conn.commit()
        print("Weight training workout registered successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to register weight training workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def update_weight_workout_db(workout_id, training_type=None, session_time=None, training_data=None):
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cursor = conn.cursor()

    try:
        # Update the Workouts table if training_type or session_time is provided
        if training_type or session_time:
            update_query = "UPDATE Workouts SET"
            update_values = []

            if training_type:
                update_query += " training_type = %s,"
                update_values.append(training_type)
            if session_time:
                update_query += " session_time = %s,"
                update_values.append(session_time)

            # Remove trailing comma
            update_query = update_query.rstrip(",")

            # Add the WHERE clause for the workout_id
            update_query += " WHERE workout_id = %s"
            update_values.append(workout_id)

            cursor.execute(update_query, tuple(update_values))

        # Update the WeightTraining table if training_data is provided
        if training_data:
            # Delete existing entries for the workout_id
            cursor.execute("DELETE FROM WeightTraining WHERE workout_id = %s", (workout_id,))

            # Insert new entries
            for exercise in training_data:
                exercise_id = exercise["exercise_id"]
                sets = exercise["sets"]
                repetitions_per_set = exercise["repetitions_per_set"]
                weight = exercise["weight"]
                rest_time = exercise["rest_time"]
                rpe_exercise = exercise["rpe_exercise"]
                rpe_overall = exercise["rpe_overall"]

                cursor.execute(
                    "INSERT INTO WeightTraining (workout_id, exercise_id, sets, repetitions_per_set, weight, rest_time, rpe_exercise, rpe_overall) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (workout_id, exercise_id, sets, repetitions_per_set, weight, rest_time, rpe_exercise, rpe_overall))

        conn.commit()
        print("Weight training workout updated successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to update weight training workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def delete_weight_workout_db(workout_id):
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cursor = conn.cursor()

    try:
        # Delete from WeightTraining table
        cursor.execute("DELETE FROM WeightTraining WHERE workout_id = %s", (workout_id,))

        # Delete from Workouts table
        cursor.execute("DELETE FROM Workouts WHERE workout_id = %s", (workout_id,))

        conn.commit()
        print("Weight training workout deleted successfully")
    except Exception as e:
        conn.rollback()
        print(f"Failed to delete weight training workout: {str(e)}")
    finally:
        cursor.close()
        conn.close()