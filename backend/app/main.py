from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import collection
    
app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is alive 🚀"}

@app.post("/items")
def create_item(item: dict):
    collection.insert_one(item)
    return {"status": "saved"}

@app.get("/items")
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return items