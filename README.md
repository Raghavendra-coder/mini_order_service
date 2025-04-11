# Mini Order Processing Service

This project implements a simple order processing system for a small online retailer. It allows for managing products, calculating order totals, applying discounts, handling shipping fees, and updating inventory in a transactional manner. It is built with **FastAPI** for the API, **SQLAlchemy** for ORM, and **SQLite** for database management.

## Features

- **Product Management**: View available products and create new ones.
- **Order Processing**: Create an order by selecting products, applying bulk discounts, calculating shipping fees, and updating inventory.
- **Input Validation**: Using **Pydantic** to validate the inputs for product creation and order submission.
- **Atomic Transactions**: Ensures inventory updates and order creation are handled atomically using **SQLAlchemy**.

## Requirements

- Python 3.8 or higher
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (or any other SQL database if needed)
- Alembic for migrations

