from api import BaseReq
from saver import FileSaver
from arg_parsers import BaseController
from utils import create_data_folder

#constants
URL = "https://google-translate20.p.rapidapi.com"
FILE = './dictionary.json'
FILE_FORMAT = '.json'
FOLDER = './data/'

#base classes
api = BaseReq(URL, FILE)
file_saver = FileSaver(FILE, FILE_FORMAT, FOLDER)
controller = BaseController(api, file_saver)

def main():
   create_data_folder()
   controller.cmdloop()