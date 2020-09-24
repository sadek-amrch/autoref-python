from link import Link
from curl import curl
from FileManager import FileManager
import time

array_link = None
file_ok: bool = False
curl: curl = curl()
count_success: int = 0
count_all: int = 0
count_fail: int = 0


print("""
                _                  __
     /\        | |                / _|
    /  \  _   _| |_ ___  _ __ ___| |_
   / /\ \| | | | __/ _ \| '__/ _ \  _|
  / ____ \ |_| | || (_) | | |  __/ |
 /_/    \_\__,_|\__\___/|_|  \___|_|

                                      """)

print("***********************Autoref by Sadek, Adamo, Ismael**********************************")

while not file_ok:
    try:
        file_link: str = input("Merci d'entrer le nom du fichier : ")
        fm: FileManager = FileManager(file_link, 'out.txt')
        array_link: list = (fm.read_file())
        file_ok = True
    except:
        print("Erreur de fichier introuvable ou illisible")


print("Démarrage du traitement des données")
time.sleep(0.2)
print('...')
time.sleep(0.2)
print('...')
time.sleep(0.2)
print("...\n\n")

"""
- Parcours le fichier (va être amélioré) 
"""
for line in array_link:
    title = curl.filter(line)
    count_all += 1
    if (title != 0):
        link: Link = Link(line, title)
        link.PrintLink()
        count_success += 1
    else:
        count_fail += 1

procent_success: float = (count_success / count_all) * 100

print("\n\nNombre de lien(s) traité(s) avec succès : {0} - Nombre de requêtes échoués : {1} - Nombre total : {2} - {3} %".format(
             count_success,
             count_fail,
             count_all,
             procent_success))




