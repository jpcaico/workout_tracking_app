import streamlit as st
from user import *
from workout import *
import pandas as pd


def register_user():
    #st.title("Register User")
    name = st.sidebar.text_input("Name", max_chars=50)
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
    weight = st.sidebar.number_input("Weight (kg)", min_value=0.0)
    height = st.sidebar.number_input("Height (cm)", min_value=0.0)
    bodyfat = st.sidebar.number_input("Body Fat (%)", min_value=0.0, max_value=100.0)

    if st.sidebar.button("Register"):
        register_user_db(name=name, age=age, weight=weight, height=height, bodyfat=bodyfat)
        st.write("User registered successfully.")

def update_user():
   #st.title("Update User")
    user_id = st.sidebar.number_input("User ID", min_value=1, step=1)
    name = st.sidebar.text_input("Name", max_chars=50)
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
    weight = st.sidebar.number_input("Weight (kg)", min_value=0.0)
    height = st.sidebar.number_input("Height (cm)", min_value=0.0)
    bodyfat = st.sidebar.number_input("Body Fat (%)", min_value=0.0, max_value=100.0)

    if st.sidebar.button("Update"):
        # Code for updating a 
        update_user_db(user_id=user_id, name=name, age=age, weight=weight, height=height, bodyfat=bodyfat)
        st.write(f"User {user_id} updated successfully.")

def delete_user():
    #st.title("Delete User")
    user_id = st.sidebar.number_input("User ID", min_value=1, step=1)

    if st.sidebar.button("Delete"):
        # Code for deleting a user
        delete_user_db(user_id=user_id)
        st.write(f"User {user_id} deleted successfully.")

def user_management_tab():
    #st.title("User Management")
    action = st.sidebar.selectbox("Select an action:", ["Register User", "Update User", "Delete User"])

    if action == "Register User":
        register_user()
    elif action == "Update User":
        update_user()
    elif action == "Delete User":
        delete_user()

def register_aerobic_workout():
    #st.title("Register Aerobic Workout")

    user_id = st.sidebar.number_input("User ID", min_value=1, step=1)
    workout_type = st.sidebar.selectbox("Workout Type", ['Cardio','Conditioning','Performance'])
    session_time = st.sidebar.text_input("Session duration (min)")

    activity_name = st.sidebar.selectbox("Activity", get_aerobic_activity_db())

    activity_id = get_aerobic_activity_id_db(activity_name=activity_name)

    training_equipment_type = st.sidebar.text_input("Training Description", max_chars=20)
    is_hiit = st.sidebar.checkbox("Is HIIT?")
    avg_speed = st.sidebar.number_input("Average Speed", min_value=0.0)
    max_speed = st.sidebar.number_input("Max Speed", min_value=0.0)
    lowest_speed = st.sidebar.number_input("Lowest Speed", min_value=0.0)
    resistance_level = st.sidebar.number_input("Resistance Level", min_value=0.0)
    rpe_overall = st.sidebar.selectbox("RPE Overall", ["Very Light", "Light", "Average", "Hard", "Very Hard"])

    if st.sidebar.button("Register"):

        training_data_cardio = [{'activity_id':activity_id,
                        'training_type':training_equipment_type,
                        'is_hiit':is_hiit,
                        'avg_speed':avg_speed,
                        'max_speed':max_speed,
                        'lowest_speed':lowest_speed,
                        'resistance_level':resistance_level,
                        'rpe_overall':rpe_overall}]
        
        # Code for registering an aerobic workout
        
        register_aerobic_workout_db(user_id=user_id,
                                    training_type=workout_type,
                                    session_time=session_time,
                                    training_data=training_data_cardio)
        st.write("Aerobic Workout registered successfully.")

def update_aerobic_workout():
   # st.title("Update Aerobic Workout")
    workout_id = st.sidebar.number_input("Workout ID", min_value=1, step=1)
    workout_type = st.sidebar.selectbox("Workout Type", ['Cardio','Conditioning','Performance'])
    session_time = st.sidebar.text_input("Session duration (min)")
    activity_name = st.sidebar.selectbox("Activity", get_aerobic_activity_db())
    activity_id = get_aerobic_activity_id_db(activity_name=activity_name)
    training_equipment_type = st.sidebar.text_input("Training Description", max_chars=20)
    is_hiit = st.sidebar.checkbox("Is HIIT?")
    avg_speed = st.sidebar.number_input("Average Speed", min_value=0.0)
    max_speed = st.sidebar.number_input("Max Speed", min_value=0.0)
    lowest_speed = st.sidebar.number_input("Lowest Speed", min_value=0.0)
    resistance_level = st.sidebar.number_input("Resistance Level", min_value=0.0)
    rpe_overall = st.sidebar.selectbox("RPE Overall", ["Very Light", "Light", "Average", "Hard", "Very Hard"])
    if st.sidebar.button("Update"):

        training_data_cardio = [{'activity_id':activity_id,
                'training_type':training_equipment_type,
                'is_hiit':is_hiit,
                'avg_speed':avg_speed,
                'max_speed':max_speed,
                'lowest_speed':lowest_speed,
                'resistance_level':resistance_level,
                'rpe_overall':rpe_overall}]
        # Code for updating an aerobic workout
        update_aerobic_workout_db(workout_id=workout_id,
                                  training_type=workout_type,
                                  session_time=session_time,
                                  training_data=training_data_cardio)

        st.write(f"Aerobic Workout {workout_id} updated successfully.")

