from pydantic import BaseModel

class CalculationCreate(BaseModel):
    expression: str

class CalculationRead(CalculationCreate):
    id: int
    result: float
    created_at: str

    class Config:
        orm_mode = True
