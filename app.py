import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

import json
import streamlit as st
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load career dataset
json_path = Path(__file__).parent / "careers.json"
with open(json_path, "r") as f:
    career_data = json.load(f)

# Convert your dict-style career_data to a list of dicts for easier processing
career_list = []
for title, details in career_data.items():
    career_list.append({
        "title": title,
        **details
    })

# Prepare corpus for similarity search (for RAG retrieval)
def create_corpus(careers):
    corpus = []
    for career in careers:
        text = career["title"] + " "
        text += career.get("description", "") + " "
        text += " ".join(career.get("skills", [])) + " "
        text += " ".join(career.get("subjects", []))
        corpus.append(text)
    return corpus

corpus = create_corpus(career_list)
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(corpus)

def retrieve_relevant_docs(query, top_k=3):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, X).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [career_list[i] for i in top_indices]

def generate_answer(question, relevant_docs):
    context_text = ""
    for doc in relevant_docs:
        context_text += f"Career Title: {doc['title']}\nDescription: {doc.get('description')}\n\n"
    prompt = (
        f"You are an expert career advisor. Use the following career information to answer the question:\n\n"
        f"{context_text}\n"
        f"Question: {question}\nAnswer:"
    )
    from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ],
    temperature=0.7,
    n=1,
)

answer = response.choices[0].message.content


    return response.choices[0].text.strip()
except Exception as e:
    return f"Sorry, I couldn't generate an answer due to an error: {str(e)}"

