import json

class jsonParser:
    def __init__(self, data):
        self.data: str = data

    def parse (self):
        return json.load(self.data)
