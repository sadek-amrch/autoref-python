from datetime import datetime

class Link:
    def __init__(self, link, domaine, title):
        self.link = link
        self.domaine = domaine
        self.title = title

    def PrintLink(self):
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        print(self.title + ", " + self.domaine + ", consuté le " + current_date + ", disponible à l'adresse suivante : " + self.link)

