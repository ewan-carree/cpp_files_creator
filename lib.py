"""
python3 projet_createFilescpp.py main_program_name header_name namespace

"""
import os #bibliothèque dédié aux besoins de gestion de fichiers et de dossiers
import sys
import glob # récupérer les dossiers et les fichiers correspondant à un motif
import datetime
import getpass

def extract_args():
	"""
	Cette fonction permet de récupérer les arguments passés lors de l'appel du programme

	"""
	arguments = sys.argv
	assert isinstance(arguments, list)
	arguments = arguments[1:]
	
	if len(arguments) == 0 or len(arguments)>3:
		print("Vous n'avez pas passé le bon nombre d'argument(s), veuillez les saisir à nouveau.")
		sys.exit(0)

	arguments = " ".join(arguments).lower().strip() #transforme la liste en chaine pour la travailler
	assert isinstance(arguments, str)

	arguments = arguments.split(" ") #retransforme la chaine en liste

	main = arguments[0]
	header = arguments[1]
	namespace = arguments[2]
	return main, header, namespace

def add_GNU():
	"""
	Cette fonction permet d'ajouter le fichier make nécessaire pour la compilation du code

	"""
	search = glob.glob("GNUmakefile") #recherche si GNU est dans le répertoire
	if not search :
		#add gnu
		pass

def get_path():
	"""
	Cette fontion récupère le chemin du répertoire dans lequel nous nous trouvons

	"""
	path = os.getcwd()
	return path

def create_file(fileName):
	"""
	Cette fonction créer un dossier où nous allons stocker nos futurs fichiers
	"""
	os.mkdir(fileName)

get_time = lambda : str(datetime.datetime.now()) #date et heure

get_userName = lambda : getpass.getuser() # nom de l'utilisateur