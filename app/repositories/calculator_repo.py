from sqlalchemy.orm import Session
from app.db import models
from app.schemas.calculator import CalculationCreate

class CalculatorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj_in: CalculationCreate, result: float):
        db_obj = models.Calculation(expression=obj_in.expression, result=result)
        self.db.add(db_obj); self.db.commit(); self.db.refresh(db_obj)
        return db_obj

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Calculation).offset(skip).limit(limit).all()
