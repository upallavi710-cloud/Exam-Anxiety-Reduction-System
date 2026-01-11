import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8080"

st.set_page_config(
    page_title="Exam Anxiety Reduction System",
    layout="centered"
)

st.title(" Exam Anxiety Reduction System")
st.caption("Focus on preparation, not pressure")

# -----------------------------
# DAILY CHECK-IN
# -----------------------------
st.header(" Daily Check-in")

subject = st.selectbox(
    "Select Subject",
    ["Physics", "Mathematics", "Chemistry", "Biology"]
)

study_hours = st.number_input(
    "Study hours today",
    min_value=0,
    max_value=12,
    value=2,
    step=1
)

sleep_hours = st.number_input(
    "Sleep hours last night",
    min_value=0,
    max_value=12,
    value=6,
    step=1
)

confidence_level = st.slider(
    "How confident do you feel today? (1 = low, 5 = high)",
    min_value=1,
    max_value=5,
    value=3
)

syllabus_chapter = st.text_input(
    "Current syllabus topic / chapter",
    "Chapter 3 – Current Electricity"
)

# -----------------------------
# GENERATE PLAN
# -----------------------------
if st.button("Generate Today's Plan"):
    payload = {
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "confidence_level": confidence_level,
        "syllabus_chapter": syllabus_chapter
    }

    response = requests.post(f"{API_BASE_URL}/progress/", json=payload)

    if response.status_code == 200:
        data = response.json()

        st.subheader(" Anxiety Status")
        st.write(f"**Level:** {data['anxiety']['anxiety_level']}")
        st.caption(data['anxiety']['explanation'])

        st.subheader(" Focus Area (Common Mistake)")
        st.warning(data["mistake_focus"])

        st.subheader(" Small, Realistic Goals for Today")
        for goal in data["goals"]:
            st.checkbox(goal)

        st.subheader(" Encouragement")
        st.success(data["message"])

    else:
        st.error("Backend server not responding")

# -----------------------------
# CONFIDENCE BAR CHART
# -----------------------------
st.header(" Confidence Trend")

scores_input = st.text_input(
    "Enter recent test scores (comma-separated)",
    "55, 60, 68, 72"
)

if st.button("Show Confidence Chart"):
    scores = [int(x.strip()) for x in scores_input.split(",") if x.strip().isdigit()]

    if scores:
        df = pd.DataFrame({
            "Attempt": range(1, len(scores) + 1),
            "Score": scores
        })

        st.bar_chart(df.set_index("Attempt"))
    else:
        st.warning("Please enter valid numeric scores")

# -----------------------------
# FOOTER
# -----------------------------
st.caption("Small steps every day reduce exam anxiety.")
