from scrapy import fetch, page_scraper
import info_category as ic
import scrape_all_books as iab
import infos_page as ip

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
    category_number = int(input('\n Veuillez choisir SVP le numero de la categorie que vous voulez scraper: '))
    return(dictionnaire[category_number])

# Cette fonction prend le lien de la categori choisi pour scraper les liens des livres dans la categorie choisi
def get_books_links(result_fetch_categori):
    links = []
    for link in result_fetch_categori:
        result_fetch = fetch(link)
        books_links = page_scraper(result_fetch).find('ol', {'class': 'row'})('h3')
        for book_link in books_links:      
            links.append("https://books.toscrape.com/catalogue/" + book_link.a['href'].replace('../', ''))
    return links

# Cette fonction prend les liens des livres pour scraper les titres pour les mettre ensuite dans un dictionnaire 
def get_product_titel(links_books):
    titels = []
    for link in links_books:
        result_fetch = fetch(link)
        titel = page_scraper(result_fetch).h1
        titels.append(titel.text)
    titel_number = [i for i in range(len(titels))]
    dictionnaire = dict(zip(titel_number , titels[0:(len(titels))]))
    for i in dictionnaire.items():
        print(i)

# Cette fonction prend les liens des lires pour les mettre ensuite dans un dictionnaire     
def choice_book(book_link):
    names_number = [i for i in range(len(book_link))]
    dictionnaire = dict(zip(names_number , book_link[0:(len(book_link))]))
    category_number = int(input('Veuillez choisir SVP le numero du livre que vous voulez scraper: '))
    return(dictionnaire[category_number])

if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    get_categorys_names(result_request)
    links = iab.all_categoris_links(result_request) # Scrape les liens des categories
    link_category = choice_category(links) 
    pagination = ic.pagination(fetch(link_category)) # Permet de defiler entre les pages si une categorie contien plusqu'une page 
    books_links = get_books_links(pagination)
    print('\n Cette categorie contient',(len(books_links)),'livres \n')
    get_product_titel(books_links)
    choice = choice_book(books_links)
    recup = ip.recup(fetch(choice)) # Scrape ous les informations sur le livre choisi 
    titel = ip.get_product_titel(fetch(choice)) # Scrape le titre du livre pour l'utiliser comment nom du fichier csv
    link_pic_book = ip.get_product_pic(fetch(choice))
    category_name = ip.get_product_category(fetch(choice))
    ip.download_pic(link_pic_book, titel, category_name)
    ip.creating_csv_file(recup,titel, category_name)