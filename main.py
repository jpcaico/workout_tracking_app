from user import *
from workout import *


if __name__ == '__main__':

    #register_user(name = 'JP', age=26, weight=80, height=183, bodyfat=15)
    #update_user(user_id=1, name='Joao Paulo', age=26, weight=26, height=183, bodyfat=16)
    #delete_user(user_id=1)
    aerobic_training = [{
    'training_type': 'Bike', 'activity_id' : 3, 'is_hiit': False, 'avg_speed': 15, 'max_speed': 20, 'lowest_speed': 12, 'resistance_level': 0, 'rpe_overall': 'High'
    }]

    weight_training = [{
    'exercise_id':1, 'sets':3, 'repetitions_per_set':8, 'weight':60.6, 'rest_time': 30, 'rpe_exercise':'low', 'rpe_overall':'medium'
    },
    {'exercise_id':1, 'sets':3, 'repetitions_per_set':8, 'weight':60.6, 'rest_time': 30, 'rpe_exercise':'low', 'rpe_overall':'medium'
    },
    {'exercise_id':1, 'sets':3, 'repetitions_per_set':8, 'weight':60.6, 'rest_time': 30, 'rpe_exercise':'low', 'rpe_overall':'medium'
    }
    
    ]
    #register_aerobic_workout(user_id=1, training_type='Cardio', session_time='1:00:00', training_data=aerobic_training)
    #register_weight_workout(user_id=1, training_type='Weight', session_time='00:50:00', training_data= weight_training)
    #delete_aerobic_workout(workout_id=4)
    #delete_weight_workout(workout_id=7)
    #update_aerobic_workout(workout_id=8, training_data=aerobic_training)
    #update_weight_workout(workout_id=9, training_type='Peso bruto', training_data=weight_training)