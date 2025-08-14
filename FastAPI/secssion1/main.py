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

@app.get("/items/")
def get_item_all(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            return {"error": "Item not found"}
        return item
    except Exception as e:
        return {"error": str(e)}
    
@app.delete('/items/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return {"message": "Item deleted successfully"}
        return {"error": "Item not found"}
    except Exception as e:
        return {"error": str(e)}