def delete_aerobic_workout():
    #st.title("Delete Aerobic Workout")

    workout_id = st.sidebar.number_input("Workout ID", min_value=1, step=1)

    if st.sidebar.button("Delete"):
        # Code for deleting an aerobic workout
        delete_aerobic_workout_db(workout_id=workout_id)
        st.write(f"Aerobic Workout {workout_id} deleted successfully.")

# def register_weight_workout():
#     #st.title("Register Weight Workout")

#     user_id = st.sidebar.number_input("User ID", min_value=1, step=1)
#     training_type = st.sidebar.text_input("Training Type")
#     session_time = st.sidebar.text_input("Session Time")
#     exercise_id = st.number_input("Exercise ID", min_value=1, step=1)
#     sets = st.sidebar.number_input("Sets", min_value=1, step=1)
#     repetitions_per_set = st.sidebar.number_input("Repetitions per Set", min_value=1, step=1)
#     weight = st.sidebar.number_input("Weight", min_value=0.0, step=0.1)
#     rest_time = st.sidebar.number_input("Rest Time", min_value=0.0, step=0.1)
#     rpe_exercise = st.sidebar.selectbox("RPE Exercise", ["Very Light", "Light", "Average", "Hard", "Very Hard"])
#     rpe_overall = st.sidebar.selectbox("RPE Overall", ["Very Light", "Light", "Average", "Hard", "Very Hard"])


#     if st.sidebar.button('Register'):
#         # Code for registering a weight workout
#         st.write("Weight Workout registered successfully.")

def register_weight_workout():
    # st.title("Register Weight Workout")

    user_id = st.sidebar.number_input("User ID", min_value=1, step=1)
    training_type = st.sidebar.selectbox("Training Type", ['Strength','Hypertrophy','Adaptation'])
    session_time = st.sidebar.text_input("Session duration (min)")

    num_exercises = st.sidebar.number_input("Number of Exercises", min_value=1, step=1)
    exercises = []

    for i in range(num_exercises):
        exercise_name = st.sidebar.selectbox(f"Exercise Name {i+1}", get_weight_exercise_db())
        exercise_id = get_weight_exercise_id_db(exercise_name=exercise_name)
        sets = st.sidebar.number_input(f"Sets for Exercise {i+1}", min_value=1, step=1)
        repetitions_per_set = st.sidebar.number_input(f"Repetitions per Set for Exercise {i+1}", min_value=1, step=1)
        weight = st.sidebar.number_input(f"Weight for Exercise {i+1}", min_value=0.0, step=0.1)
        rest_time = st.sidebar.number_input(f"Rest Time for Exercise {i+1}", min_value=0.0, step=0.1)
        rpe_exercise = st.sidebar.selectbox(f"RPE Exercise for Exercise {i+1}", ["Very Light", "Light", "Average", "Hard", "Very Hard"])
        rpe_overall = st.sidebar.selectbox(f"RPE Overall for Exercise {i+1}", ["Very Light", "Light", "Average", "Hard", "Very Hard"])

        exercise = {
            "exercise_id": exercise_id,
            "sets": sets,
            "repetitions_per_set": repetitions_per_set,
            "weight": weight,
            "rest_time": rest_time,
            "rpe_exercise": rpe_exercise,
            "rpe_overall": rpe_overall
        }
        exercises.append(exercise)

    if st.sidebar.button('Register'):
        # Code for registering a weight workout
        register_weight_workout_db(user_id=user_id,
                                   training_type=training_type,
                                   session_time=session_time,
                                   training_data=exercises)
        st.write("Weight Workout registered successfully.")
       # st.write("Exercises:", exercises)



