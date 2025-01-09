"""
'first_file' -> 'First file'
'first_file' -> 'first file'
'first-file' -> 'First file'
'firstFile' -> 'First file'
'desktop/first_file' -> 'First file'
"""

import re


class StringFormatter:
    def __init__(self):
        pass

    def format_string(self, input_string: str) -> list:
        stripped_input: str = input_string.strip()
        output: list[str] = []

        if re.match(r"^[a-z]+([A-Z][a-z]*)*$", stripped_input):
            result_string = ""

            for i in range(len(stripped_input)):
                if stripped_input[i].isupper():
                    break

            stripped_input: list[str] = [stripped_input[:i], stripped_input[i:]]
            result_string += " ".join(stripped_input).capitalize()
            output.append(result_string)

        elif re.match(r"^[a-zA-Z0-9_]+$", stripped_input):
            result_string1: str = stripped_input.replace("_", " ").capitalize()
            result_string2: str = stripped_input.replace("_", " ")
            output.extend([result_string1, result_string2])

        elif re.match(r"^[a-zA-Z0-9-]+$", stripped_input):
            result_string: str = stripped_input.replace("-", " ").capitalize()
            output.append(result_string)

        elif re.match(r"^([a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)$", stripped_input):
            parts = stripped_input.split("/")
            result_string = parts[1].replace("_", " ").capitalize()
            output.append(result_string)

        if not output:
            output.append(input_string)

        return output
