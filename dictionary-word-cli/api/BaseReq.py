import requests
import json
import uuid
import datetime

HEADERS = {
    'x-rapidapi-key': "d75c6c9665msh5467048e1cfda96p1b5a75jsnf2d0f09ae1bd",
    'x-rapidapi-host': "google-translate20.p.rapidapi.com"
}

class BaseReq:
    """
    This class is responsible for a comunication with our server or API.
    """
    def __init__(self, url, file):
        self.url = url
        self.file = file

    def get_word(self, text, target='ru'):
        "gets a data from the API endpoint and return in an appropriate interface"
        querystring = {'text': text, 'tl': target}

        print('requesting the word')
        response = requests.request("GET", self.url + '/translate', headers = HEADERS, params = querystring)

        print('parsing the result')
        return self.parse_word(response, text)

    def parse_word(self, data, text):
        "parses and return data"

        parsed = json.loads(data.text)
        data = parsed['data']
        translation = data['translation']

        return {'word': text, 
                'translation': translation, 
                "id": str(uuid.uuid4()), 
                "last_updated": str(datetime.datetime.now())
               }