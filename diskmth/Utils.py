from tkinter import messagebox
import os
import sys
import json
import shutil

global translation_list
active_language = "english"  # default on start
global json_items
global json_blocks
global json_blockstates
global json_items_to_generate
global json_blocks_to_generate
global json_blockstates_to_generate


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
            if str(files.lower()).endswith(".lang"):
                with open(get_resources_path("resources\\lang\\") + files, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    translation_list.append(data)

    except json.decoder.JSONDecodeError:
        pass


def get_translations(translation_group, translation_key):
    global translation_list
    global active_language

    for languages in translation_list:
        try:
            if languages["language"] == active_language:
                try:
                    return languages[translation_group][0][translation_key]
                except KeyError:
                    return "Error"
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
        if str(file.lower()).endswith(".json"):
            try:
                with open(get_resources_path("resources\\json\\models\\item\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_items[file] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(get_resources_path("resources\\json\\models\\block\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(get_resources_path("resources\\json\\models\\block\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_blocks[file] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(get_resources_path("resources\\json\\blockstates\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(get_resources_path("resources\\json\\blockstates\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_blockstates[file] = json.load(json_file)

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


def make_output_dir(output_folder_path):
    os.chdir(output_folder_path)

    try:
        os.mkdir("Json maker")
    except FileExistsError:
        shutil.rmtree("Json maker")
        os.mkdir("Json maker")

    os.chdir("Json maker")

    os.mkdir("blockstates")
    os.mkdir("models")

    os.chdir("models")

    os.mkdir("block")
    os.mkdir("item")


def create_json_list_to_generate(json_list, material_name):
    global json_items
    global json_blocks
    global json_blockstates
    global json_items_to_generate
    global json_blocks_to_generate
    global json_blockstates_to_generate

    json_items_to_generate = []
    json_blocks_to_generate = []
    json_blockstates_to_generate = []

    for json_files in json_list:
        if json_files in json_blocks and json_files not in json_blockstates:

            if messagebox.askyesno(get_translations("other", "warning_GUI_title"),
                                   get_translations("other", "missing_model_warning_messagebox")
                                   + json_files.replace("+++", material_name), icon="warning"):
                json_list.remove(json_files)

            else:
                json_items_to_generate = []
                json_blocks_to_generate = []
                json_blockstates_to_generate = []
                break

        elif json_files not in json_blocks and json_files in json_blockstates:

            if messagebox.askyesno(get_translations("other", "warning_GUI_title"),
                                   get_translations("other", "missing_blockstate_warning_messagebox")
                                   + json_files.replace("+++", material_name), icon="warning"):
                json_list.remove(json_files)

            else:
                json_items_to_generate = []
                json_blocks_to_generate = []
                json_blockstates_to_generate = []
                break

        elif json_files in json_blocks and json_files in json_blockstates:
            json_items_to_generate.append(json_files)
            json_blocks_to_generate.append(json_files)
            json_blockstates_to_generate.append(json_files)

        elif json_files in json_items:
            json_items_to_generate.append(json_files)


def create_json(output_folder_path, modid, material_name):
    global json_items
    global json_blocks
    global json_blockstates
    global json_items_to_generate
    global json_blocks_to_generate
    global json_blockstates_to_generate

    items_path = ""
    blocks_path = output_folder_path + "\\Json maker\\models\\block\\"
    blockstates_path = output_folder_path + "\\Json maker\\blockstates\\"

    index = 0
    for json_files in json_items_to_generate:

        print(json_items[json_items_to_generate[index]])


        with open(output_folder_path + "\\Json maker\\models\\item\\" + json_files.replace("+++", material_name), "w", encoding="utf-8") as json_file:
            json.dump(json_items[json_items_to_generate[index]], json_file)
        index += 1


def zip_output_dir(output_folder_path):
    os.chdir(output_folder_path)
    shutil.make_archive("Json maker", "zip", "Json maker")
    shutil.rmtree("Json maker")
