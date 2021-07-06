import requests 
from bs4 import BeautifulSoup

def fetch(url):
    result = requests.get(url)
    if result.ok: 
        return result.text

def soup(infos, balise):
    soup = BeautifulSoup(infos, 'html.parser')
    infos_produit = soup.findAll(balise)
    return infos_produit
        
def product_info(tableau):
    info = soup(result_request,tableau)
    [print(tableau) for tableau in info ]
    return info 

def product_category(category):
    categorie = soup(result_request,category)
    [print(category) for category in categorie]
    return categorie

def product_titel(titel):
    titel = soup(result_request,titel)
    print(titel)
    return titel

def review_rating(review):
    note = soup(result_request,review)
    return note

def product_description(description):
    product_desc = soup(result_request,description)
    return product_desc

def product_pic(pic):
    product_img = soup(result_request,pic)
    return product_img

def recup(tableau,category,titel,rating,description,pic):
    info = product_info(tableau)
    category = product_category(category)
    titel = product_titel(titel)
    rating = review_rating(rating)
    description = product_description(description)
    image = product_pic(pic)
    a = (info, category, titel, rating, description, image)
    

if __name__ =='__main__':    
    result_request = fetch("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    recup('td', 'a', 'h1', 'i', 'p', 'img')
