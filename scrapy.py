import requests 
from bs4 import BeautifulSoup

def fetch(url):
    result = requests.get(url)
    if result.ok: 
        return (result.content , url)
    
def page_scraper(result_fetch):
    soup = BeautifulSoup((result_fetch[0]), 'html.parser')
    return soup

if __name__ =='__main__':
    result_request = fetch()
    page_scraper(result_request)