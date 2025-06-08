from pydantic import BaseModel
from datetime import datetime

class CalculationCreate(BaseModel):
    expression: str

class CalculationRead(CalculationCreate):
    id: int
    result: float
    created_at: datetime

    class Config:
        orm_mode = True