# Full career dataset with all careers you provided
career_data = {
  "Software Engineer": {
    "description": "Designs and develops software applications.",
    "skills": ["Programming", "Problem solving", "Logical thinking"],
    "subjects": ["Mathematics", "ICT"],
    "work_style": "Alone",
    "average_salary": "$80,000 - $120,000",
    "job_demand": "High",
    "recommended_tools": ["Python", "Git", "VS Code"],
    "learning_paths": ["CS degree", "freeCodeCamp", "LeetCode"]
  },
  "Data Scientist": {
    "description": "Analyzes complex data to help decision making.",
    "skills": ["Logical thinking", "Data analysis", "Statistics"],
    "subjects": ["Mathematics", "Science", "ICT"],
    "work_style": "Alone",
    "average_salary": "$90,000 - $130,000",
    "job_demand": "High",
    "recommended_tools": ["Python", "Pandas", "Jupyter Notebook"],
    "learning_paths": ["Coursera: Data Science", "Kaggle", "edX"]
  },
  "Digital Marketer": {
    "description": "Promotes products or services using digital channels.",
    "skills": ["Creativity", "SEO", "Social media"],
    "subjects": ["Business Studies", "English"],
    "work_style": "Team",
    "average_salary": "$50,000 - $90,000",
    "job_demand": "Medium",
    "recommended_tools": ["Google Ads", "Canva", "HubSpot"],
    "learning_paths": ["Google Digital Garage", "Udemy: Marketing"]
  },
  "Graphic Designer": {
    "description": "Creates visual content to communicate ideas.",
    "skills": ["Creativity", "Design", "Attention to detail"],
    "subjects": ["Art", "Media", "ICT"],
    "work_style": "Alone",
    "average_salary": "$45,000 - $75,000",
    "job_demand": "Medium",
    "recommended_tools": ["Adobe Photoshop", "Illustrator", "Figma"],
    "learning_paths": ["Coursera: Graphic Design", "Skillshare"]
  },
  "Psychologist": {
    "description": "Helps people improve mental health and wellbeing.",
    "skills": ["Empathy", "Listening", "Analysis"],
    "subjects": ["Biology", "English", "Psychology"],
    "work_style": "Team",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "High",
    "recommended_tools": ["DSM-5", "SPSS"],
    "learning_paths": ["BA Psychology", "Clinical Psychology Masters"]
  },
  "Teacher": {
    "description": "Educates students at various levels.",
    "skills": ["Communication", "Patience", "Leadership"],
    "subjects": ["Any depending on subject"],
    "work_style": "Team",
    "average_salary": "$40,000 - $70,000",
    "job_demand": "High",
    "recommended_tools": ["Google Classroom", "Kahoot"],
    "learning_paths": ["Teaching degree", "Diploma in Education"]
  },
  "Mechanical Engineer": {
    "description": "Designs and builds mechanical systems.",
    "skills": ["Problem solving", "Math", "Design"],
    "subjects": ["Mathematics", "Physics"],
    "work_style": "Alone",
    "average_salary": "$70,000 - $110,000",
    "job_demand": "Medium",
    "recommended_tools": ["AutoCAD", "SolidWorks"],
    "learning_paths": ["Mechanical Eng. Degree", "Coursera"]
  },
  "Nurse": {
    "description": "Provides healthcare and support to patients.",
    "skills": ["Empathy", "Attention to detail", "Teamwork"],
    "subjects": ["Biology", "Health Science"],
    "work_style": "Team",
    "average_salary": "$60,000 - $90,000",
    "job_demand": "Very High",
    "recommended_tools": ["Electronic Health Records", "Stethoscope"],
    "learning_paths": ["Nursing diploma", "BSN", "CPR training"]
  },
  "Journalist": {
    "description": "Gathers and reports news stories.",
    "skills": ["Communication", "Research", "Writing"],
    "subjects": ["English", "Media Studies"],
    "work_style": "Alone",
    "average_salary": "$45,000 - $80,000",
    "job_demand": "Medium",
    "recommended_tools": ["Notion", "AP Stylebook"],
    "learning_paths": ["Journalism degree", "Blogging"]
  },
  "Chef": {
    "description": "Prepares meals in restaurants or other venues.",
    "skills": ["Creativity", "Attention to detail", "Time management"],
    "subjects": ["Home Economics"],
    "work_style": "Team",
    "average_salary": "$30,000 - $60,000",
    "job_demand": "High",
    "recommended_tools": ["Knives", "Kitchen equipment"],
    "learning_paths": ["Culinary school", "YouTube: Cooking"]
  },
  "Civil Engineer": {
    "description": "Designs and supervises construction projects.",
    "skills": ["Problem solving", "Math", "Project management"],
    "subjects": ["Mathematics", "Physics"],
    "work_style": "Team",
    "average_salary": "$70,000 - $100,000",
    "job_demand": "High",
    "recommended_tools": ["AutoCAD", "Revit", "MS Project"],
    "learning_paths": ["Civil Eng. Degree", "Coursera: Structural Eng."]
  },
  "Accountant": {
    "description": "Manages financial records and reports.",
    "skills": ["Attention to detail", "Math", "Organization"],
    "subjects": ["Mathematics", "Business Studies"],
    "work_style": "Alone",
    "average_salary": "$60,000 - $95,000",
    "job_demand": "High",
    "recommended_tools": ["Excel", "QuickBooks", "Xero"],
    "learning_paths": ["Accounting degree", "ACCA", "CPA"]
  },
  "Pharmacist": {
    "description": "Dispenses medications and advises patients.",
    "skills": ["Attention to detail", "Science", "Communication"],
    "subjects": ["Biology", "Chemistry"],
    "work_style": "Alone",
    "average_salary": "$80,000 - $120,000",
    "job_demand": "High",
    "recommended_tools": ["Pharmacy systems", "RxNorm"],
    "learning_paths": ["Pharmacy degree", "Clinical training"]
  },
  "Architect": {
    "description": "Designs buildings and structures.",
    "skills": ["Design", "Creativity", "Problem solving"],
    "subjects": ["Art", "Mathematics", "Physics"],
    "work_style": "Team",
    "average_salary": "$70,000 - $110,000",
    "job_demand": "Medium",
    "recommended_tools": ["AutoCAD", "SketchUp", "Rhino"],
    "learning_paths": ["Architecture degree", "Internship"]
  },
  "Lawyer": {
    "description": "Provides legal advice and representation.",
    "skills": ["Communication", "Research", "Critical thinking"],
    "subjects": ["English", "History"],
    "work_style": "Alone",
    "average_salary": "$90,000 - $150,000",
    "job_demand": "High",
    "recommended_tools": ["Legal databases", "Case management software"],
    "learning_paths": ["Law degree", "Bar exam", "Moot court"]
  },
  "Electrician": {
    "description": "Installs and maintains electrical systems.",
    "skills": ["Problem solving", "Technical skills", "Attention to detail"],
    "subjects": ["Physics", "Technical Drawing"],
    "work_style": "Alone",
    "average_salary": "$50,000 - $80,000",
    "job_demand": "High",
    "recommended_tools": ["Multimeter", "Circuit testers"],
    "learning_paths": ["Apprenticeship", "Technical college"]
  },
  "Social Worker": {
    "description": "Supports individuals and communities in need.",
    "skills": ["Empathy", "Communication", "Problem solving"],
    "subjects": ["Psychology", "Sociology"],
    "work_style": "Team",
    "average_salary": "$45,000 - $75,000",
    "job_demand": "High",
    "recommended_tools": ["Case management software"],
    "learning_paths": ["Social Work degree", "Volunteer experience"]
  },
  "Pilot": {
    "description": "Operates aircraft safely.",
    "skills": ["Attention to detail", "Technical skills", "Calm under pressure"],
    "subjects": ["Physics", "Mathematics"],
    "work_style": "Alone",
    "average_salary": "$100,000 - $180,000",
    "job_demand": "Medium",
    "recommended_tools": ["Flight simulators", "Navigation systems"],
    "learning_paths": ["Pilot school", "Flight hours", "FAA license"]
  },
  "Veterinarian": {
    "description": "Provides medical care to animals.",
    "skills": ["Science", "Empathy", "Attention to detail"],
    "subjects": ["Biology", "Chemistry"],
    "work_style": "Alone",
    "average_salary": "$80,000 - $120,000",
    "job_demand": "High",
    "recommended_tools": ["Veterinary software", "X-ray machine"],
    "learning_paths": ["Veterinary degree", "Internship"]
  },
  "Entrepreneur": {
    "description": "Starts and manages new businesses.",
    "skills": ["Leadership", "Risk-taking", "Creativity"],
    "subjects": ["Business Studies", "Economics"],
    "work_style": "Both",
    "average_salary": "Varies widely",
    "job_demand": "High (self-driven)",
    "recommended_tools": ["Notion", "Canva", "Shopify"],
    "learning_paths": ["Startup incubator", "Entrepreneurship courses"]
  },
  "Translator": {
    "description": "Converts written or spoken language.",
    "skills": ["Language skills", "Attention to detail", "Communication"],
    "subjects": ["Languages", "English"],
    "work_style": "Alone",
    "average_salary": "$40,000 - $80,000",
    "job_demand": "Medium",
    "recommended_tools": ["CAT Tools", "Google Translate", "DeepL"],
    "learning_paths": ["Language degree", "Translation certificate"]
  },
  "Event Planner": {
    "description": "Organizes events and meetings.",
    "skills": ["Organization", "Communication", "Creativity"],
    "subjects": ["Business Studies", "English"],
    "work_style": "Team",
    "average_salary": "$45,000 - $75,000",
    "job_demand": "Medium",
    "recommended_tools": ["Trello", "Eventbrite", "Google Calendar"],
    "learning_paths": ["Event Planning courses", "Internships"]
  },
  "Fashion Designer": {
    "description": "Creates clothing and accessories.",
    "skills": ["Creativity", "Design", "Attention to detail"],
    "subjects": ["Art", "Textiles"],
    "work_style": "Alone",
    "average_salary": "$50,000 - $90,000",
    "job_demand": "Medium",
    "recommended_tools": ["Sketchpad", "Adobe Illustrator"],
    "learning_paths": ["Fashion Design degree", "Portfolio building"]
  },
  "Environmental Scientist": {
    "description": "Studies environmental problems and solutions.",
    "skills": ["Research", "Science", "Problem solving"],
    "subjects": ["Biology", "Chemistry", "Geography"],
    "work_style": "Both",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "High",
    "recommended_tools": ["GIS software", "Excel"],
    "learning_paths": ["Environmental Science degree", "Field work"]
  },
  "Animator": {
    "description": "Creates animations for media.",
    "skills": ["Creativity", "Design", "Technical skills"],
    "subjects": ["Art", "ICT"],
    "work_style": "Alone",
    "average_salary": "$50,000 - $85,000",
    "job_demand": "Medium",
    "recommended_tools": ["Blender", "Maya", "Toon Boom"],
    "learning_paths": ["Animation course", "Practice with projects"]
  },
  "Police Officer": {
    "description": "Enforces laws and protects the public.",
    "skills": ["Physical fitness", "Communication", "Problem solving"],
    "subjects": ["Physical Education", "Social Studies"],
    "work_style": "Team",
    "average_salary": "$50,000 - $80,000",
    "job_demand": "High",
    "recommended_tools": ["Radio", "Body cam"],
    "learning_paths": ["Police academy", "Law & Criminology course"]
  },
  "Photographer": {
    "description": "Takes professional photographs.",
    "skills": ["Creativity", "Technical skills", "Attention to detail"],
    "subjects": ["Art", "Media Studies"],
    "work_style": "Alone",
    "average_salary": "$40,000 - $70,000",
    "job_demand": "Medium",
    "recommended_tools": ["DSLR", "Lightroom", "Photoshop"],
    "learning_paths": ["Photography course", "YouTube tutorials"]
  },
  "Fitness Trainer": {
    "description": "Helps clients improve fitness and health.",
    "skills": ["Physical fitness", "Motivation", "Communication"],
    "subjects": ["Physical Education", "Biology"],
    "work_style": "Team",
    "average_salary": "$40,000 - $70,000",
    "job_demand": "High",
    "recommended_tools": ["Resistance bands", "Workout app"],
    "learning_paths": ["Personal training certificate", "CPR"]
  },
  "Biomedical Engineer": {
    "description": "Designs medical devices and equipment.",
    "skills": ["Engineering", "Biology", "Problem solving"],
    "subjects": ["Biology", "Mathematics", "Physics"],
    "work_style": "Alone",
    "average_salary": "$70,000 - $110,000",
    "job_demand": "Medium",
    "recommended_tools": ["CAD software", "MATLAB"],
    "learning_paths": ["Biomedical Engineering degree", "Internship"]
  },
  "Economist": {
    "description": "Studies economic trends and provides forecasts.",
    "skills": ["Analytical thinking", "Mathematics", "Research"],
    "subjects": ["Mathematics", "Economics"],
    "work_style": "Alone",
    "average_salary": "$70,000 - $120,000",
    "job_demand": "Medium",
    "recommended_tools": ["Excel", "Statistical software"],
    "learning_paths": ["Economics degree", "Masters in Economics"]
  },
  "Web Developer": {
    "description": "Builds and maintains websites and web applications.",
    "skills": ["Programming", "Design", "Problem solving"],
    "subjects": ["ICT", "Mathematics"],
    "work_style": "Alone",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "High",
    "recommended_tools": ["HTML", "CSS", "JavaScript"],
    "learning_paths": ["Bootcamps", "CS degree", "Online courses"]
  },
  "Content Writer": {
    "description": "Creates written content for websites, blogs, and marketing.",
    "skills": ["Writing", "Creativity", "Research"],
    "subjects": ["English", "Media Studies"],
    "work_style": "Alone",
    "average_salary": "$35,000 - $65,000",
    "job_demand": "Medium",
    "recommended_tools": ["Google Docs", "Grammarly"],
    "learning_paths": ["English degree", "Content marketing courses"]
  },
  "UX Designer": {
    "description": "Designs user-friendly interfaces for products and apps.",
    "skills": ["Creativity", "User research", "Design"],
    "subjects": ["ICT", "Art"],
    "work_style": "Team",
    "average_salary": "$70,000 - $110,000",
    "job_demand": "High",
    "recommended_tools": ["Figma", "Sketch", "Adobe XD"],
    "learning_paths": ["UX courses", "Design degree"]
  },
  "Civil Architect": {
    "description": "Designs buildings and infrastructure projects.",
    "skills": ["Design", "Project management", "Creativity"],
    "subjects": ["Art", "Mathematics", "Physics"],
    "work_style": "Team",
    "average_salary": "$65,000 - $110,000",
    "job_demand": "Medium",
    "recommended_tools": ["AutoCAD", "Revit", "SketchUp"],
    "learning_paths": ["Architecture degree", "Internships"]
  },
  "Environmental Engineer": {
    "description": "Develops solutions to environmental problems.",
    "skills": ["Science", "Problem solving", "Research"],
    "subjects": ["Biology", "Chemistry", "Mathematics"],
    "work_style": "Team",
    "average_salary": "$65,000 - $105,000",
    "job_demand": "Medium",
    "recommended_tools": ["GIS software", "AutoCAD"],
    "learning_paths": ["Environmental Engineering degree", "Internship"]
  },
  "Real Estate Agent": {
    "description": "Helps clients buy, sell, and rent properties.",
    "skills": ["Communication", "Negotiation", "Customer service"],
    "subjects": ["Business Studies", "Economics"],
    "work_style": "Team",
    "average_salary": "$40,000 - $90,000",
    "job_demand": "Medium",
    "recommended_tools": ["CRM software", "MLS databases"],
    "learning_paths": ["Real estate courses", "Licensing"]
  },
  "Mechanical Technician": {
    "description": "Maintains and repairs mechanical equipment.",
    "skills": ["Technical skills", "Problem solving", "Manual dexterity"],
    "subjects": ["Technical Drawing", "Physics"],
    "work_style": "Alone",
    "average_salary": "$40,000 - $70,000",
    "job_demand": "Medium",
    "recommended_tools": ["Toolkits", "Diagnostic software"],
    "learning_paths": ["Technical diploma", "Apprenticeship"]
  },
  "Audiologist": {
    "description": "Diagnoses and treats hearing problems.",
    "skills": ["Science", "Communication", "Attention to detail"],
    "subjects": ["Biology", "Health Science"],
    "work_style": "Alone",
    "average_salary": "$70,000 - $110,000",
    "job_demand": "Medium",
    "recommended_tools": ["Audiometers", "Soundproof booths"],
    "learning_paths": ["Audiology degree", "Clinical training"]
  },
  "Chemist": {
    "description": "Researches chemicals and their properties.",
    "skills": ["Science", "Research", "Attention to detail"],
    "subjects": ["Chemistry", "Mathematics"],
    "work_style": "Alone",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "Medium",
    "recommended_tools": ["Lab equipment", "Analytical software"],
    "learning_paths": ["Chemistry degree", "Research assistantship"]
  },
  "Dentist": {
    "description": "Provides dental care and oral health services.",
    "skills": ["Science", "Manual dexterity", "Communication"],
    "subjects": ["Biology", "Chemistry"],
    "work_style": "Alone",
    "average_salary": "$120,000 - $180,000",
    "job_demand": "High",
    "recommended_tools": ["Dental equipment", "X-ray machines"],
    "learning_paths": ["Dentistry degree", "Internship"]
  },
  "Film Director": {
    "description": "Directs film productions from start to finish.",
    "skills": ["Creativity", "Leadership", "Storytelling"],
    "subjects": ["Art", "Media Studies"],
    "work_style": "Team",
    "average_salary": "$50,000 - $150,000",
    "job_demand": "Medium",
    "recommended_tools": ["Editing software", "Camera equipment"],
    "learning_paths": ["Film school", "Internships"]
  },
  "Geologist": {
    "description": "Studies Earth's physical structure and processes.",
    "skills": ["Science", "Fieldwork", "Research"],
    "subjects": ["Geography", "Physics", "Chemistry"],
    "work_style": "Both",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "Medium",
    "recommended_tools": ["GIS software", "Field tools"],
    "learning_paths": ["Geology degree", "Field internships"]
  },
  "HR Manager": {
    "description": "Manages recruitment, training, and employee relations.",
    "skills": ["Communication", "Organization", "Leadership"],
    "subjects": ["Business Studies", "Psychology"],
    "work_style": "Team",
    "average_salary": "$60,000 - $110,000",
    "job_demand": "High",
    "recommended_tools": ["HR software", "Payroll systems"],
    "learning_paths": ["Business degree", "HR certifications"]
  },
  "Interior Designer": {
    "description": "Designs interior spaces for aesthetics and function.",
    "skills": ["Creativity", "Design", "Communication"],
    "subjects": ["Art", "Design"],
    "work_style": "Team",
    "average_salary": "$50,000 - $85,000",
    "job_demand": "Medium",
    "recommended_tools": ["AutoCAD", "SketchUp"],
    "learning_paths": ["Interior design degree", "Portfolio"]
  },
  "IT Support Specialist": {
    "description": "Provides technical support and troubleshooting.",
    "skills": ["Problem solving", "Technical skills", "Communication"],
    "subjects": ["ICT"],
    "work_style": "Team",
    "average_salary": "$40,000 - $70,000",
    "job_demand": "High",
    "recommended_tools": ["Helpdesk software", "Remote tools"],
    "learning_paths": ["IT certifications", "Diploma in IT"]
  },
  "Journalist": {
    "description": "Gathers and reports news stories.",
    "skills": ["Communication", "Research", "Writing"],
    "subjects": ["English", "Media Studies"],
    "work_style": "Alone",
    "average_salary": "$45,000 - $80,000",
    "job_demand": "Medium",
    "recommended_tools": ["Notion", "AP Stylebook"],
    "learning_paths": ["Journalism degree", "Blogging"]
  },
  "Logistics Manager": {
    "description": "Coordinates supply chain and logistics operations.",
    "skills": ["Organization", "Planning", "Problem solving"],
    "subjects": ["Business Studies", "Mathematics"],
    "work_style": "Team",
    "average_salary": "$60,000 - $100,000",
    "job_demand": "High",
    "recommended_tools": ["ERP software", "Excel"],
    "learning_paths": ["Business degree", "Logistics courses"]
  }
}

