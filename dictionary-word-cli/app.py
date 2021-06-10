from api import BaseReq
from saver import FileSaver
from arg_parsers import HelloWorld

#constants
URL = "https://google-translate20.p.rapidapi.com"
FILE = './dictionary.json'
FILE_FORMAT = '.json'
FOLDER = './data/'

#base classes
req = BaseReq(URL, FILE)
json_saver = FileSaver(FILE, FILE_FORMAT, FOLDER)
base_parser = HelloWorld(req, json_saver)

def main():
   base_parser.cmdloop()