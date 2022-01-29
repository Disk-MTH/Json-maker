import os
import sys
import json

global translation_list
global json_items
global json_blocks
global json_blockstates
active_language = "english"  # default on start


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
    global translation_list
    translation_list = []

    try:
        for files in os.listdir(get_resources_path("resources\\lang\\")):
            if files.lower().endswith(tuple(".json")):
                with open(get_resources_path("resources\\lang\\") + files, "r", encoding='utf-8') as file:
                    data = json.load(file)
                    translation_list.append(data)

    except json.decoder.JSONDecodeError:
        pass


def get_translations(translation_group, translation_key):
    global translation_list
    global active_language

    for languages in translation_list:
        if languages["language"] == active_language:
            try:
                return languages[translation_group][0][translation_key]
            except KeyError:
                return "Error"


def get_languages_list():
    global active_language
    global translation_list
    language_list = []

    for languages in translation_list:
        language_list.append(languages["language"])

    return language_list


def set_active_language(new_language):
    global active_language
    active_language = new_language


def load_json():
    global json_items
    global json_blocks
    global json_blockstates

    json_items = {}
    json_blocks = {}
    json_blockstates = {}

    for file in os.listdir(get_resources_path("resources\\json\\models\\item\\")):
        if file.lower().endswith(tuple(".json")):
            try:
                with open(get_resources_path("resources\\json\\models\\item\\") + file, "r",
                          encoding='utf-8') as json_file:
                    json_items[file.replace("+++", get_translations("other", "json_material"))] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(get_resources_path("resources\\json\\models\\block\\")):
        if file.lower().endswith(tuple(".json")):
            try:
                with open(get_resources_path("resources\\json\\models\\block\\") + file, "r",
                          encoding='utf-8') as json_file:
                    json_blocks[file.replace("+++", get_translations("other", "json_material"))] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(get_resources_path("resources\\json\\blockstates\\")):
        if file.lower().endswith(tuple(".json")):
            try:
                with open(get_resources_path("resources\\json\\blockstates\\") + file, "r",
                          encoding='utf-8') as json_file:
                    json_blockstates[file.replace("+++", get_translations("other", "json_material"))] = \
                        json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass


def get_json_list(json_list):
    global json_items
    global json_blocks
    global json_blockstates

    if json_list == "items":
        return json_items
    elif json_list == "blocks":
        return json_blocks
    if json_list == "blockstates":
        return json_blockstates
















    """
    for root, dirs, files in os.walk(get_resources_path("resources\\json\\")):
        for directory in dirs:
            dir_path = get_resources_path("resources") + os.path.join(root, directory).split("resources")[1] + "\\"
            for file in os.listdir(dir_path):
                if file.lower().endswith(tuple(".json")):
                    with open(dir_path + file, "r", encoding='utf-8') as json_file:
                        json_list[file] = json.load(json_file)
                        print(json_list)
    """
