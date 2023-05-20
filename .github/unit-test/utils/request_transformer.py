from stores.function_store import Function
import re

class RequestTransformer:
    def __init__(self) -> None:
        pass

    def get_code_string_from_functions(self, functions: Function):
        code_string = ""
        for function in functions:
            code_string += function.code
            code_string += "\n"
        return code_string

    def extract_code_block(self, string):
        pattern = r"```([\s\S]*)```"  # Matches the text between ``` delimiters
        match = re.search(pattern, string)
        
        if match:
            return match.group(1)
        else:
            return None