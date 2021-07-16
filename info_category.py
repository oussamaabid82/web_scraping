import infos_page as ip
import csv

def get_books_links(result_fetch_categori):
    link_categori = [result_fetch_categori[1]]
    if (ip.page_scraper(result_fetch_categori).find('li', {'class': 'next'}).text) == "next":
        page_number = ip.page_scraper(result_fetch_categori).find('li', {'class': 'next'}).a['href']
        link_categori.append(result_fetch_categori[1].replace('index.html', page_number))
    links = []
    for link in link_categori:
        resut_fetch = ip.fetch(link)
        books_links = ip.page_scraper(resut_fetch).find('ol', {'class': 'row'})('h3')
        for book_link in books_links:      
            links.append("https://books.toscrape.com/catalogue/" + book_link.a['href'].replace('../', ''))
    return (links)
   
def get_infos_book(fetch):
    for link in fetch:
        result_fetch_book = ip.fetch(link)
        recups = ip.recup(result_fetch_book)
        return recups

if __name__ =='__main__':    
    result_request_categori = ip.fetch("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")
    links_books = get_books_links(result_request_categori)
    file_name = input("nomme le fichier: ")
    recups = get_infos_book(links_books)
    ip.creating_csv_file(recups,file_name)
    