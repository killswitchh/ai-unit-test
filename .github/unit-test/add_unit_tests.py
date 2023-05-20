# Import necessary libraries
import sys

from utils.file_utils import FileUtils
from utils.code_parser_interface import CodeParser
from stores.function_store import FunctionStore
from core.open_ai import OpenAI as AI
from utils.request_transformer import RequestTransformer


def generate_ai_unit_tests(file_path):
    parser = CodeParser(file_path)
    store = FunctionStore()
    transformer = RequestTransformer()
    open_ai = AI()
    functions = parser.find_functions()
    store.add_function_group(functions)
    function_names = store.function_names
    ai_response = open_ai.chat(transformer.get_code_string_from_functions(functions))
    content = ai_response.choices[0].message.content
    unit_test_content = transformer.extract_code_block(content)
    path = FileUtils.create_directory("./ai-tests")
    filename = FileUtils.get_file_name(file_path)
    filename_without_extension = filename.split(".")[0]

    # create test files
    with open(FileUtils.convert_to_test("ai-tests/" + filename), "w", encoding="utf-8") as f:
        functions = ", ".join(function_names)
        f.write(f"import sys\n")
        f.write(f"import os\n")
        f.write(f"sys.path.insert(0, os.getcwd())\n")
        f.write(f"from {filename_without_extension} import {functions}\n")
        f.write(unit_test_content)


# Run the function if this script is called directly
if __name__ == "__main__":
    # filePath = sys.argv[1]
    filePath = "addition.py"
    generate_ai_unit_tests(filePath)
