from fastapi import FastAPI

app = FastAPI(
    title="Menu Planning Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "Running",
        "application": "Menu Planning Agent"
    }