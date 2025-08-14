from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from models import Item

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

