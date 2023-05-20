from typing import List


class Function:
    def __init__(self, name = "", code = "") -> None:
        self.name = name
        self.code = code

class FunctionStore:
    def __init__(self) -> None:
        self.functions = []
        self.function_names = []

    def add_item(self, function):
        self.functions.append(function)
        self.function_names.append(function.name)

    def add_function_group(self, functions: List[Function]):
        for function in functions:
            self.add_item(function)
