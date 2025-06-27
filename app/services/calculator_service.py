import re
from app.repositories.calculator_repo import CalculatorRepository
from app.schemas.calculator import CalculationCreate
from app.ai.chain import chain

class CalculatorService:
    def __init__(self, repo: CalculatorRepository):
        self.repo = repo

    def compute_and_store(self, expression: str):
        result = eval(expression)
        return self.repo.create(CalculationCreate(expression=expression), result)

    def get_history(self, skip: int = 0, limit: int = 100):
        return self.repo.list(skip, limit)

    async def ai_compute(self, user_input: str):
        print(f"AI Chain Input: {user_input}")
        raw = await chain.ainvoke({"text": user_input})
        print(f"AI Chain Raw Output: {raw}")

        # Extract LLM text output
        if isinstance(raw, dict):
            raw_text = raw.get("text") or raw.get("response") or next(iter(raw.values()), "")
        else:
            raw_text = str(raw)

        if not raw_text:
            raise ValueError(f"Empty response from AI: {raw!r}")

        # Split into non-empty lines
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        print(f"LLM returned lines: {lines}")

        # Decide whether to trust LLM extraction: only if single line
        if len(lines) == 1:
            expr_line = lines[0]
            print(f"Using LLM-extracted expression line: {expr_line}")
            clean_expr_parts = re.findall(r"[0-9\.\+\-\*\/\(\)\s]+", expr_line)
            expr = "".join(clean_expr_parts).strip()
        else:
            # Fallback: extract from original user input
            print("Multiple lines from LLM; falling back to regex on user input.")
            m = re.search(r"\d+(?:\s*[\+\-\*\/]\s*\d+)+", user_input)
            if not m:
                raise ValueError(f"Could not extract expression from: {user_input!r}")
            expr = m.group(0)

        print(f"Final math expression to eval: {expr}")

        try:
            result = float(eval(expr))
        except Exception as e:
            raise ValueError(f"Invalid expression '{expr}': {e}")

        return self.repo.create(CalculationCreate(expression=expr), result)
