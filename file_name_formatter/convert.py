"""
'first_file' -> 'First file'
'first_file' -> 'first file'
'first-file' -> 'First file'
'firstFile' -> 'First file'
'desktop/first_file' -> 'First file'
"""

import os


class Convert:
    def __init__(self):
        pass

    def convert_input(self):
        clear = lambda: os.system("cls")

        controls: str = input(
            "1. Convert from 'first_file' -> 'First file'\n2. Convert from 'first_file' -> 'first file'\n3. Convert from 'first-file' -> 'First file'\n4. Convert from 'firstFile' -> 'First file'\n5. Convert from 'desktop/first_file' -> 'First file'\n"
        ).strip()
        clear()

        if controls == "1":
            return remove_underscore_capitalize()
        elif controls == "2":
            return remove_underscore_lowercase()
        elif controls == "3":
            return remove_hyphen_capitalize()
        elif controls == "4":
            return insert_space()
        elif controls == "5":
            return remove_computer_directory()
        else:
            raise ValueError("Invalid format")


def remove_underscore_capitalize():
    file_name: str = input("Enter file name: ").strip()

    if file_name == "":
        raise ValueError("Empty inputs not allowed")

    if not file_name[len(file_name) - 1].isalnum() or not file_name[0].isalnum():
        raise ValueError("Invalid input format")

    result_string: str = file_name.replace("_", " ").capitalize()
    return result_string


def remove_underscore_lowercase():
    file_name: str = input("Enter file name: ").strip()

    if file_name == "":
        raise ValueError("Empty inputs not allowed")

    if not file_name[len(file_name) - 1].isalnum() or not file_name[0].isalnum():
        raise ValueError("Invalid input format")

    result_string: str = file_name.replace("_", " ")
    return result_string


def remove_hyphen_capitalize():
    file_name: str = input("Enter file name: ").strip()

    if file_name == "":
        raise ValueError("Empty inputs not allowed")

    if not file_name[len(file_name) - 1].isalnum() or not file_name[0].isalnum():
        raise ValueError("Invalid input format")

    if "-" not in file_name:
        raise ValueError("Invalid input format")
    else:
        result_string: str = file_name.replace("-", " ").capitalize()
        return result_string


def insert_space():
    file_name: str = input("Enter file name: ").strip()

    if file_name == "":
        raise ValueError("Empty inputs not allowed")

    if not file_name[len(file_name) - 1].isalnum() or not file_name[0].isalnum():
        raise ValueError("Invalid input format")

    i = 0

    for i in range(len(file_name)):
        if file_name[i].isupper():
            break
        i += 1

    split_file_name: list[str] = [file_name[:i], file_name[i:]]
    return " ".join(split_file_name).capitalize()


def remove_computer_directory():
    file_name: str = input("Enter file name: ").strip()

    if file_name == "":
        raise ValueError("Empty inputs not allowed")

    i = 0

    for i in range(len(file_name)):
        if file_name[i] == "/":
            break
        i += 1

    new_file_name = [file_name[i + 1 :]]

    result_string = "".join(new_file_name)
    return result_string.replace("_", " ").capitalize()
