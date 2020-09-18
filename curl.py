import requests

class curl:
    def __init__(self, adress):
        self.adress: str = adress
        self.timeout: int = 3000


    def get(self):
        req = requests.get(self.adress)
        return req.text;

    def filter(self):
        
        return 0