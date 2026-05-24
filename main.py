from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str):
    """
    Tool that searches over the internet
    Args:
        query - The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What are the top 3 job positings for AI engineer on linkedin?"
                )
            ]
        }
    )
    print(response)


if __name__ == "__main__":
    main()
