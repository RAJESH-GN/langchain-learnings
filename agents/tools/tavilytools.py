from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name:str) -> str:
    search = TavilySearchResults()
    res = search.run(name)
    return res