# coding: utf-8
from constantes import *
import pymysql
import pymysql.cursors
"""CONNECT TO THE DATABASE"""


var = NAME_CATEGORIES
choice = var[2]
fichier = open("BDD_save.txt", "a")
def delete_txt():
	"""On ouvre le fichier avec le mode write pour supprimer son contenu"""
	fichier = open("BDD_save.txt", "w")
	fichier.write("Liste de mes catégories produits dans ma BDD :")
	"""On ferme le fichier"""
	fichier.close()
def write_txt():
	"""on attribue le contenu du fichier à une variable"""
	lecture = str
	with open("BDD_save.txt", "r") as fichier:
		for l in fichier :
			lecture = l
			print(l)
	"""on test si la catégorie est presente dans la variable donc dans le fichier"""
	if choice in lecture :
		print(choice + " est bien présent dans la base de données")
		#select_and_substitut()
	else :
		print(choice + " n'est pas présent dans la base de données")
		with open("BDD_save.txt", "a") as fichier:
			fichier.write("\n" + choice + " ")
			fichier.close()

write_txt()