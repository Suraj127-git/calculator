from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM
from app.core.config import settings

# Prompt to extract mathematical expressions from natural language
extraction_prompt = PromptTemplate(
    input_variables=["text"],
    template=(
        "Extract the mathematical expression from the following input.\n"
        "Input: {text}\n"
        "Only return the valid math expression (like 2 + 3 * 2), without any explanation or symbols.\n"
        "Example:\n"
        "Input: 'what will be the ans 2 + 3 * 2'\n"
        "Output: 2 + 3 * 2\n"
    )
)

llm = OllamaLLM(model=settings.OLLAMA_MODEL)

# Create the LLM chain
chain = LLMChain(llm=llm, prompt=extraction_prompt)
