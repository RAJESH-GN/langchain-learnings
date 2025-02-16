from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from third_party.linkedin_scrape import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup

def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup(name)
    linkedin_information = scrape_linkedin_profile(linkedin_username)
    summary_template = """Given a linkedin information {information} about a person, 
    1. write a short summary about them.
    2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    #llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm 

    result = chain.invoke(input={"information": linkedin_information})

    print(result)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker entered")
    ice_break_with("Naga Rajesh Gaddale")