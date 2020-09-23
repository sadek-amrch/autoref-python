from datetime import datetime
from urllib.parse import urlparse

class Link:
    def __init__(self, link, title):
        self.link: str = link
        self.domaine: str = ""
        self.title: str = title

    def PrintLink(self):
        now: str = datetime.now()
        self.domaine = urlparse(self.link).netloc
        current_date: str = now.strftime("%d.%m.%Y")
        print(self.title + ", " + self.domaine + ", consuté le " + current_date + ", disponible à l'adresse suivante : " + self.link)

