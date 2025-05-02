import os
from dotenv import load_dotenv
load_dotenv()
from smolagents import OpenAIServerModel, CodeAgent,DuckDuckGoSearchTool

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_base="https://api.openai.com/v1",
    api_key= os.getenv("API_KEY"),
)

agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool()],
    description="Runs web searches for you. Give it your query as an argument.",
    planning_interval=3
)

agent.run(
    "Search for what is capital of India and then find all the popular places there then all the best food items in each of those places."
)