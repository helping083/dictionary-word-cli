from api import BaseReq
from arg_parsers import BaseParser
from saver import FileSaver

URL = "https://google-translate20.p.rapidapi.com"
FILE = './dictionary.json'

parser = BaseParser()
req = BaseReq(URL, FILE)
saver = FileSaver(FILE)

argum = parser.x

def main():
   if argum.create:
      db_name = argum.create[0]
      saver.create_db(db_name)