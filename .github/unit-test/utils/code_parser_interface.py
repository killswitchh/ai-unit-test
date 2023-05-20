from enums.enums import Parser
from utils.red_baron_parser import RedBaronParser

class CodeParser:
    def __init__(self, file_name):
        parser = self.find_parser(file_name)
        if parser == Parser.REDBARON:
            self.parser = RedBaronParser(file_name)
        else:
            self.parser = None

    def find_functions(self):
        if self.parser is not None:
            return self.parser.find_functions()

    def find_parser(self, file_name):
        if (file_name.endswith(".py")):
            return Parser.REDBARON