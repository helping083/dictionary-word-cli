import datetime
import json
import datetime
import os

class FileSaver:
    def __init__(self, file_location) -> None:
        self.file_location = file_location
    
    def save_file(self):
        pass

    def create_db(self, name):
        if os.path.exists(name):
            print('db with this name is already exists')
            return
        now = str(datetime.datetime.now())
        with open(name, 'w') as o:
            now = str(datetime.datetime.now())
            data = {
                "notes": [],
                "last_updated": now
            }
            json.dump(data, o)
            print('Databse created. You are ready to add notes.')

    def check_word(self):
        pass