import streamlit as st
import pandas as pd
import joblib

model = joblib.load('student_score_prediction.pkl')

# Streamlit app UI
st.title("Student marks finder based on their behaviour")

st.markdown("### Enter you behviour details")

age=st. number_input("enter you age:")
gender=st.text_input("enter you gender (male/female/other):")
studyhours= st.number_input("Study time per day (hours): ")
socialmedia_hours = st.number_input("Social media time per day (hours): ")
OTT_hours = st.number_input("enter ott platform usage (hours):") 
part_time_job  = st.text_input("part time job working (Yes/No): ")
attendance_percentage = st.number_input("enter you attendance percentage: ")
sleep_hours = st.number_input("enter your sleep hour per day: ")
diet_quality = st.text_input("enter your diet quality (fair/good/poor): ")
exercise_frequency=st.number_input("enter no of exercise days in a week:")
parental_education_level=st.text_input("how is your parent education(Master/Bachelor/high school/nan):")
internet_quality=st.text_input("how was you internet quality (average/poor/good):")
mental_health_rating=st.number_input("enter how you will rate your mental health from 0 to 10:")
extracurricular_participation=st.text_input("are in any extra curicular participation(yes/no):")


# Predict button
if st.button("Predict score"):
    # Prepare input as DataFrame
    input_data = pd.DataFrame({
       'age': [age],
    'gender': [gender], 
    'study_hours_per_day': [studyhours],
    'social_media_hours': [socialmedia_hours],
    'netflix_hours': [OTT_hours],
    'part_time_job':[part_time_job],
    'attendance_percentage': [attendance_percentage],
    'sleep_hours': [sleep_hours],
    'exercise_frequency': [exercise_frequency],
    'diet_quality': [diet_quality],
    'parental_education_level': [parental_education_level],
    'internet_quality': [internet_quality],
    'mental_health_rating': [mental_health_rating],
    'extracurricular_participation': [extracurricular_participation]
    })

    # Make prediction
    predicted_score = model.predict(input_data)[0]
    st.success(f" Expected score to be: {predicted_score:,.2f}")
