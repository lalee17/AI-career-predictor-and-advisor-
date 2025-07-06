import streamlit as st

st.set_page_config(page_title="AI Career Predictor", layout="centered")

st.title("🎓 AI Career Predictor and Advisor")

# --- Step 1: Input Form ---
with st.form("career_form"):
    name = st.text_input("What's your name?")
     age = st.text_input("How old are you?")
    educational level = st.multiselect(
        "Choose your educational level",
        ["Grade10","Grade11","A/L Student","University student","othe"]
         )
    
    skills = st.multiselect(
        "What skills do you have?",
        ["problem solving", "programming", "statistics", "design", "data analysis", "algorithms", "creativity", "communication"]
    )
    
    interests = st.multiselect(
        "What are your interests?",
        ["AI", "designing interfaces", "coding", "building apps", "debugging", "user experience", "predictive models", "art"]
    )
    
    submitted = st.form_submit_button("Get My Career Recommendation")

# --- Step 2: Career Data & Logic ---
career_data = [
    {
        "career": "Software Engineer",
        "skills": ["problem solving", "programming", "algorithms"],
        "interests": ["building apps", "coding", "debugging"]
    },
    {
        "career": "Data Scientist",
        "skills": ["statistics", "programming", "data analysis"],
        "interests": ["AI", "predictive models", "working with data"]
    },
    {
        "career": "UI/UX Designer",
        "skills": ["creativity", "design", "communication"],
        "interests": ["designing interfaces", "user experience", "art"]
    },
    {
        "career": "AI Engineer",
        "skills": ["programming", "statistics", "algorithms"],
        "interests": ["AI", "predictive models", "coding"]
    },
    {
        "career": "Frontend Developer",
        "skills": ["programming", "design", "creativity"],
        "interests": ["designing interfaces", "building apps", "user experience"]
    },
    {
        "career": "Backend Developer",
        "skills": ["problem solving", "programming", "algorithms"],
        "interests": ["debugging", "coding", "building apps"]
    },
    {
        "career": "Data Analyst",
        "skills": ["statistics", "data analysis", "communication"],
        "interests": ["working with data", "predictive models", "AI"]
    },
    {
        "career": "Product Manager",
        "skills": ["communication", "problem solving", "organization"],
        "interests": ["user experience", "building apps", "teamwork"]
    },
    {
        "career": "Graphic Designer",
        "skills": ["design", "creativity", "communication"],
        "interests": ["art", "user experience", "designing interfaces"]
    },
    {
        "career": "DevOps Engineer",
        "skills": ["problem solving", "programming", "automation"],
        "interests": ["building apps", "debugging", "efficiency"]
    }
]

def compute_fit_score(user_skills, user_interests, career):
    skill_matches = len(set(user_skills) & set(career["skills"]))
    interest_matches = len(set(user_interests) & set(career["interests"]))
    return skill_matches + interest_matches

def recommend_career(user_skills, user_interests, data):
    scores = []
    for career in data:
        score = compute_fit_score(user_skills, user_interests, career)
        scores.append((career["career"], score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0] if scores else ("No match found", 0)

# --- Step 3: Show Recommendation ---
if submitted:
    if not skills and not interests:
        st.warning("Please select at least one skill or interest.")
    else:
        career, score = recommend_career(skills, interests, career_data)
        st.success(f"🎯 **Hi {name}!** Based on your profile, you might enjoy being a **{career}**.")
        st.info(f"✅ Fit Score: {score}/6 (out of 3 skill + 3 interest matches)")

    st.write("Skills:", skills)
    st.write("Interests:", interests)
    st.write("Work Style:", work_style)


