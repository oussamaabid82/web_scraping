from scrapy import fetch, page_scraper
import infos_page as ip
import csv
import os

# Si la cartégorie a plusieurs pages, cette fonction nous permet de scraper *tous les liens des pages de cette catégorie* 
def pagination (result_fetch_categori):
    link_categori = [result_fetch_categori[1]]
    page_footer = page_scraper(result_fetch_categori).find('li', {'class': 'current'})
    if page_footer:
        page_number = page_footer.text.rstrip().lstrip() # Page 1 of 4
        total_page_count = int(page_number.split(' ')[-1])
        for p in range(2,total_page_count+1):
            page_html = 'page-'+ str(p)  +'.html'
            link_categori.append(result_fetch_categori[1].replace('index.html', '') + page_html)
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
    recups = []
    for link in result_fetch:
        result_fetch_book = fetch(link)
        recups.append(ip.recup(result_fetch_book))
    return recups 

def category_name(result_fetch):
      resu_fetch = fetch(result_fetch) 
      get_name = page_scraper(resu_fetch).find('li', {'class': 'active'}).text
      return get_name

def creating_csv_file(recup, file_name):
    
    ligne_en_tete = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 
    'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    os.mkdir(file_name)
    with open (file_name + '.csv', 'w') as file:
        writer_csv = csv.writer(file, delimiter=',')
        writer_csv.writerow(ligne_en_tete)
        for line in recup:
            writer_csv.writerow(line)
        
    
if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
    name = category_name(result_request[1])
    link_categori = pagination(result_request)
    links_books = get_books_links(link_categori) 
    recup = get_infos_book(links_books)
    creating_csv_file(recup,name)