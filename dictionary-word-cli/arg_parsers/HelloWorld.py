import cmd

class HelloWorld(cmd.Cmd):
    "Base app controller"

    intro = 'Welcome to the dictionary shell. Type help or ? to list commands or quit to quit the programm.\n'
    prompt = 'type a command '

    def __init__(self, req, saver):
        super().__init__()
        self.req = req
        self.saver = saver

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_quit(self, line):
        "quits from the app"
        return True
    
    def do_init_word_db(self, name):
        "creates the words database"

        if not name:
            print('please, provide a database name')
            return

        print("starting to create a database")
        data = {
            'words': []
        }
        self.saver.create_db(data, name)
    
    def do_save(self, word):
        "saves a word to the db"

        print('starting to save a word')
        resp = self.req.get_word(word)
        print('resp', resp)
        self.saver.save_file(resp, 'words')

        print('the world was saved in the db')
    
    def do_delete_db(self, name):
        "deletes a db by a db's name"

        print("starting to delete a database")
        self.saver.drop_db(name)

    def postloop(self):
        "this function fires before finishing the app"
        print('bye!')