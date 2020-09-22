import requests
import re

class curl:
    def __init__(self, adress):
        self.adress: str = adress
        self.timeout: int = 3000


    def get(self):
        req: str = requests.get(self.adress)
        return req.text

    def filter(self):
        titleReg: str = '(?<=<title>)(.*)(?=</title>)'
        title: str = re.search(titleReg, self.get())
        return title
