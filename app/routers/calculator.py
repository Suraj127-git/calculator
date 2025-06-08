from fastapi import APIRouter, Depends, HTTPException
from app.schemas.calculator import CalculationCreate, CalculationRead
from app.services.calculator_service import CalculatorService
from app.core.dependencies import get_calculator_service


router = APIRouter(prefix="/calc", tags=["calculator"])

@router.post("/", response_model=CalculationRead)
def calculate(item: CalculationCreate, svc: CalculatorService = Depends(get_calculator_service)):
    try:
        return svc.compute_and_store(item.expression)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/history", response_model=list[CalculationRead])
def history(skip: int = 0, limit: int = 50, svc: CalculatorService = Depends(get_calculator_service)):
    return svc.get_history(skip, limit)


@router.post("/ai/", response_model=CalculationRead)
async def ai_calculate(item: CalculationCreate, svc: CalculatorService = Depends(get_calculator_service)):
    return await svc.ai_compute(item.expression)

