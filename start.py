from scrapy import fetch, page_scraper
import info_category as ic
import infos_all_books as iab


def get_categorys_names(result_fetch):
    names = []
    get_names = page_scraper(result_fetch).find('ul', {'class': 'nav nav-list'})('a')
    for name in get_names:
        names.append(name.text.rstrip().lstrip())
    names_number = [i for i in range(len(names))]
    dictionnaire = dict(zip(names_number , names[1:(len(names))]))
    for i in dictionnaire.items():
        print(i)

def choice_category(category_links):
    names_number = [i for i in range(len(category_links))]
    dictionnaire = dict(zip(names_number , category_links[0:(len(category_links))]))
    category_number = int(input('Veuillez choisir SVP le numero de la categorie que vous voulez scraper: '))
    return(dictionnaire[category_number])

def category_name(result_fetch):
      resu_fetch = fetch(result_fetch) 
      get_name = page_scraper(resu_fetch).find('li', {'class': 'active'}).text
      return get_name

if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/index.html")
    get_categorys_names(result_request)
    links = iab.all_categoris_links(result_request)
    link_category = choice_category(links)
    pagination = ic.pagination(fetch(link_category))   
    books_links = ic.get_books_links(pagination)
    print('Cette categorie contient',(len(books_links)),'livres')
    infos_books = ic.get_infos_book(books_links)
    # print('\n', infos_books)
    name_category = category_name(link_category)
    ic.creating_csv_file(infos_books,name_category)