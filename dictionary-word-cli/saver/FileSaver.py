import datetime
import json
import os

class FileSaver:
    """
    This class is responsible for CRUD operations with databases.
    The imitations of databases is json files located in the data folder.
    """
    def __init__(self, file_location, file_format, folder_name) -> None:
        self.file_location = file_location
        self.file_format = file_format
        self.folder_name = folder_name

    def save_file(self, word, db_name):
        "saves a word to the db"
        file_name = self.folder_name + db_name + self.file_format

        with open(file_name, 'r', encoding='utf8') as f:
            data = json.load(f)
            now = str(datetime.datetime.now())

            data['words'].append(word)
            data["last_updated"] = now

            self.write_file(file_name, data)

    def write_file(self, file_name, data):
            try:
                with open(file_name, "w", encoding='utf8') as o:
                  json.dump(data, o, ensure_ascii=False, sort_keys=True, indent=4)
            except IOError as e:
                  print('oops!', e)
    
    def create_db(self, data, name):
        "creates a database name if no exists"

        print('checking databases...')
        db_exists = self.check_db_exists(name)
        if not db_exists:
            print('database is creating...')
            now = str(datetime.datetime.now())
            with open(self.folder_name + name + self.file_format, 'w') as o:
                now = str(datetime.datetime.now())
                data["last_updated"] = now
                json.dump(data, o)
                print('Database is created. You are ready to add notes.')

    def check_db_exists(self, db_name):
        'checks if db exists'

        print("checking a file for existing")
        if os.path.exists(self.folder_name + db_name + self.file_format):
            print('this name is already exists')
            return True
        return False
    
    def drop_db(self, db_name):
        "deletes a db"

        file_name = self.folder_name + db_name + self.file_format
        if os.path.exists(file_name):
            os.remove(file_name)
            print('db was deleted')
        else:
            print("The file does not exist")

    def check_duplicate_word(self, word, db_name):
        "this method checks if the world exists in the database"

        file_name = self.folder_name + db_name + self.file_format

        with open(file_name, 'r', encoding='utf8') as f:
            data = json.load(f)
            for item in data['words']:
                original_word = item['word']
                if original_word == word:
                    print('the world {} exists in db'.format(original_word),'\n')
                    return True
        return False