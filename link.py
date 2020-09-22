from datetime import datetime
from urllib.parse import urlparse

class Link:
    def __init__(self, link, title):
        self.link = link
        self.domaine = ""
        self.title = title

    def PrintLink(self):
        now = datetime.now()
        self.domaine = urlparse(self.link).netloc
        current_date = now.strftime("%d.%m.%Y")
        print(self.title + ", " + self.domaine + ", consuté le " + current_date + ", disponible à l'adresse suivante : " + self.link)

