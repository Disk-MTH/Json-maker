from tkinter import messagebox
import Utils
import json
import os

json_items = {}
json_blocks = {}
json_blockstates = {}
json_specials = {}
global json_items_to_generate
global json_blocks_to_generate
global json_blockstates_to_generate
global json_specials_to_generate


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

    for file in os.listdir(Utils.get_resources_path("resources\\json\\models\\item\\special\\")):
        if str(file.lower()).endswith(".json"):
            try:
                with open(Utils.get_resources_path("resources\\json\\models\\item\\special\\") + file, "r",
                          encoding="utf-8") as json_file:
                    json_specials[file.replace(".json", "")] = json.load(json_file)

            except json.decoder.JSONDecodeError:
                pass


def get_json_list(json_list):
    if json_list == "items":
        return json_items
    elif json_list == "blocks":
        return json_blocks
    if json_list == "blockstates":
        return json_blockstates
    if json_list == "specials":
        return json_specials


def create_json_lists_to_generate(json_list, material_name):
    global json_items_to_generate
    global json_blocks_to_generate
    global json_blockstates_to_generate
    global json_specials_to_generate

    json_items_to_generate = []
    json_blocks_to_generate = []
    json_blockstates_to_generate = []
    json_specials_to_generate = []

    for json_file in json_list:
        if not json_file.replace("+++", "") == "":
            item = json_file.replace("+++", "")
        else:
            item = json_file

        for key, value in json_items.items():
            if item in key and not item == "+++":
                json_items_to_generate.append(key)
            elif item == "+++":
                json_items_to_generate.append("+++")
                break

        for key, value in json_blocks.items():
            if item in key and not item == "+++":
                json_blocks_to_generate.append(key)

        for key, value in json_blockstates.items():
            if item in key and not item == "+++":
                json_blockstates_to_generate.append(key)

        for key, value in json_specials.items():
            if item in key and not item == "+++":
                json_specials_to_generate.append(key)


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

    for json_file in json_specials_to_generate:
        with open(output_folder_path + "\\Json maker\\models\\item\\" + json_file.replace("+++", material_name)
                  + ".json", "w+", encoding="utf-8") as file:
            json.dump(json_specials[json_file], file, indent=4)
            file.seek(0)
            file_content = file.read().replace("+++", material_name).replace("---", modid)
            file.truncate(0)
            file.seek(0)
            file.write(file_content)
