# coding: utf-8
from constantes import *
import pymysql
import pymysql.cursors
"""CONNECT TO THE DATABASE"""


var = NAME_CATEGORIES
choice = var[2]

fichier_texte = open("BDD_save.txt", "a")
def delete_txt():
	"""On ouvre le fichier_texte avec le mode write pour supprimer son contenu"""
	fichier_texte = open("BDD_save.txt", "w")
	fichier_texte.write("Liste de mes catégories produits dans ma BDD :")
	"""On ferme le fichier_texte"""
	fichier_texte.close()
def write_txt():
	"""on attribue le contenu du fichier_texte à une variable"""
	lecture = str
	with open("BDD_save.txt", "r") as fichier_texte:
		for l in fichier_texte :
			lecture = l
			print(l)
	"""on test si la catégorie est presente dans la variable donc dans le fichier_texte"""
	if choice in lecture :
		print(choice + " est bien présent dans la base de données")
		#select_and_substitut()
	else :
		print(choice + " n'est pas présent dans la base de données")
		with open("BDD_save.txt", "a") as fichier_texte:
			fichier_texte.write("\n" + choice + " ")
			fichier_texte.close()

write_txt()