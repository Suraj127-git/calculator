from openai import OpenAI
from app.core.config import settings

client = OpenAI(base_url=settings.LMSTUDIO_URL, api_key="not-needed")
