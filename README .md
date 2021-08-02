# Programme d'extraction des prix 

* ##### Ce programme aide à extraire des informations inscrit dans le tableau ci-dessous sur des livres vendus sur le site web ["https://books.toscrape.com/index.html"](https://books.toscrape.com/index.html)

|product_page_url|universal_ product_code (upc)|title|price_including_tax|price_excluding_tax|number_available|product_description|category|review_rating|image_url
|-|-|-|-|-|-|-|-|-|-|

* ### Pré-requis
	- il faut installer un shell sur votre ordinateur, si non vous pouvez utiliser le terminal pré-installé avec votre système d'exploitation:

	- WINDOWS:
		-  touche Windows + R puis tapez 'cmd' puis ENTRER 

	- MAC:
		- Cliquez sur l’icône Launchpad dans le Dock, saisissez Terminal dans le champ de recherche, puis cliquez sur Terminal.
		- Dans le Finder, ouvrez le dossier /Applications/Utilitaires, puis cliquez deux fois sur Terminal.
	 
	- LINUX: 
		- ctrl + alt + t

* ### Démarrage
	- Sauvegardez tous les fichiers en format .py dans un même dossier
	- Démarrer votre terminal et diriger vous dans le dossier ou vous avez sauvegarder les fichiers ‘.py’
	- Installez les modules néssesaire pour le bon fonctionnement du programme
		```bash
		pip install -r requirements.txt
		``` 
	- Maintenant pour scraper les informations d'un seul livre il faut taper dans votre terminal:

		```shell
		python scrape_one_book.py
		```
	- Pour choisir une catégorie et scraper toutes les informations de tous les livres de cette catégorie il faut taper dans votre terminal:

		```shell
		python scrape_category.py
		```  
	* Finalement pour scraper tous les livres il faut taper dans votre terminal:

		```shell
		python scrape_all_books.py
		```

* ### Fabriqué avec
	- [VSCode](https://code.visualstudio.com/) 
	- [Cygwin](https://www.cygwin.com/install.html)

* ### Versions
	- 1.0

* ### Auteurs
	- Abid Oussama:
 
	 [oussamaabidd@gmail.com](oussamaabidd@gmail.com)

	- Mr Williams De Souza
