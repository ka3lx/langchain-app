from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query - The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Weather in tokyo is sunny"


llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    response = agent.invoke(
        {"messages": [HumanMessage(content="What is the weather in Tokyo?")]}
    )
    print(response)


if __name__ == "__main__":
    main()
