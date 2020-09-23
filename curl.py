import requests
import re

headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
class curl:
    def __init__(self):
        self.timeout: int = 3000


    def get(self, adress: str):
        req = requests.get(adress, headers=headers)

        if (req.status_code == 200):
            return req.text
        else:
            return 0;

    def filter(self, adress):
        titleReg: str = '<title[^>]*>([^<]*)<\/title>'

        title: str = re.search(titleReg, self.get(adress))

        if (title.group(0)[0] == '<'):
            return title.group(1)
        else:
            return title.group(0)