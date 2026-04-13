from fastapi import FastAPI

app = FastAPI(title="Comic Inventory System")


@app.get("/")
def root():
    return {"message": "Comic inventory system is running"}
