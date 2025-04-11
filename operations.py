from sqlalchemy.orm import Session
import models

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_inventory(db: Session, product_id: int, quantity: int):
    product = get_product(db, product_id)
    if product and product.quantity >= quantity:
        product.quantity -= quantity
        db.add(product)
        return True
    return False
