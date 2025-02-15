from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_party.linkedin_scrape import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello, World!")
    summary_template = """Given a linkedin information {information} about a person, 
    1. write a short summary about them.
    2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm 
    linkedin_information = scrape_linkedin_profile("https://www.linkedin.com/in/naga-rajesh-gaddale/")

    result = chain.invoke(input={"information": linkedin_information})

    print(result)