# Streamlit UI with two pages: Questionnaire and Chatbot
st.set_page_config(page_title="🎓 AI Career Predictor & Advisor", layout="wide")
st.title("🎓 AI Career Predictor & Advisor")

menu = ["Career Questionnaire", "Career Chatbot"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Career Questionnaire":
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
    career_fit_details = {}

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
        explanation = []
        if skill_match:
            score += 1
            explanation.append("Skills matched")
        if subject_match:
            score += 1
            explanation.append("Subjects matched")
        if style_match:
            score += 1
            explanation.append("Work style matched")

        if score >= 2:
            matched_careers.append(career)
            career_fit_details[career] = {
                "score": score,
                "explanation": ", ".join(explanation)
            }

    if matched_careers:
        for i, job in enumerate(matched_careers, 1):
            fit = career_fit_details[job]["score"]
            expl = career_fit_details[job]["explanation"]
            st.write(f"{i}. {job} — {career_data[job]['description']}")
            st.write(f"   💡 Fit Score: {fit}/3 ({expl})")
            st.write(f"   💰 Typical Salary: {career_data[job]['average_salary']}")
            st.write(f"   📈 Job Market Demand: {career_data[job]['job_demand']}")
            st.write(f"   🛠️ Recommended Tools: {', '.join(career_data[job]['recommended_tools'])}")
            st.write(f"   🎓 Suggested Learning Paths: {', '.join(career_data[job]['learning_paths'])}")
            st.markdown("---")
    else:
        st.info("We couldn't find a strong match. Try adding more subjects and skills.")


        # 🔍 Optional: Mental Well-being Check
st.subheader("🧠 Mental Well-being Check")

st.markdown("On a scale from 1 to 5, how do you feel about the recommended careers?")

well_being_score = st.slider("How confident or happy do you feel about pursuing the above careers?", 1, 5)

if well_being_score <= 2:
    st.warning("It looks like you're not feeling great about the options. It's okay! Explore more or talk to a career counselor. 💬")
elif well_being_score == 3:
    st.info("You're unsure — maybe try learning more about each career before deciding.")
else:
    st.success("Great! You're feeling positive. Keep exploring and preparing for your journey! 🚀")
if well_being_score <= 2:
    st.warning("It looks like you're not feeling great about the options. You can ask a question below 👇")

    concern = st.text_input("🗣️ What's bothering you about the careers suggested?")
    if concern:
        st.success("Thank you for sharing. We'll use this to improve future suggestions. ❤️")

elif choice == "Career Chatbot":
    st.header("💬 Career Advisor Chatbot")
    st.info("Ask me anything about careers! I will answer based on your career data and general knowledge.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="chat_input")

    if user_input:
        relevant_docs = retrieve_relevant_docs(user_input, top_k=3)
        answer = generate_answer(user_input, relevant_docs)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", answer))

    for i in range(0, len(st.session_state.chat_history), 2):
        user_msg = st.session_state.chat_history[i][1]
        bot_msg = st.session_state.chat_history[i + 1][1]
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**Bot:** {bot_msg}")














