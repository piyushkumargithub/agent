import os
from dotenv import load_dotenv
load_dotenv()
from smolagents import OpenAIServerModel, CodeAgent

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_base="https://api.openai.com/v1",
    api_key= os.getenv("API_KEY"),
)

agent = CodeAgent(
    model=model,
    tools=[]
)

agent.run(
    "Write a fibonnaci function in python"
)