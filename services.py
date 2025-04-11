from conf import BULK_DISCOUNT_THRESHOLD, BULK_DISCOUNT_PERCENTAGE, SHIPPING_THRESHOLD, SHIPPING_FEE
from sqlalchemy.orm import Session
import models

def process_order(db: Session, items):
    subtotal = 0
    inventory_check = True

    for item in items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product or product.quantity < item.quantity:
            inventory_check = False
            break

        price = product.price
        if item.quantity >= BULK_DISCOUNT_THRESHOLD:
            price *= (1 - BULK_DISCOUNT_PERCENTAGE)

        subtotal += price * item.quantity

    if not inventory_check:
        return None, "Insufficient inventory"

    total = subtotal
    if subtotal < SHIPPING_THRESHOLD:
        total += SHIPPING_FEE

    order = models.Order(total=total)
    db.add(order)
    db.flush()

    for item in items:
        db.query(models.Product).filter(models.Product.id == item.product_id).update({
            models.Product.quantity: models.Product.quantity - item.quantity
        })

        order_item = models.OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity)
        db.add(order_item)

    db.commit()
    return order, None
