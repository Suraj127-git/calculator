from app.repositories.calculator_repo import CalculatorRepository
from app.schemas.calculator import CalculationCreate
from app.ai.chain import chain

class CalculatorService:
    def __init__(self, repo: CalculatorRepository):
        self.repo = repo

    def compute_and_store(self, expression: str):
        # Basic eval as placeholder; sanitize in prod
        result = eval(expression)
        calc = self.repo.create(CalculationCreate(expression=expression), result)
        return calc

    def get_history(self, skip: int = 0, limit: int = 100):
        return self.repo.list(skip, limit)

    async def ai_compute(self, expression: str):
        resp = await chain.arun(expr=expression)
        result = float(resp.strip())
        return self.repo.create(CalculationCreate(expression=expression), result)
