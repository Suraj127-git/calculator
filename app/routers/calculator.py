from fastapi import APIRouter, Depends, HTTPException
from app.schemas.calculator import CalculationCreate, CalculationRead
from app.services.calculator_service import CalculatorService
from app.core.dependencies import get_calculator_service
import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/calc", tags=["calculator"])

@router.post("/", response_model=CalculationRead)
def calculate(item: CalculationCreate, svc: CalculatorService = Depends(get_calculator_service)):
    logger.info(f"Received calculation request with expression: {item.expression}")
    try:
        result = svc.compute_and_store(item.expression)
        logger.info(f"Successfully calculated expression. Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error calculating expression: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/history", response_model=list[CalculationRead])
def history(skip: int = 0, limit: int = 50, svc: CalculatorService = Depends(get_calculator_service)):
    logger.info(f"Fetching calculation history with skip={skip}, limit={limit}")
    result = svc.get_history(skip, limit)
    logger.info(f"Retrieved {len(result)} history records")
    return result

@router.post("/ai/", response_model=CalculationRead)
async def ai_calculate(item: CalculationCreate, svc: CalculatorService = Depends(get_calculator_service)):
    logger.info(f"Received AI calculation request with expression: {item.expression}")
    result = await svc.ai_compute(item.expression)
    logger.info(f"Successfully completed AI calculation. Result: {result}")
    return result

