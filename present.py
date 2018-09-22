# coding: utf-8
result = "[{'NOM': 'Bordeaux superieur', 'PRODUIT_ID': 276}, {'NOM': 'Château Lataste', 'PRODUIT_ID': 279}, {'NOM': '', 'PRODUIT_ID': 281}, {'NOM': 'Domaine du Bourdier Bordeaux', 'PRODUIT_ID': 284}, {'NOM': 'Chateau La Croix Bigorre', 'PRODUIT_ID': 286}, {'NOM': 'Bordeaux élevé en fûts de chêne', 'PRODUIT_ID': 289}, {'NOM': 'Bordeaux Clairet', 'PRODUIT_ID': 291}, {'NOM': 'Bordeaux 2016', 'PRODUIT_ID': 294}, {'NOM': 'CHATEAU CARBONNIEUX GRAND CRU CLASSE DE GRAVES PESSAC - LEOGNAN', 'PRODUIT_ID': 296}, {'NOM': 'chateau ferrande ', 'PRODUIT_ID': 299}]"
result = result.replace('{','\n')
result = result.replace('}','')
print(result)