Guide d'installation du programme :

1 Télécharger le repositories Git hub à l'aide d'un "git clone https://github.com/Wanbli83470/P5.git" dans votre terminal ou bien en téléchargeant le zip.

2 Connecter vous à votre client mySQL, puis exécuter le fichier BDD.sql pour initer la base de données

3 Indiquer dans le fichier P5.py votre nom d'utilisateur et le mot de passe SQL de votre poste.

4 Activer l'environnement virtuel sur votre terminal à l'aide de la commande "source/venv/bin/activate"

5 Installer les paquets et les dépendances à l'aide de la commande "pip install -r requirements.txt"

6 Exécuter le fichier P5.py en indiquant dans le terminal "python P5.py" en ayant pris soins d'activer l'environnement virtuel.

Configuration de la base MYSQL :

1 Le fichier constantes.py vous permet en premier lieu de modifier :
le nom de la base de données, l'hote, le mot de passe ainsi que le port.
2 De plus il vous est possible d'ajouter le téléchargement d'une catégorie en ajoutant celle-ci à l'intérieur de la liste "NAME_CATEGORIES" en séparant son nom d'une virgule et en contant la chaine de caracètre entre guillemets.
3 Enfin si vous souhaitez modifier le nom des tables vous pouvez modifier celle-ci dans le fichier BDD.sql avant la création de votre BDD. Puis dans un second temps en modifiant le contenue des variables correspondantes dans constantes.py

Remarque :
Le fichier save_BDD.txt est automatiquement mis à jour à l'aide du programme Python "P5.py" et son bon fonctionnement ne dépend que de celui-ci. 
