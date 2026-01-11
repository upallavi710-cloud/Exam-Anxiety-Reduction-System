Exam Anxiety Reduction System

This project is a Python-based AI system that helps students reduce exam anxiety by giving small daily study goals, tracking confidence, and encouraging healthy study and sleep habits.

Instead of pressuring students with marks and ranks, the system focuses on consistency, confidence, and mental well-being.

Problem Addressed

Many students feel anxious during exam preparation because:

They study for long hours without clear goals

They don’t know if they are improving

Poor sleep increases stress

One bad day reduces confidence

This system helps students feel prepared, not pressured.

Project Features
1. Daily Student Input

The student manually enters:

Subject

Syllabus / Chapter name

Study hours

Sleep hours

Confidence level (1 = low, 5 = high)

Recent test marks

2. Smart Daily Micro-Goals

The system generates 2–4 small goals such as:

“Revise formulas of Chapter 3 (20 minutes)”

“Attempt 5 medium questions without time pressure”

“Review today’s mistakes (15 minutes)”

Goals are:

Time-boxed

Easy to complete

Low mental pressure

3. Anxiety & Confidence Analysis

The system analyzes:

Study vs sleep balance

Self-reported confidence

Recent performance

It shows:

Anxiety level (Low / Moderate / High)

Short explanation of why

One positive encouragement message

4. Confidence Trend Visualization

Displays a bar chart using test marks

Helps students see improvement visually

No ranking or comparison with others

Technology Used
Layer	       Technology
Frontend	    Streamlit
Backend	        FastAPI
Data Processing	Pandas, NumPy
Logic	        Rule-based + simple ML
Database	    SQLite
Server	        Uvicorn

Folder Structure
exam-anxiety-ai/
│── backend/
│   ├── api/
│   ├── services/
│   ├── ml/
│   ├── models/
│   └── main.py
│
│── frontend/
│   └── streamlit_app.py
│
│── data/
│── database/
│── docs/
│── tests/
│── notebooks/
│── requirements.txt
│── README.md

How to Run the Project
Step 1: Activate Virtual Environment
venv\Scripts\activate
Step 2: Install Required Packages
pip install -r requirements.txt
Step 3: Start Backend
python -m uvicorn backend.main:app --reload --port 8080
Backend runs at:
http://127.0.0.1:8080
Step 4: Start Frontend
streamlit run frontend/streamlit_app.py


Example Output

Anxiety Level: Moderate

Explanation: Less sleep with moderate study hours

Encouragement:
“Consistency matters more than speed. You are doing well.”

Daily Goals:
Revise formulas (20 mins)
Practice 5 questions
Review mistakes (15 mins)

Future Improvements

Login system
Daily history tracking
Parent support view
Multilingual encouragement
Notification reminders
Developer

Pallavi Ravindra Upadhye
 Project – Exam Anxiety Reduction System