def update_weight_workout():
    #st.title("Update Weight Workout")
    workout_id = st.sidebar.number_input("Workout ID", min_value=1, step=1)
    training_type = st.sidebar.selectbox("Training Type", ['Strength','Hypertrophy','Adaptation'])
    session_time = st.sidebar.text_input("Session duration (min)")


    num_exercises = st.sidebar.number_input("Number of Exercises", min_value=1, step=1)
    exercises = []

    for i in range(num_exercises):
        exercise_name = st.sidebar.selectbox(f"Exercise Name {i+1}", get_weight_exercise_db())
        exercise_id = get_weight_exercise_id_db(exercise_name=exercise_name)
        sets = st.sidebar.number_input(f"Sets for Exercise {i+1}", min_value=1, step=1)
        repetitions_per_set = st.sidebar.number_input(f"Repetitions per Set for Exercise {i+1}", min_value=1, step=1)
        weight = st.sidebar.number_input(f"Weight for Exercise {i+1}", min_value=0.0, step=0.1)
        rest_time = st.sidebar.number_input(f"Rest Time for Exercise {i+1}", min_value=0.0, step=0.1)
        rpe_exercise = st.sidebar.selectbox(f"RPE Exercise for Exercise {i+1}", ["Very Light", "Light", "Average", "Hard", "Very Hard"])
        rpe_overall = st.sidebar.selectbox(f"RPE Overall for Exercise {i+1}", ["Very Light", "Light", "Average", "Hard", "Very Hard"])

        exercise = {
            "exercise_id": exercise_id,
            "sets": sets,
            "repetitions_per_set": repetitions_per_set,
            "weight": weight,
            "rest_time": rest_time,
            "rpe_exercise": rpe_exercise,
            "rpe_overall": rpe_overall
        }
        exercises.append(exercise)

    # exercise_id = st.sidebar.number_input("Exercise ID", min_value=1, step=1)
    # sets = st.sidebar.number_input("Sets", min_value=1, step=1)
    # repetitions_per_set = st.sidebar.number_input("Repetitions per Set", min_value=1, step=1)
    # weight = st.sidebar.number_input("Weight", min_value=0.0)
    # rest_time = st.sidebar.number_input("Rest Time", min_value=0.0)
    # rpe_exercise = st.sidebar.selectbox("RPE Exercise", ["Very Light", "Light", "Average", "Hard", "Very Hard"])
    # rpe_overall = st.sidebar.selectbox("RPE Overall", ["Very Light", "Light", "Average", "Hard", "Very Hard"])

    if st.sidebar.button("Update"):
        # Code for updating a weight workout
        update_weight_workout_db(workout_id=workout_id,
                                 training_type=training_type,
                                 session_time=session_time,
                                 training_data=exercises)
        st.write(f"Weight Workout {workout_id} updated successfully.")

def delete_weight_workout():
    #st.title("Delete Weight Workout")
    workout_id = st.sidebar.number_input("Workout ID", min_value=1, step=1)

    if st.sidebar.button("Delete"):
        # Code for deleting a weight workout
        delete_weight_workout_db(workout_id=workout_id)
        st.write(f"Weight Workout {workout_id} deleted successfully.")

def workout_management_tab():
    #st.title("Workout Management")
    action = st.sidebar.selectbox("Select an action:", ["Register Workout", "Update Workout", "Delete Workout"])
    workout_type = st.sidebar.selectbox("Select a workout type:", ["Aerobic Workout", "Weight Workout"])

    if workout_type == "Aerobic Workout":
        if action == "Register Workout":
            register_aerobic_workout()
        elif action == "Update Workout":
            update_aerobic_workout()
        elif action == "Delete Workout":
            delete_aerobic_workout()
    elif workout_type == "Weight Workout":
        if action == "Register Workout":
            register_weight_workout()
        elif action == "Update Workout":
            update_weight_workout()
        elif action == "Delete Workout":
            delete_weight_workout()

# Main app
#st.title("Discipulos do FEROMOX")
# Create tabs
tabs = ["User Management", "Workout Management"]
selected_tab = st.sidebar.radio("Select a tab", tabs)

# Display selected tab
if selected_tab == "User Management":
    user_management_tab()
elif selected_tab == "Workout Management":
    workout_management_tab()

# Create tabs
tabs_main = ["User Table", "Workout Tables"]
selected_tab = st.radio("Select tab", tabs_main)

def convert_df_to_csv(df):
  return df.to_csv().encode('utf-8')

# Display selected tab
if selected_tab == "User Table":
   df_user = render_user_table()
   st.text('Users')
   st.write(df_user) 
   st.download_button(
   label="Download Users",
   data=convert_df_to_csv(df_user),
   file_name='df_workout.csv',
   mime='text/csv',
    )


elif selected_tab == "Workout Tables":
    df_workout = render_workout_table()
    df_weight = render_weight_workout_table()
    df_aerobic = render_aerobic_workout_table()

    st.text('Workout')
    st.write(df_workout) 
    st.download_button(
    label="Download Workout",
    data=convert_df_to_csv(df_workout),
    file_name='df_workout.csv',
    mime='text/csv',
    )
    st.text('Weight Training')
    st.write(df_weight) 
    st.download_button(
    label="Download Weight",
    data=convert_df_to_csv(df_weight),
    file_name='df_weight.csv',
    mime='text/csv',
    )
    st.text('Aerobic Training')
    st.write(df_aerobic) 
    st.download_button(
    label="Download Aerobic",
    data=convert_df_to_csv(df_aerobic),
    file_name='aerobic.csv',
    mime='text/csv',
    )

st.image("ramondino.jpg", caption="Fica grande porra")