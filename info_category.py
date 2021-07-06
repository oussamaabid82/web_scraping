from bs4 import BeautifulSoup
from infos_page import fetch


def soup(infos, balise):
    soup = BeautifulSoup(infos, 'html.parser')
    categories = soup.find(balise, {'class': 'nav nav-list'})('a')
    print(categories) 


if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    soup(result_request,'ul')