import os
import openai
from enums.enums import OpenAiRoles, OpenAiModels


class OpenAI:
    def __init__(self) -> None:
        self.history = []
        openai.api_key = os.getenv("OPENAI_API_KEY")
        initial_prompt = self.get_initial_prompt()
        self.history = [initial_prompt]

    def get_initial_prompt(self):
        return dict(
            {
                "role": OpenAiRoles.SYSTEM,
                "content": """Hello, write tests for the function below. Also call the tests after defining them in a function. Dont add the string python after the backticks""",
                # "content": """I will send you code. write unit tests for the same. Write a minimum of 5 tests and a maximum of 7 tests for the function. Do not respond with any other text apart from the answer, assume that the function is already defined. I don't want you to explain the tests written. Do not add any text before or after the code. It should add tabs for proper formatting as well. Do not write any explanations, just send me code as a response that I can use as unit tests in the format I have mentioned below.Here is a sample input/ output for a function.input:def add(a, b):return a + b. output: "def test_add_positive_numbers():\n\tassert add(2, 3) == 5\n\n\ndef test_add_negative_numbers():\n\tassert add(-2, -3) == -5\n\n\ndef test_add_zero():\n\tassert add(0, 0) == 0\n\n\ntest_add_positive_numbers()\ntest_add_negative_numbers()\ntest_add_zero()" Do not write any explanations, just send me  code as a response that I can use as unit tests in the format I have mentioned above""",
            }
        )

    def chat(self, text):        
        print("Making OPEN AI call")
        response = openai.ChatCompletion.create(
            model=OpenAiModels.TURBO_3_5,
            temperature=0.2,
            messages=[
                *self.history,
                {"role": OpenAiRoles.USER, "content": text},
            ],
        )
        print("Response recived \n")
        return response
    

    def append_to_history(self, question, answer):
        self.history.append({"role": OpenAiRoles.USER, "content": question})
        self.history.append(
            {
                "role": OpenAiRoles.ASSISTANT,
                "content": answer,
            }
        )
