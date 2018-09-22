# coding: utf-8
import requests
import json
import pymysql
import pymysql.cursors
import math
import copy
from constantes import *
from gestion_BDD import *
"""CONNECT TO THE DATABASE"""
try :
	connection = pymysql.connect(host=HOST, #variable in file constantes.py
		                             user=USER,
		                             password=PASSWORD,
		                             db=DB,
		                             charset='utf8mb4',
		                             port = PORT,
		                             cursorclass=pymysql.cursors.DictCursor)
except :
		print("erreur de connexion")

def cleaning_tables():

	"""CLEANING TABLES"""

	with connection.cursor() as cursor:
		sql = "DELETE FROM `PRODUIT`"
		cursor.execute(sql, ())
		connection.commit()

	with connection.cursor() as cursor:
		sql = "DELETE FROM `CATEGORIES`;"
		cursor.execute(sql, ())
		connection.commit()

	with connection.cursor() as cursor:
		sql = "DELETE FROM `SUBSTITUT`;"
		cursor.execute(sql, ())
		connection.commit()
def reset_counter():
	"""RESET THE COUNTERS"""

	with connection.cursor() as cursor:
		sql = "ALTER TABLE `CATEGORIES` AUTO_INCREMENT=0;"
		cursor.execute(sql, ())
		connection.commit()

	with connection.cursor() as cursor:
		sql = "ALTER TABLE `PRODUIT` AUTO_INCREMENT=0;"
		cursor.execute(sql, ())
		connection.commit()

	with connection.cursor() as cursor:
		sql = "ALTER TABLE `SUBSTITUT` AUTO_INCREMENT=0;"
		cursor.execute(sql, ())
		connection.commit()
		"""CLEANING FILES TXT"""
"""LINK PRODUCT CATEGORY"""
categories = NAME_CATEGORIES #variable in file constantes.py
"""generate question"""
nb_series = range(1,len(categories)+1)
"""condition pour la boucle"""
generate_question = 1
propostion = []
"""depart de la liste de mots"""
mots = 0
while generate_question in nb_series :
	propostion.append((str(generate_question) + " " + categories[mots]))
	mots += 1
	generate_question +=1
propostion = str(propostion)
"""function link categories to BDD"""
def link(l = 0) :
	link_categories = 'https://fr.openfoodfacts.org/categorie/' + categories[l]
	return link_categories
"""test fonction"""
link_categories = link(l = 2)
"""condition for add product"""
mode_substitut_categorie = []

"""Separation line"""

transition = "\n"+"-"*204

"""PROGRAM FUNCTIONS"""

"""ADD PRODUCT"""

