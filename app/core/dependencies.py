from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.repositories.calculator_repo import CalculatorRepository
from app.services.calculator_service import CalculatorService

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

def get_calculator_service(db: Session = Depends(get_db)):
    return CalculatorService(CalculatorRepository(db))
