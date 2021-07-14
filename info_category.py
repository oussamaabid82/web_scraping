import infos_page as ip
import csv

def get_books_links(result_fetch_categori):
    books_links = ip.page_scraper(result_fetch_categori).find('ol', {'class': 'row'})('a')
    links = []
    for i in books_links:
        links.append("https://books.toscrape.com/catalogue/" + i['href'].replace('../', ''))
    for link in links:
        return (str(link))

if __name__ =='__main__':    
    result_request_categori = ip.fetch("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    links_books = get_books_links(result_request_categori)
    result_fetch_books = ip.fetch(links_books)
    recups = ip.recup(result_fetch_books)
    ip.info_page_csv(recups)