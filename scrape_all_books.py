from scrapy import fetch, page_scraper
import infos_category as ic

# Cette fonction scrape tous les liens des categories qui se trouve sur la page d'acceuil
def all_categoris_links(result_fetch):
    categoris_links = page_scraper(result_fetch).find('ul', {'class': 'nav nav-list'})('a')
    links_categorys = []
    for link_category in categoris_links:
        links_categorys.append("https://books.toscrape.com/" + link_category['href'].replace('../', ''))
    return (links_categorys[1:(len(links_categorys))])

if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    all_links_of_categorys = all_categoris_links(result_request)
    for link in all_links_of_categorys:
        pagination = ic.pagination(fetch(link)) # parcourir les pages de la categorie si elle contient plusier pages et affice les liens de ces pages 
        links = ic.get_books_links(pagination) # affiche les liens des chaque livre    
        recups = ic.get_infos_book(links) # affiche les informations demander
        name_category = ic.category_name(fetch(link)[1]) # affiche le nom de la categorie
        ic.creating_csv_file(recups,name_category,name_category) 