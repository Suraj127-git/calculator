from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM
from app.core.config import settings

prompt = PromptTemplate(
    input_variables=["expr"],
    template=(
        "Compute the result of the expression: {expr}\n"
        "Respond with only the number, without any explanation."
    )
)

llm = OllamaLLM(model=settings.OLLAMA_MODEL, temperature=0)

chain = LLMChain(llm=llm, prompt=prompt)
