import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(url: str, mock: bool = True) -> str:
    '''
    scrape information from a linkedin profile
    Manually scrape a linkedin profile information
    '''
    if(mock):
        return requests.get('https://gist.githubusercontent.com/RAJESH-GN/3864bc9c8b1647b38353114060b0de84/raw/2ba488c5f434bb3c886a083d7d3c28e5952d3773/rajesh-scrapin.json', timeout=10).json().get("person")
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": url
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
        response.json().get("person")
        filtered_data = {
            k: v
            for k, v in response.items()
            if v not in ([], "", None) and k not in ["certifications"]
        }
        return filtered_data


if __name__ == "__main__":
    result = scrape_linkedin_profile("https://www.linkedin.com/in/naga-rajesh-gaddale/")
    print(result)