def Add_product():
	def AlimenterListeProduit():

	    for data in product ["products"]:
	        """nutriscore = (data["nutrition_grades"])"""
	        url.append((data["url"]))

	        name.append((data["product_name"]))

	        ns.append((data["nutrition_grades_tags"]))
	"""creation des listes"""

	url = []
	store = []
	name = []
	ns = []

	""" adaptation liens en fonctions du choix"""
	link_product = choice

	"""requêtes get"""
	r = requests.get('https://fr.openfoodfacts.org/categorie/' + link_product + '/1.json')
	"""dynamic link"""
	dynamic_link = 'https://fr.openfoodfacts.org/categorie/' + link_product + '/1.json'
	"""liens catégorie figé"""
	l = str
	l = r
	"""lecture json"""
	product = r.json()
	"""on remplie la liste des produits"""
	AlimenterListeProduit()
	"""calcul du nombre de produits"""
	count = product['count'] # Le nombre total de produits
	page_size = product['page_size'] # La taille d'une page

	nbPages = int( math.floor(count / page_size) + 1) # On déduit le nombre de pages
	print("nombre de pages = " +str(nbPages))
	i = 2
	while i <= nbPages: 

		r = requests.get('https://fr.openfoodfacts.org/categorie/' + link_product + "/" + str(i)+ '.json')
		dynamic_link = 'https://fr.openfoodfacts.org/categorie/' + link_product + "/" + str(i)+ '.json'
		product = r.json()
		AlimenterListeProduit()
		print("Page " + str(i) + " récupérée !")
		i += 1

	nb_product = (len(url))
	print(nb_product)
	ns_number = []
	ns = str(ns)
	ns_simple = []
	ns_number = []


	for x in ns :
		if x in ("a","b","c","d","e") :
			ns_simple.append(x)


	def convert(score = ns_simple):
		for i in score :
			if i == 'a' :
				ns_number.append(1)
			elif i == "b" :
				ns_number.append(2)
			elif i == "c" :
				ns_number.append(3)
			elif i == "d" :
				ns_number.append(4)
			elif i == "e" :
				ns_number.append(5)
		return ns_number
	convert()

	"""recovery'ID"""

	with connection.cursor() as cursor:

		sql = "SELECT MAX(`ID`) FROM `CATEGORIES`"
		cursor.execute(sql, ())
		ID = cursor.fetchall()

	ID = str(ID)
	N_ID = ""
	for x in ID :
		if x in ("0","1","2","3","4","5","6","7","8","9") :
			N_ID+=(x)

	print(N_ID)
	N_ID = int(N_ID)

	"""INSERT TO BDD"""

	liste_position = 0
	try :
		while liste_position < nb_product :
			with connection.cursor() as cursor:
			    sql = "INSERT INTO `PRODUIT` (`NOM`,`PRODUIT_URL`,`NUTRISCORE`, `CATEGORIE_ID`) VALUES (%s, %s, %s, %s)"
			    cursor.execute(sql, (name[liste_position], url[liste_position], ns_number[liste_position], N_ID))

			connection.commit()
			liste_position = liste_position + 1
			if liste_position == liste_position + 10:
				print(str(liste_position)+"produits enregistré dans la BDD ! ")
			if liste_position == nb_product :
				print(str(liste_position)+"produits enregistré dans la BDD ! ")
	except :
		pass
		
""" SELECT AND SUBSTITUT"""
		
def select_and_substitut():
	with connection.cursor() as cursor:

		sql = "SELECT PRODUIT.NOM, PRODUIT.PRODUIT_ID FROM `PRODUIT` INNER JOIN `CATEGORIES` ON PRODUIT.CATEGORIE_ID = CATEGORIES.ID WHERE CATEGORIES.NOM = %s AND NUTRISCORE >= 3 LIMIT 10"
		cursor.execute(sql, (name_categories))
		result = cursor.fetchall()
		result = str(result)
		result = result.replace('{','\n')
		result = result.replace('}','')
		print(result)

	choice_produit = input("\n Indiquer le numéro du produit que vous souhaitez remplacer : ")

	with connection.cursor() as cursor:

		sql = "SELECT PRODUIT.NOM, PRODUIT.PRODUIT_ID FROM `PRODUIT` INNER JOIN `CATEGORIES` ON PRODUIT.CATEGORIE_ID = CATEGORIES.ID WHERE CATEGORIES.NOM = %s AND NUTRISCORE <	3 LIMIT 5"
		cursor.execute(sql, (name_categories))
		result = cursor.fetchall()
		result = str(result)
		result = result.replace('{','\n')
		result = result.replace('}','')
		print(result)


	choice_substitut = input("\n Indiquer le numéro du produit que vous souhaitez consulter ")
	print(transition)
	with connection.cursor() as cursor:

		sql = "SELECT `PRODUIT_URL` FROM `PRODUIT` WHERE `PRODUIT_ID`=%s"
		cursor.execute(sql, (choice_substitut))
		link_result = cursor.fetchall()

	link_result = str(link_result)
	n_link = ''
	for x in link_result :
		if x in ("0","1","2","3","4","5","6","7","8","9") :
			n_link+=(x)
			if len(n_link) == 13 :
				break
			

	link_url = "https://fr.openfoodfacts.org/api/v0/produit/{}.json".format(n_link)
	print(link_url)
	ri = requests.get(link_url)
	product_substitut = json.loads(ri.text)
	product_name = (product_substitut["product"]["product_name"])
	description = (product_substitut["product"]["ingredients_text_debug"])
	link_url = (product_substitut["product"]["image_front_url"])
	stores = (product_substitut["product"]["stores"])

	def afficher_descr():
		result_text = ("voici le produit " + product_name + "\n\n" + "Ce produit contient : " + description + "\n\n" + " vous pouvez retrouver le lien ici même : " + link_url + "\n\n" + "Il est disponible dans les magasins : " + stores )
		return result_text


	ok = afficher_descr()
	print(ok)

	mode_substitut = 0
	while mode_substitut == 0:
		try :
			save_BDD = input("Voulez-vous enregistrer ce produit dans vos achats ? 1/oui ; 2/non ")
			save_BDD = int(save_BDD)
			if save_BDD == 1 :
				print("Enregistrement en cours...")
				with connection.cursor() as cursor:
					sql = "INSERT INTO `SUBSTITUT` (`NOM`,`STORE`,`SUBSTITUT_URL`,`DESCRIPTION`) VALUES (%s, %s, %s, %s)"
					cursor.execute(sql, (product_name, stores, link_url, description))

					connection.commit()
				print("enregistrement terminé !")
				mode_substitut = 1
			elif save_BDD == 2:
				print("\n enregistrement non effectuée, \n retour vers le menu")
				mode_substitut = 1
			elif save_BDD > 2 :
				print("{} n'est pas dans les numéros proposés\n".format(save_BDD))
		except ValueError :
			if len(save_BDD) > 1 :
				print("\nOops! {} est un mot, veuillez recommencer : \n".format(save_BDD))
			else :
				print("\nOops! {} est une lettre, veuillez recommencer : \n".format(save_BDD))

