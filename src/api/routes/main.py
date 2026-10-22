from fastapi import FastAPI

from .predict import router

app = FastAPI(
    title="HarassmentProject API",
    description="Harassment detection using Machine Learning",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Harassment detection API is running"}

app.include_router(router)
