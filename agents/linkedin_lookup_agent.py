import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor) 
from langchain import hub
from agents.tools.tavilytools import get_profile_url_tavily

def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    summary_template = """Given a full name {name} of a person, i want you to find the linkedin profile of the person
      i want to only get the url of the linkedin profile as the output"""
    summary_prompt_template = PromptTemplate(
        input_variables=["name"], template=summary_template)
    
    tools_for_agent = [
        Tool(name="Crawl google for linkedin profile", description="useful for when u need to get the linkedin profile of a person",func=get_profile_url_tavily)
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent= create_react_agent(llm,tools_for_agent,react_prompt)
    agent_executor = AgentExecutor(agent = agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": summary_prompt_template.format_prompt(name=name)})
    linkedin_profile_url = result["output"]
    return linkedin_profile_url

if __name__ == "__main__":
    print(lookup(name= "Naga Rajesh Gaddale"))
