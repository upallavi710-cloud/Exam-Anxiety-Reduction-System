from backend.data_processing.loader import load_mock_performance

def generate_micro_goals(anxiety_level: str, subject: str, syllabus_topic: str):
    df = load_mock_performance()

    common_mistake = df.iloc[-1]["mistake"]

    goals = []

    if anxiety_level == "High":
        goals = [
            f"Revise formulas of {syllabus_topic} – 20 mins",
            f"Attempt 5 easy questions avoiding '{common_mistake}'",
            "Read solved examples only – 15 mins"
        ]

    elif anxiety_level == "Medium":
        goals = [
            f"Revise key concepts of {syllabus_topic} – 25 mins",
            f"Attempt 5 medium questions carefully",
            f"Review '{common_mistake}' mistakes – 10 mins"
        ]

    else:
        goals = [
            f"Attempt 10 mixed questions from {syllabus_topic} – 30 mins",
            "Analyze mistakes calmly – 15 mins"
        ]

    return {
        "topic": syllabus_topic,
        "common_mistake": common_mistake,
        "goals": goals[:3],
        "design_principles": [
            "time-boxed",
            "low cognitive load",
            "single sitting"
        ]
    }
