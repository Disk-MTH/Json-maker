from tkinter import messagebox
import Utils
import json
import os


json_items = {}
json_blocks = {}
json_blockstates = {}
global json_items_to_generate
global json_blocks_to_generate
global json_blockstates_to_generate


def load_jsons():
    global json_items
    global json_blocks
    global json_blockstates

    for file in os.listdir(Utils.get_resources_path("resources\\json\\models\\item\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(Utils.get_resources_path("resources\\json\\models\\item\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_items[file.replace(".json", "")] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(Utils.get_resources_path("resources\\json\\models\\block\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(Utils.get_resources_path("resources\\json\\models\\block\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_blocks[file.replace(".json", "")] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass

    for file in os.listdir(Utils.get_resources_path("resources\\json\\blockstates\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(Utils.get_resources_path("resources\\json\\blockstates\\") + file, "r", encoding="utf-8") \
                        as json_file:
                    json_blockstates[file.replace(".json", "")] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass


def get_json_list(json_list):
    if json_list == "items":
        return json_items
    elif json_list == "blocks":
        return json_blocks
    if json_list == "blockstates":
        return json_blockstates


def create_json_lists_to_generate(json_list, material_name):
    global json_items_to_generate
    global json_blocks_to_generate
    global json_blockstates_to_generate

    json_items_to_generate = []
    json_blocks_to_generate = []
    json_blockstates_to_generate = []

    already_cancel = False

    for json_file in json_list:
        if json_file in json_blocks and json_file not in json_blockstates and not already_cancel:
            if not messagebox.askyesno(Utils.get_translations("other", "warning_GUI_title"),
                                       Utils.get_translations("labels", "label_missing_blockstate_warning_messagebox")
                                       + json_file.replace("+++", material_name), icon="warning"):
                already_cancel = True
                checked_json_list = []
        elif json_file not in json_blocks and json_file in json_blockstates and not already_cancel:
            if not messagebox.askyesno(Utils.get_translations("other", "warning_GUI_title"),
                                       Utils.get_translations("labels", "label_missing_model_warning_messagebox")
                                       + json_file.replace("+++", material_name), icon="warning"):
                already_cancel = True
                checked_json_list = []
        elif json_file in json_blocks and json_file in json_blockstates:
            json_items_to_generate.append(json_file)
            json_blocks_to_generate.append(json_file)
            json_blockstates_to_generate.append(json_file)

        elif json_file in json_items and json_file not in json_blocks and json_file not in json_blockstates:
            json_items_to_generate.append(json_file)
    return already_cancel


def create_json_files(modid, material_name, output_folder_path):
    for json_file in json_items_to_generate:
        with open(output_folder_path + "\\Json maker\\models\\item\\" + json_file.replace("+++", material_name) +
                  ".json", "w+", encoding="utf-8") as file:
            json.dump(json_items[json_file], file, indent=4)
            file.seek(0)
            file_content = file.read().replace("+++", material_name).replace("---", modid)
            file.truncate(0)
            file.seek(0)
            file.write(file_content)

    for json_file in json_blocks_to_generate:
        with open(output_folder_path + "\\Json maker\\models\\block\\" + json_file.replace("+++", material_name) +
                  ".json", "w+", encoding="utf-8") as file:
            json.dump(json_blocks[json_file], file, indent=4)
            file.seek(0)
            file_content = file.read().replace("+++", material_name).replace("---", modid)
            file.truncate(0)
            file.seek(0)
            file.write(file_content)
    for json_file in json_blockstates_to_generate:
        with open(output_folder_path + "\\Json maker\\blockstates\\" + json_file.replace("+++", material_name) +
                  ".json", "w+", encoding="utf-8") as file:
            json.dump(json_blockstates[json_file], file, indent=4)
            file.seek(0)
            file_content = file.read().replace("+++", material_name).replace("---", modid)
            file.truncate(0)
            file.seek(0)
            file.write(file_content)
