from scrapy import fetch, page_scraper
from scrape_one_book import get_categorys_names, choice_category
import infos_category as ic
import scrape_all_books as iab


if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    get_categorys_names(result_request) # Cette fonction scrape les noms des categories pour les mettre ensuite dans un dictionnaire
    links = iab.all_categoris_links(result_request) # Cette fonction scrape tous les liens des categories qui se trouve sur la page d'acceuil
    link_category = choice_category(links)
    pagination = ic.pagination(fetch(link_category))   
    books_links = ic.get_books_links(pagination) # Cette fonction scrape chaque *lien* de chaque *livre qui appatient à la catégorie* choisie 
    print('Cette categorie contient',(len(books_links)),'livres')
    recup = ic.get_infos_book(books_links)
    name_category = ic.category_name(link_category)
    ic.creating_csv_file(recup,name_category,name_category)