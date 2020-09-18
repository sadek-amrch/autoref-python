from link import Link
from FileManager import FileManager
import sys

array_link = None

print("***********************Autoref by Sadek, Adamo, Ismael**********************************")
file_link = input("Merci d'entrer le nom du fichier : ")

fm:FileManager = FileManager(file_link, 'test.txt')

array_link = (fm.read_file())

for f in array_link:
    link:Link = Link(f,"t", "t")
    link.PrintLink()
