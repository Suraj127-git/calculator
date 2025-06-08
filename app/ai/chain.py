from langchain import LLMChain, PromptTemplate
from app.ai.llm_client import client

prompt = PromptTemplate(
    input_variables=["expr"],
    template="Compute the result of the expression: {expr}"
)
llm = client.as_openai_compatible()
chain = LLMChain(llm=llm, prompt=prompt)
