import requests
import json
headers = {
    'x-rapidapi-key': "d75c6c9665msh5467048e1cfda96p1b5a75jsnf2d0f09ae1bd",
    'x-rapidapi-host': "google-translate20.p.rapidapi.com"
}

class BaseReq:
    def __init__(self, url, file):
        self.url = url
        self.file = file

    def get_word(self, text, target):
        querystring = {'text': text, 'tl': target}
        print(querystring)
        response = requests.request("GET", self.url + '/translate', headers = headers, params = querystring)
        self.parse_word(response)

    def parse_word(self, data):
        parsed = json.loads(data.text)
        data = parsed['data']
        translation = data['translation']
        print(translation)