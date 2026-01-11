from fastapi import FastAPI
from backend.api import goals, progress, confidence, feedback

app = FastAPI(title="Exam Anxiety Reduction System")

@app.get("/")
def root():
    return {"message": "Exam Anxiety Reduction System is running"}

app.include_router(goals.router, prefix="/goals", tags=["Micro Goals"])
app.include_router(progress.router, prefix="/progress", tags=["Progress"])
app.include_router(confidence.router, prefix="/confidence", tags=["Confidence"])
app.include_router(feedback.router, prefix="/feedback", tags=["Encouragement"])
