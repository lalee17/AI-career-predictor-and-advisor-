import streamlit as st

# Sample career dataset
career_data = {
    "Software Engineer": {
        "skills": ["Logical thinking", "Problem solving", "Technology", "Coding"],
        "subjects": ["Mathematics", "ICT"],
        "work_style": "Alone"
    },
    "Digital Marketer": {
        "skills": ["Creativity", "Communication", "Empathy", "Public Speaking"],
        "subjects": ["Business Studies", "English"],
        "work_style": "Team"
    },
    "Graphic Designer": {
        "skills": ["Creativity", "Design", "Attention to detail"],
        "subjects": ["Art", "Media", "ICT"],
        "work_style": "Alone"
    },
    "Data Scientist": {
        "skills": ["Logical thinking", "Attention to detail", "Problem solving"],
        "subjects": ["Mathematics", "Science", "ICT"],
        "work_style": "Alone"
    },
    "Psychologist": {
        "skills": ["Empathy", "Communication", "Teamwork"],
        "subjects": ["Biology", "English", "Psychology"],
        "work_style": "Team"
    }
}

st.title("🎓 AI Career Predictor & Advisor")
st.markdown("This form collects your interests, skills, preferences and other details to recommend suitable career paths.")

with st.form("career_form"):
    name = st.text_input("1. Full Name")
    age = st.number_input("2. Age", min_value=10, max_value=100)
    grade = st.selectbox("3. Grade or Education Level", ["Grade 10", "Grade 11", "A/L Student", "University student", "Other"])

    fav_subjects = st.text_input("4. What are your favorite subjects in school?")
    weak_subjects = st.text_input("5. Which subjects do you dislike or struggle with?")
    hobbies = st.text_input("6. What are your hobbies or interests?")

    task_preference = st.multiselect(
        "7. What type of tasks do you enjoy most?",
        ["Solving problems", "Talking to people", "Designing or creating things", "Working with technology",
         "Writing or research", "Planning or organizing", "Leading others", "Other"]
    )

    st.markdown("8. Your MBTI personality type (find it here: [16personalities](https://www.16personalities.com/))")
    mbti = st.text_input("Enter your MBTI type")

    soft_skills = st.multiselect(
        "9. What soft skills describe you?",
        ["Leadership", "Communication", "Teamwork", "Creativity", "Attention to detail",
         "Logical thinking", "Empathy", "Public Speaking"]
    )
    other_soft_skills = st.text_input("Other soft skills (if any):")

    preferred_field = st.text_input("10. Do you have any preferred career field?")

    work_style = st.radio(
        "11. How do you prefer to work?",
        ["Alone", "In a team", "Both"]
    )

    tools = st.text_area("12. List any digital tools, platforms, or courses you've used or learned.")
    existing_ideas = st.text_area("13. Do you already have any career ideas in mind?")
    career_preferences = st.text_area("14. Fields or careers you'd like to work in:")

    submitted = st.form_submit_button("🔍 Get Career Suggestions")

    for career, data in career_data.items():
        # Match skills
        skill_match = any(skill.lower() in all_skills for skill in data["skills"])
        
        # Match subjects
        subject_match = any(sub.lower() in fav_subjects_list for sub in data["subjects"])
        
        # Match work style
        style_match = (data["work_style"].lower() in style) or (style == "both")

        # Show debug info (optional, remove later if you want)
        st.write(f"Checking {career}: skills={skill_match}, subjects={subject_match}, style={style_match}")

        # Count how many things matched
        score = 0
        if skill_match:
            score += 1
        if subject_match:
            score += 1
        if style_match:
            score += 1

        # Recommend if 2 or more things matched
        if score >= 2:
            matched_careers.append(career)


    for career, data in career_data.items():
        skill_match = any(skill.lower() in all_skills for skill in data["skills"])
        subject_match = any(sub.lower() in fav_subjects_list for sub in data["subjects"])
        style_match = (data["work_style"].lower() in style) or (style == "both")

        score = 0
if skill_match:
    score += 1
if subject_match:
    score += 1
if style_match:
    score += 1

if score >= 2:  # if 2 or more matches
    matched_careers.append(career)


    st.subheader("✅ Recommended Career Paths for You:")

    if matched_careers:
        for i, job in enumerate(matched_careers, 1):
            st.write(f"{i}. {job}")
    else:
        st.info("We couldn't find a strong match. Try adding more subjects and skills.")