"""MAIN LOOP"""

continu = 0
while continu == 0 :
	try :
		print(transition)
		terminal_mode = input("\n1 - Quel aliment souhaitez-vous remplacer ? \n2 - Retrouver mes aliments substitués. \n3 - Sortir du programme ? \n4 - Nettoyer la Base de données")
		terminal_mode = int(terminal_mode)

		"""mode remplacement"""
		while terminal_mode == 1 :
			print(transition)
			"""condition for mode_substitut catégorie"""
			print(mode_substitut_categorie)
			temp_categorie = int
			try :
				keyboard_input = input ("choissisez votre catégorie de produit : " + propostion)
				keyboard_input = int(keyboard_input)
				choice = str
				name_categories = str

				if keyboard_input in nb_series :
					choice = categories[keyboard_input - 1]
					name_categories = categories[keyboard_input - 1]
					link_categories = link(l = keyboard_input - 1)
					temp_categorie = keyboard_input
					print(temp_categorie)
				elif keyboard_input not in nb_series :
					print("{} n'est pas dans les numéros proposés\n".format(keyboard_input))
					break

				if keyboard_input in mode_substitut_categorie :
					print("catégories {} existante dans la BDD".format(name_categories))
					select_and_substitut()
				else :
					with connection.cursor() as cursor:
						sql = "INSERT INTO `CATEGORIES` (`NOM`,`LINK_OFF`) VALUES (%s, %s)"
						cursor.execute(sql, (name_categories, link_categories))
					mode_substitut_categorie.append(temp_categorie)
					connection.commit()
					Add_product()
					print(transition)
					select_and_substitut()

			except ValueError :
				print("\nOops! {} est une lettre, veuillez recommencer : \n".format(keyboard_input))
				
			terminal_mode = 0

		"""Consult database"""

		while terminal_mode == 2 :
			print(transition)
			print("Voici vos produits : \n ")
			with connection.cursor() as cursor:
				sql = "SELECT `NOM`,`STORE`,`SUBSTITUT_ID` FROM `SUBSTITUT`"
				cursor.execute(sql, ())
				my_product = cursor.fetchall()
				my_product = str(my_product)
				my_product = my_product.replace('{','\n')
				my_product = my_product.replace('}','')
				print(my_product)


			terminal_mode = 0

		"""exit mode"""

		if terminal_mode == 3 :
			print(transition)
			print("Aurevoir ! ")
			continu = 1

		if terminal_mode == 4 :
			delete_txt()
			cleaning_tables()
			reset_counter()

		elif terminal_mode > 4 :
			print("{} n'est pas dans les numéros proposés\n".format(terminal_mode))

	except ValueError :
		if len(terminal_mode) > 1 :
			print("\nOops! {} est un mot, veuillez recommencer : \n".format(terminal_mode))
		else :
			print("\nOops! {} est une lettre, veuillez recommencer : \n".format(terminal_mode))