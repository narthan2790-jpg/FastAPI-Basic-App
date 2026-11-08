from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI application!",
        "status": "Success"
    }

@app.get("/about")
def about():
    return {
        "project": "FastAPI Basic App",
        "created_by": "Student"
    }