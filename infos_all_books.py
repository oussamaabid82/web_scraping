from scrapy import fetch, page_scraper
import infos_page as ip
import info_category as ic
import csv

# Cette fonction scrape tous les liens des categories qui se trouve sur la page d'acceuil
def all_categoris_links(result_fetch):
    categoris_links = page_scraper(result_fetch).find('ul', {'class': 'nav nav-list'})('a')
    links_categorys = []
    for link_category in categoris_links:
        links_categorys.append("https://books.toscrape.com/" + link_category['href'].replace('../', ''))
    return (links_categorys[1:(len(links_categorys))])

# Cette fonction scrape tous les liens de tous les livres sur le site     
def get_links_all_books(result_fetch):
    all_books_links = ic.get_books_links(result_fetch)
    print (len(all_books_links))
'''
def creating_csv_file(recup):
    
    ligne_en_tete = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 
    'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    
    with open ( + '.csv', 'w') as file:
        writer_csv = csv.writer(file, delimiter=',')
        writer_csv.writerow(ligne_en_tete)
        writer_csv.writerow(recup)

'''
if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    all_links_of_categorys = all_categoris_links(result_request)
    links = get_links_all_books(all_links_of_categorys)
    recups = ic.get_infos_book(links)
    # name = ic.category_name
    # ic.creating_csv_file(recups,name)
    
    
    
    
