from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, operations, services
from db import SessionLocal, engine
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products", response_model=list[schemas.ProductOut])
def get_products(db: Session = Depends(get_db)):
    return operations.get_products(db)

@app.post("/orders")
def create_order(order: schemas.OrderIn, db: Session = Depends(get_db)):
    processed_order, error = services.process_order(db, order.items)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return JSONResponse(content={"order_id": processed_order.id, "total": processed_order.total})
