from scrapy import fetch, page_scraper
import infos_page as ip
import csv

# Si la cartégorie a plusieurs pages, cette fonction nous permet de scraper *tous les liens des pages de cette catégorie* 
def pagination (result_fetch_categori):
    link_categori = [result_fetch_categori[1]]
    if (page_scraper(result_fetch_categori).find('li', {'class': 'next'}).text) == "next":
        page_number = page_scraper(result_fetch_categori).find('li', {'class': 'next'}).a['href']
        link_categori.append(result_fetch_categori[1].replace('index.html', page_number))
    return link_categori

# Cette fonction scrape chaque *lien* de chaque *livre qui appatient à la catégorie* choisie 
def get_books_links(result_fetch_categori):
    links = []
    for link in result_fetch_categori:
        result_fetch = fetch(link)
        books_links = page_scraper(result_fetch).find('ol', {'class': 'row'})('h3')
        for book_link in books_links:      
            links.append("https://books.toscrape.com/catalogue/" + book_link.a['href'].replace('../', ''))
    return links

# Cette fonction scrape tous les informations *de chaque livre*   
def get_infos_book(result_fetch):
    for link in result_fetch:
        result_fetch_book = fetch(link)
        recups = ip.recup(result_fetch_book)
        return recups

def creating_csv_file(recup, file_name):
    ligne_en_tete = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 
    'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    with open (file_name + '.csv', 'w') as file:
        writer_csv = csv.writer(file, delimiter=',')
        writer_csv.writerow(ligne_en_tete)
        writer_csv.writerow(recup)
        
        
if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")
    link_categori = pagination(result_request)
    links_books = get_books_links(link_categori)
    recups = get_infos_book(links_books)
    file_name = input("nomme le fichier: ")
    creating_csv_file(recups,file_name)