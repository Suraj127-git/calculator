from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from app.core.config import settings

prompt = PromptTemplate(
    input_variables=["expr"],
    template="Compute the result of the expression: {expr}"
)

llm = OpenAI(
    base_url=settings.LMSTUDIO_URL,
    api_key="not-needed",
    temperature=0
)

chain = LLMChain(llm=llm, prompt=prompt)
