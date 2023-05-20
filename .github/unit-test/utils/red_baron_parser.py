from redbaron import RedBaron
from stores.function_store import Function

class RedBaronParser:
    def __init__(self, file_name):
        self.file_node = self.load_file(file_name)

    def load_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            content = RedBaron(f.read())
        return content

    def find_functions(self):
        functions = []
        for node in self.file_node.find_all("def"):
            functions.append(Function(node.name, node.dumps())) 
        return functions