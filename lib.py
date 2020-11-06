import os #bibliothèque dédié aux besoins de gestion de fichiers et de dossiers
import glob # récupérer les dossiers et les fichiers correspondant à un motif
import datetime
import getpass

import GNUMakeFile


def parseArguments():
  import argparse

  parser = argparse.ArgumentParser(description='Extract the necessary names to create c++ files')

  parser.add_argument("main_file_name", type = str , help = "This argument represents the way you want to call your main program file, usually it's called 'prog' or 'main'")
  parser.add_argument("header_file_name", type = str , help = "This argument represents the way you want to call your header program file, usually it's called the way you want to call you class")
  parser.add_argument("namespace_name", type = str , help = "This argument represents the way you want to encapsulate your header program file")
  parser.add_argument("--GNUversion", type = int, default=2, help = "Choose between the first version (S4) or the second one (S5 - by default)")
  parser.add_argument("--folder", type = bool, default=False, help = "Put files into a folder if True")
  parser.add_argument("--add", type = bool, default = False, help = "Use this if you want to add more folder with other classes (only when you already have run oncce at least the program")

  return parser.parse_args()

def addGNU(version, main_file_name):
  """
  Cette fonction permet d'ajouter le fichier make nécessaire pour la compilation du code

  """
  search = glob.glob("GNUmakefile") #recherche si GNU est dans le répertoire
  if not search :
    with open("GNUmakefile", 'w') as file:
      if version == 1:
        file.write(GNUMakeFile.v1.replace("EXE_PREFIX=prog", "EXE_PREFIX=" + main_file_name))
      elif version == 2:
        file.write(GNUMakeFile.v2.replace("EXE_PREFIX=prog", "EXE_PREFIX=" + main_file_name))
      else:
        raise Exception("You didn't enter a correct version")
  else:
    raise Exception("You already have a GNUMakeFile")




get_time = lambda : str(datetime.datetime.now()) #date et heure

get_userName = lambda : getpass.getuser() # nom de l'utilisateur

get_path = lambda : os.getcwd() #répertoire actuel

create_folder = lambda folderName : os.mkdir(folderName) #créer le dossier de travail

set_path = lambda path,folderName : os.chdir(path+'/'+folderName) #va dans le dossier de travail
