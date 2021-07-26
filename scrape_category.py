from scrapy import fetch, page_scraper
import info_category as ic
import scrape_all_books as iab

# Cette fonction scrape les noms des categories pour les mettre ensuite dans un dictionnaire
def get_categorys_names(result_fetch):
    names = []
    get_names = page_scraper(result_fetch).find('ul', {'class': 'nav nav-list'})('a')
    for name in get_names:
        names.append(name.text.rstrip().lstrip())
    names_number = [i for i in range(len(names))]
    dictionnaire = dict(zip(names_number , names[1:(len(names))]))
    for i in dictionnaire.items():
        print(i)
        
# Cette fonction scrape les liens des categories pour les mettre ensuite dans un dictionnaire et demande a l'utilisateur a choisir une categorie 
def choice_category(category_links):
    names_number = [i for i in range(len(category_links))]
    dictionnaire = dict(zip(names_number , category_links[0:(len(category_links))]))
    category_number = int(input('Veuillez choisir SVP le numero de la categorie que vous voulez scraper: '))
    return(dictionnaire[category_number])

if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    get_categorys_names(result_request)
    links = iab.all_categoris_links(result_request) # Cette fonction scrape tous les liens des categories qui se trouve sur la page d'acceuil
    link_category = choice_category(links)
    pagination = ic.pagination(fetch(link_category))   
    books_links = ic.get_books_links(pagination) # Cette fonction scrape chaque *lien* de chaque *livre qui appatient à la catégorie* choisie 
    print('Cette categorie contient',(len(books_links)),'livres')
    recup = ic.get_infos_book(books_links)
    name_category = ic.category_name(link_category)
    ic.creating_csv_file(recup,name_category,name_category)