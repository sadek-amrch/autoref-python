import requests
import re
import json
from datetime import datetime

headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class curl:
    def get(self, address: str):
        try:
            req = requests.get(address, headers=headers)
        except:
            return 0

        if (req.status_code == 200):
            req.elapsed.total_seconds()
            return req.text
        else:
            return 0;

    def filterTitle(self, address):
        titleReg: str = '<title[^>]*>([^<]*)<\/title>'

        try:
            title = re.search(titleReg, self.get(address))
        except:
            return 0

        if (title.group(0)[0] == '<'):
            return title.group(1)
        else:
            return title.group(0)

    def filterJson(self, address):

        output: dict = {}
        jsonReg: str = '(?<=<script type="application\/ld\+json">)(.*?)(?=<\/script)'

        try:
            jsonRaw = re.search(jsonReg, self.get(address))
            jsonParsed = json.loads(jsonRaw.group(0))
        except:
            return 0

        if ("author" in jsonParsed):
            author = jsonParsed["author"][0]["name"]
            #Last name
            output.update({"LastName": author.split(" ",1)[1]})
            #First name
            output.update({"FirstName": author.split(" ",1)[0]})

        if ("copyrightYear" in jsonParsed):
            output.update({"Year": jsonParsed["copyrightYear"]})

        if ("headline" in jsonParsed):
            output.update({"Title": jsonParsed["headline"]})

        if ("datePublished" in jsonParsed):
            publishDate = jsonParsed["datePublished"][0:9]
            publishDate = datetime.strptime(publishDate, "%d-%m-%Y").strftime("%Y.%m.%d")
            output.update({"DatePublished": publishDate})

        if ("dateModified" in jsonParsed):
            modifyDate = jsonParsed["dateModified"][0:9]
            modifyDate = datetime.strptime(modifyDate, "%d-%m-%Y").strftime("%Y.%m.%d")
            output.update({"DateModified": modifyDate})

        if (len(output) >= 1 and "Title" in output):
            return output
        else:
            return 0
