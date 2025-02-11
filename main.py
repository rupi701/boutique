from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.dresses import Dress
from setup import get_db

app = FastAPI()

class FrontEndDressRequestType(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    shopping_cart: int
    sku: str
    transaction_date: str

    def get_default_quantity(self):
        return 10


@app.post("/add_dress")
def add_dress(frontend_dress: FrontEndDressRequestType, db: Session = Depends(get_db)):
    db_dress = Dress(
        name=frontend_dress.name,
        description=frontend_dress.description,
        price=frontend_dress.price,
        quantity=  frontend_dress.quantity if frontend_dress.quantity > 0 else frontend_dress.get_default_quantity(),
    )
    db.add(db_dress)
    db.commit()
    db.refresh(db_dress)
    return db_dress

@app.get("/get_dresses")
def get_dresses(db: Session = Depends(get_db)):
    dresses = db.query(Dress).all()
    return dresses

@app.get("/get_dresses/{dress_id}")
def get_dress(dress_id: int, db: Session = Depends(get_db)):
    dress = db.query(Dress).filter(Dress.id == dress_id).first()
    return dress

@app.delete("/delete_dress/{dress_id}")
def delete_dress(dress_id: int, db: Session = Depends(get_db)):
    dress = db.query(Dress).filter(Dress.id == dress_id).first()
    db.delete(dress)
    db.commit()
    return 'dress deleted'

@app.put("/update_dress/{dress_id}")
def update_dress(dress_id: int, front_end_dress: FrontEndDressRequestType, db: Session = Depends(get_db)):
    dress = db.query(Dress).filter(Dress.id == dress_id).first()
    dress.name = front_end_dress.name
    dress.description = front_end_dress.description
    dress.price = front_end_dress.price
    dress.quantity = front_end_dress.quantity
    db.commit()
    db.refresh(dress)
    return dress

@app.get("/")
async def root():
    return {"message": "Hello Rupi's Boutique"}


