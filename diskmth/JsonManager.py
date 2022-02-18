"""
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
"""