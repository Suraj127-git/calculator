from app.repositories.calculator_repo import CalculatorRepository
from app.schemas.calculator import CalculationCreate
from app.ai.chain import chain
import re

class CalculatorService:
    def __init__(self, repo: CalculatorRepository):
        self.repo = repo

    def compute_and_store(self, expression: str):
        # Basic eval placeholder; sanitize in production!
        result = eval(expression)
        return self.repo.create(CalculationCreate(expression=expression), result)

    def get_history(self, skip: int = 0, limit: int = 100):
        return self.repo.list(skip, limit)

    async def ai_compute(self, expression: str):
        # Fire the chain and get raw output (could be dict or string)
        raw = await chain.ainvoke(expression)

        # If the chain returned a dict, extract the main text field
        if isinstance(raw, dict):
            # Common keys could be 'text', 'response', or first value
            raw_text = raw.get("text") or raw.get("response") or next(iter(raw.values()), None)
        else:
            raw_text = raw

        if raw_text is None:
            raise ValueError(f"AI returned unexpected non-text response: {raw!r}")

        # Extract the first floating-point or integer number
        match = re.search(r"-?\d+(?:\.\d+)?", str(raw_text))
        if not match:
            raise ValueError(f"AI returned non-numeric response: {raw_text!r}")

        result = float(match.group(0))
        return self.repo.create(CalculationCreate(expression=expression), result)
