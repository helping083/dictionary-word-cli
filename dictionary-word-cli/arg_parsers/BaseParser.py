import argparse

class BaseParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-s", help="show notes", action="store_true")
        self.parser.add_argument('-v', help="search for the world", dest='word', type=str, nargs='*')
        self.parser.add_argument('-save', help='search for a word and save', type=str, dest='save')
        self.parser.add_argument('-t', help='test exit', type=str, nargs=1)
        self.parser.add_argument('-create', help='create db file', type=str, nargs=1)

    @property
    def x(self):
        args = self.parser.parse_args()
        return args

    def create_sub_parser(self):
        pass

    def test_exit(self):
        print('works')