import streamlit as st

st.title("AI Career Predictor and Advisor")

# Section: User Info
st.header("Basic Info")
name = st.text_input("What's your name?")
age = st.number_input("Your age", min_value=10, max_value=100)

# Section: Skills and Interests
st.header("Your Skills & Interests")
skills = st.multiselect("What are your skills?", [
    "Programming", "Design", "Writing", "Public Speaking", "Data Analysis", "Creativity"
])
interests = st.multiselect("Your interests?", [
    "Technology", "Arts", "Business", "Science", "Education", "Health"
])
work_style = st.radio("Preferred work style", [
    "Teamwork", "Independent", "Flexible", "Structured"
])

# Submit Button
if st.button("Submit"):
    st.success(f"Thanks {name}! Your data has been recorded.")
    st.write("Age:", age)
    st.write("Skills:", skills)
    st.write("Interests:", interests)
    st.write("Work Style:", work_style)


