from scrapy import fetch, page_scraper
import urllib.request
import csv
import os

def affichage_link(url):
    return str(url)
 
def get_universal_product_code(result_fetch):
    commercial_infos = page_scraper(result_fetch).findAll('td')
    return (commercial_infos[0].text)

def get_product_titel(result_fetch):
    titel = page_scraper(result_fetch).h1
    titel_less_caracter = titel.text.replace(':','').replace('/','').replace("\ ",'').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')
    return (titel_less_caracter) 

def get_price_including_tax(result_fetch):
    commercial_infos = page_scraper(result_fetch).findAll('td')
    return (commercial_infos[2].text)

def get_price_excluding_tax(result_fetch):
    commercial_infos = page_scraper(result_fetch).findAll('td')
    return (commercial_infos[3].text)

def get_number_available(result_fetch):
    commercial_infos = page_scraper(result_fetch).findAll('td') 
    return (commercial_infos[5].text)

def get_product_description(result_fetch):
    description = page_scraper(result_fetch).find('article', {'class': 'product_page'})('p')
    return (description[3].text)
 
def get_product_category(result_fetch):
    categorie = page_scraper(result_fetch).find('ul', {'class': 'breadcrumb'})('a')
    return (categorie[2].text)

def get_review_rating(result_fetch):    
    rev_rating = page_scraper(result_fetch).find('p', {'class': 'star-rating'})
    return (rev_rating.attrs.get('class')[1])

def get_product_pic(result_fetch):
    product_img = page_scraper(result_fetch).find('div', {'class': 'item active'})('img')
    links_pic=[]
    for i in product_img:
        links_pic.append("https://books.toscrape.com/" + i['src'].replace('../', ''))
    return (links_pic[0])

def download_pic(link_product_pic, titel, folder_name):
    if not os.path.exists ('./' + "P2_03_SCRAPING_RESULT" ):
        os.mkdir ('./' + "P2_03_SCRAPING_RESULT")
    if not os.path.exists ('./' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name ):
        os.mkdir ('./' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name)
    if(len(titel))> 160:
        img_name = './' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name + '/' + str(titel[0:140]) + '.jpg'
    else:
        img_name = './' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name + '/' + str(titel) + '.jpg' 
    urllib.request.urlretrieve(link_product_pic,img_name)

def recup(result_fetch):
    affichage_url = affichage_link(result_fetch[1])
    pro_upc = get_universal_product_code(result_fetch)
    pro_titel = get_product_titel(result_fetch)
    pro_price_tax_inc = get_price_including_tax(result_fetch)
    pro_price_tax_exc = get_price_excluding_tax(result_fetch)
    pro_num_available = get_number_available(result_fetch)
    pro_description = get_product_description(result_fetch)
    pro_category = get_product_category(result_fetch)
    pro_rating = get_review_rating(result_fetch)
    pro_picture = get_product_pic(result_fetch)
    download_img = download_pic(pro_picture, pro_titel,pro_category)
    all_program = [affichage_url, pro_upc, pro_titel, pro_price_tax_inc, pro_price_tax_exc, pro_num_available, pro_description, pro_category, pro_rating, pro_picture, download_img]
    return all_program

def creating_csv_file(program, file_name, folder_name):
    ligne_en_tete = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 
    'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    if(len(file_name))> 140:
        with open ('./' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name + '/' + file_name[0:100] + '.csv', 'w', encoding="utf-8") as file:
            writer_csv = csv.writer(file, delimiter=',')
            writer_csv.writerow(ligne_en_tete)
            writer_csv.writerow(program)
    else:
        with open ('./' + "P2_03_SCRAPING_RESULT" + '/ ' + folder_name + '/' + file_name + '.csv', 'w', encoding="utf-8") as file:
            writer_csv = csv.writer(file, delimiter=',')
            writer_csv.writerow(ligne_en_tete)
            writer_csv.writerow(program)
        
if __name__ =='__main__':
    result_request = fetch("https://books.toscrape.com/catalogue/political-suicide-missteps-peccadilloes-bad-calls-backroom-hijinx-sordid-pasts-rotten-breaks-and-just-plain-dumb-mistakes-in-the-annals-of-american-politics_917/index.html")
    recup_program = recup(result_request)
    file_name = get_product_titel(result_request)
    category_name = get_product_category(result_request)
    creating_csv_file(recup_program, file_name,category_name )