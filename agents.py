from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import calculate


"""
This file contains the definition of custom agents.
To create a Agent, you need to define the following:
1. Role: The role of the agent.
2. Backstory: The backstory of the agent.
3. Goal: The goal of the agent.
4. Tools: The tools that the agent has access to (optional).
5. Allow Delegation: Whether the agent can delegate tasks to other agents(optional).

Goal : Craete a 5 day tripplan for the user. Make sure to cover the itinerary with detailed per day plans.
       Include the budget, packing suggestions, flight and hotel costs.

Captain/Manger :
- Expert Travel agent


Employees :
- City Selection expert
- Local Expert


"""


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT41Mini = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        #self.calculator_tools = CalculatorTools()
        self.search_tools = SearchTools()
        #self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel agent",
            backstory=dedent(f"""
            You are an expert travel agent with 10 years of experience in travel planning.
            You are very knowledgeable about the best destinations, flights, hotels, and activities.
            You are also very good at budgeting and packing suggestions.
                """),
            goal=dedent(f"""
            To create a 5 day tripplan for the user. Make sure to cover the itinerary with detailed per day plans.
            Include the budget, packing suggestions, flight and hotel costs.
                """),
            tools=[SearchTools.search_internet, calculate],
            verbose=True,
            llm=self.OpenAIGPT41Mini,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection expert",
            backstory=dedent(f"""
            You are an expert in city selection.
            You are very knowledgeable about the best destinations, flights, hotels, and activities.
            You are also very good at budgeting and packing suggestions.
                """),
            goal=dedent(f"""
            To select the best city for the trip based on weather, season, and prices.
            """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT41Mini,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Expert at this city",
            backstory=dedent(f"""
            You are a local tour guide with 5 years of experience in providing insights about the city.
            You are very knowledgeable about the best attractions, restaurants, and activities.
            You are also very good at budgeting and packing suggestions.
                """),
            goal=dedent(f"""
            To provide the best insights about the selected city.
            """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT41Mini,
        )
