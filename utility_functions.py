from os import name, system
import json


def clear_screen() -> None:
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')


def init_json_file(file_path: str) -> None:
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            if not content:
                json.dump([], file)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            json.dump([], file)
