from tkinter import messagebox
import Utils
import json
import os

available_json = {}
cancel_generate = False
global json_items_to_generate
global json_blocks_to_generate
global json_blockstates_to_generate
json_items_path = Utils.get_resources_path("resources\\json\\models\\item\\")
json_blocks_path = Utils.get_resources_path("resources\\json\\models\\block\\")
json_blockstates_path = Utils.get_resources_path("resources\\json\\blockstates\\")


def load_jsons():
    global available_json

    try:
        with open(Utils.get_resources_path("resources\\json\\available_json.json"), "r", encoding="utf-8") as json_file:
            available_json = json.load(json_file)
            json_file.close()
    except json.decoder.JSONDecodeError:
        pass


def get_json_list():
    json_list = []
    for key, value in available_json.items():
        json_list.append(key)
    return json_list


def create_json_lists_to_generate(json_list, material_name):
    global json_items_to_generate
    global json_blocks_to_generate
    global json_blockstates_to_generate

    json_items_to_generate = []
    json_blocks_to_generate = []
    json_blockstates_to_generate = []

    for json_file in json_list:
        for key_1, value_1 in available_json.items():
            if json_file == key_1:
                for i in value_1:
                    for key_2, value_2 in i.items():
                        if key_2 == "item_model":
                            for json_item in value_2:
                                json_items_to_generate.append(json_item)
                        elif key_2 == "block_model":
                            for json_block in value_2:
                                json_blocks_to_generate.append(json_block)
                        elif key_2 == "blockstate":
                            for json_blockstate in value_2:
                                json_blockstates_to_generate.append(json_blockstate)


def create_json_files(modid, material_name, output_folder_path):
    global cancel_generate
    json_item_missing = []
    json_block_missing = []
    json_blockstate_missing = []

    for json_file in json_items_to_generate:
        try:
            original_json_content = {}
            with open(Utils.get_resources_path("resources\\json\\models\\item\\" + json_file + ".json"),
                      encoding="utf-8") as original_json_file:
                original_json_content = json.load(original_json_file)
                original_json_file.close()

            with open(output_folder_path + "\\Json maker\\models\\item\\" + json_file.replace("+++",
                                                                                              material_name) + ".json",
                      "w+", encoding="utf-8") as new_json_file:
                json.dump(original_json_content, new_json_file, indent=4)
                new_json_file.seek(0)
                file_content = new_json_file.read().replace("+++", material_name).replace("---", modid)
                new_json_file.truncate(0)
                new_json_file.seek(0)
                new_json_file.write(file_content)
        except FileNotFoundError:
            cancel_generate = True
            json_item_missing.append(json_file)

    for json_file in json_blocks_to_generate:
        try:
            original_json_content = {}
            with open(Utils.get_resources_path("resources\\json\\models\\block\\" + json_file + ".json"),
                      encoding="utf-8") as original_json_file:
                original_json_content = json.load(original_json_file)
                original_json_file.close()

            with open(output_folder_path + "\\Json maker\\models\\block\\" + json_file.replace("+++",
                                                                                               material_name) + ".json",
                      "w+", encoding="utf-8") as new_json_file:
                json.dump(original_json_content, new_json_file, indent=4)
                new_json_file.seek(0)
                file_content = new_json_file.read().replace("+++", material_name).replace("---", modid)
                new_json_file.truncate(0)
                new_json_file.seek(0)
                new_json_file.write(file_content)
        except FileNotFoundError:
            cancel_generate = True
            json_block_missing.append(json_file)

    for json_file in json_blockstates_to_generate:
        try:
            original_json_content = {}
            with open(Utils.get_resources_path("resources\\json\\blockstates\\" + json_file + ".json"),
                      encoding="utf-8") as original_json_file:
                original_json_content = json.load(original_json_file)
                original_json_file.close()

            with open(output_folder_path + "\\Json maker\\blockstates\\" + json_file.replace("+++",
                                                                                             material_name) + ".json",
                      "w+", encoding="utf-8") as new_json_file:
                json.dump(original_json_content, new_json_file, indent=4)
                new_json_file.seek(0)
                file_content = new_json_file.read().replace("+++", material_name).replace("---", modid)
                new_json_file.truncate(0)
                new_json_file.seek(0)
                new_json_file.write(file_content)
        except FileNotFoundError:
            cancel_generate = True
            json_blockstate_missing.append(json_file)

    if cancel_generate:
        messagebox.showerror(Utils.get_translations("other", "error_GUI_title"),
                             Utils.get_translations("labels", "label_json_missing_error_messagebox") +
                             "\n      " + Utils.get_translations("labels", "label_json_category_item") +
                             str(json_item_missing) +
                             "\n      " + Utils.get_translations("labels", "label_json_category_block") +
                             str(json_block_missing) +
                             "\n      " + Utils.get_translations("labels", "label_json_category_blockstate") +
                             str(json_blockstate_missing))
