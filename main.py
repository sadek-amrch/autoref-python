from link import Link
from FileManager import FileManager
import sys

array_link = None
print("""
                _                  __
     /\        | |                / _|
    /  \  _   _| |_ ___  _ __ ___| |_
   / /\ \| | | | __/ _ \| '__/ _ \  _|
  / ____ \ |_| | || (_) | | |  __/ |
 /_/    \_\__,_|\__\___/|_|  \___|_|

                                      """)

print("***********************Autoref by Sadek, Adamo, Ismael**********************************")
file_link = input("Merci d'entrer le nom du fichier : ")

fm:FileManager = FileManager(file_link, 'out.txt')

array_link = (fm.read_file())

for f in array_link:
    link:Link = Link(f, "t")
    link.PrintLink()
