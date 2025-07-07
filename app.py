import streamlit as st

# Full career dataset with all careers you provided
career_data = {
    "Software Engineer": {
        "skills": ["Programming", "Problem solving", "Logical thinking"],
        "subjects": ["Mathematics", "ICT"],
        "work_style": "Alone",
        "description": "Designs and develops software applications."
    },
    "Digital Marketer": {
        "skills": ["Creativity", "Communication", "Public Speaking"],
        "subjects": ["Business Studies", "English"],
        "work_style": "Team",
        "description": "Promotes products or services using digital channels."
    },
    "Graphic Designer": {
        "skills": ["Creativity", "Design", "Attention to detail"],
        "subjects": ["Art", "Media", "ICT"],
        "work_style": "Alone",
        "description": "Creates visual content to communicate ideas."
    },
    "Data Scientist": {
        "skills": ["Logical thinking", "Attention to detail", "Problem solving"],
        "subjects": ["Mathematics", "Science", "ICT"],
        "work_style": "Alone",
        "description": "Analyzes complex data to help decision making."
    },
    "Psychologist": {
        "skills": ["Empathy", "Communication", "Teamwork"],
        "subjects": ["Biology", "English", "Psychology"],
        "work_style": "Team",
        "description": "Helps people improve mental health and wellbeing."
    },
    "Teacher": {
        "skills": ["Communication", "Patience", "Leadership"],
        "subjects": ["Varies by subject"],
        "work_style": "Team",
        "description": "Educates students at various levels."
    },
    "Mechanical Engineer": {
        "skills": ["Problem solving", "Math", "Design"],
        "subjects": ["Mathematics", "Physics"],
        "work_style": "Alone",
        "description": "Designs and builds mechanical systems."
    },
    "Nurse": {
        "skills": ["Empathy", "Attention to detail", "Teamwork"],
        "subjects": ["Biology", "Health Science"],
        "work_style": "Team",
        "description": "Provides healthcare and support to patients."
    },
    "Journalist": {
        "skills": ["Communication", "Research", "Writing"],
        "subjects": ["English", "Media Studies"],
        "work_style": "Alone",
        "description": "Gathers and reports news stories."
    },
    "Chef": {
        "skills": ["Creativity", "Attention to detail", "Time management"],
        "subjects": ["Home Economics"],
        "work_style": "Team",
        "description": "Prepares meals in restaurants or other venues."
    },
    "Civil Engineer": {
        "skills": ["Problem solving", "Math", "Project management"],
        "subjects": ["Mathematics", "Physics"],
        "work_style": "Team",
        "description": "Designs and supervises construction projects."
    },
    "Accountant": {
        "skills": ["Attention to detail", "Math", "Organization"],
        "subjects": ["Mathematics", "Business Studies"],
        "work_style": "Alone",
        "description": "Manages financial records and reports."
    },
    "Pharmacist": {
        "skills": ["Attention to detail", "Science", "Communication"],
        "subjects": ["Biology", "Chemistry"],
        "work_style": "Alone",
        "description": "Dispenses medications and advises patients."
    },
    "Architect": {
        "skills": ["Design", "Creativity", "Problem solving"],
        "subjects": ["Art", "Mathematics", "Physics"],
        "work_style": "Team",
        "description": "Designs buildings and structures."
    },
    "Lawyer": {
        "skills": ["Communication", "Research", "Critical thinking"],
        "subjects": ["English", "History"],
        "work_style": "Alone",
        "description": "Provides legal advice and representation."
    },
    "Electrician": {
        "skills": ["Problem solving", "Technical skills", "Attention to detail"],
        "subjects": ["Physics", "Technical Drawing"],
        "work_style": "Alone",
        "description": "Installs and maintains electrical systems."
    },
    "Social Worker": {
        "skills": ["Empathy", "Communication", "Problem solving"],
        "subjects": ["Psychology", "Sociology"],
        "work_style": "Team",
        "description": "Supports individuals and communities in need."
    },
    "Pilot": {
        "skills": ["Attention to detail", "Technical skills", "Calm under pressure"],
        "subjects": ["Physics", "Mathematics"],
        "work_style": "Alone",
        "description": "Operates aircraft safely."
    },
    "Veterinarian": {
        "skills": ["Science", "Empathy", "Attention to detail"],
        "subjects": ["Biology", "Chemistry"],
        "work_style": "Alone",
        "description": "Provides medical care to animals."
    },
    "Entrepreneur": {
        "skills": ["Leadership", "Risk-taking", "Creativity"],
        "subjects": ["Business Studies", "Economics"],
        "work_style": "Both",
        "description": "Starts and manages new businesses."
    },
    "Translator": {
        "skills": ["Language skills", "Attention to detail", "Communication"],
        "subjects": ["Languages", "English"],
        "work_style": "Alone",
        "description": "Converts written or spoken language."
    },
    "Event Planner": {
        "skills": ["Organization", "Communication", "Creativity"],
        "subjects": ["Business Studies", "English"],
        "work_style": "Team",
        "description": "Organizes events and meetings."
    },
    "Fashion Designer": {
        "skills": ["Creativity", "Design", "Attention to detail"],
        "subjects": ["Art", "Textiles"],
        "work_style": "Alone",
        "description": "Creates clothing and accessories."
    },
    "Environmental Scientist": {
        "skills": ["Research", "Science", "Problem solving"],
        "subjects": ["Biology", "Chemistry", "Geography"],
        "work_style": "Both",
        "description": "Studies environmental problems and solutions."
    },
    "Animator": {
        "skills": ["Creativity", "Design", "Technical skills"],
        "subjects": ["Art", "ICT"],
        "work_style": "Alone",
        "description": "Creates animations for media."
    },
    "Police Officer": {
        "skills": ["Physical fitness", "Communication", "Problem solving"],
        "subjects": ["Physical Education", "Social Studies"],
        "work_style": "Team",
        "description": "Enforces laws and protects the public."
    },
    "Scientist": {
        "skills": ["Research", "Analytical thinking", "Attention to detail"],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "work_style": "Alone",
        "description": "Conducts scientific experiments and research."
    },
    "Photographer": {
        "skills": ["Creativity", "Technical skills", "Attention to detail"],
        "subjects": ["Art", "Media Studies"],
        "work_style": "Alone",
        "description": "Takes professional photographs."
    },
    "Fitness Trainer": {
        "skills": ["Physical fitness", "Motivation", "Communication"],
        "subjects": ["Physical Education", "Biology"],
        "work_style": "Team",
        "description": "Helps clients improve fitness and health."
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

    

    soft_skills = st.multiselect(
        "9. What soft skills describe you?",
        ["Leadership", "Communication", "Teamwork", "Creativity", "Attention to detail",
         "Logical thinking", "Empathy", "Public Speaking"]
    )
    other_soft_skills = st.text_input("Other soft skills (if any):")

    

    work_style = st.radio(
        "11. How do you prefer to work?",
        ["Alone", "In a team", "Both"]
    )

    tools = st.text_area("12. List any digital tools, platforms, or courses you've used or learned.")
    existing_ideas = st.text_area("13. Do you already have any career ideas in mind?")
    career_preferences = st.text_area("14. Fields or careers you'd like to work in:")

    submitted = st.form_submit_button("🔍 Get Career Suggestions")

if submitted:
    matched_careers = []

    # Clean inputs for better matching
    all_skills = [s.strip().lower() for s in soft_skills]
    if other_soft_skills:
        all_skills.extend([s.strip().lower() for s in other_soft_skills.split(",")])

    fav_subjects_list = [s.strip().lower() for s in fav_subjects.split(",")]
    style = work_style.lower()

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

        if score >= 2:
            matched_careers.append(career)

    st.subheader("✅ Recommended Career Paths for You:")

    if matched_careers:
        for i, job in enumerate(matched_careers, 1):
            st.write(f"{i}. {job} — {career_data[job]['description']}"))
 
    else:
        st.info("We couldn't find a strong match. Try adding more subjects and skills.")

st.header("🗣️ Career Advice Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def find_career_answer(user_msg):
    user_msg_lower = user_msg.lower()
    # Try to find any career keyword in user message
    for career, data in career_data.items():
        if career.lower() in user_msg_lower:
            return f"**{career}**: {data['description']}\nSkills needed: {', '.join(data['skills'])}\nSubjects relevant: {', '.join(data['subjects'])}"
        # Also check if any skill or subject is mentioned
        for skill in data['skills']:
            if skill.lower() in user_msg_lower:
                return f"Career related to skill '{skill}': {career}\nDescription: {data['description']}"
        for subject in data['subjects']:
            if subject.lower() in user_msg_lower:
                return f"Career related to subject '{subject}': {career}\nDescription: {data['description']}"
    return "Sorry, I couldn't find any career information related to your question."

user_input = st.chat_input("Ask me about careers, skills, or subjects")

if user_input:
    # Append user question
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get chatbot reply
    reply = find_career_answer(user_input)

    # Append bot reply
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])






