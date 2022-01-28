import os
import sys
import json

global translation_dictionary


def get_resources_path(relative_path):
    try:
        file_name = relative_path.split("\\")[-1]
        base_path = sys._MEIPASS
        return os.path.join(base_path + "\\" + file_name)
    except Exception:
        base_path = os.path.realpath(__file__)
        base_path = base_path.replace("\\Utils.py", "")
        return os.path.join(base_path + "\\" + relative_path)


def load_translations():
    global translation_dictionary
    translation_dictionary = []

    try:
        for files in os.listdir(get_resources_path("resources\\lang\\")):
            if files.lower().endswith(tuple(".json")):
                with open(get_resources_path("resources\\lang\\") + files, "r", encoding='utf-8') as file:
                    data = json.load(file)
                    translation_dictionary.append(data)

    except json.decoder.JSONDecodeError:
        pass


def get_translations_dict():
    global translation_dictionary
    return translation_dictionary
