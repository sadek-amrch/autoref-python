import requests
import re

class curl:
    def __init__(self):
        self.timeout: int = 3000


    def get(self, adress):
        req: str = requests.get(adress)
        return req.text

    def filter(self, adress):
        titleReg: str = '(?<=<title>)(.*)(?=</title>)'
        title: str = re.search(titleReg, self.get(adress))
        return title
