import os
import sys
import shutil
import tradlib

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


def get_translations(translation_group, translation_key):
    try:
        return tradlib.get_translation(active_language, [translation_group, 0, translation_key])
    except KeyError:
        return "Error"


def set_active_language(selected_language):
    global active_language
    active_language = selected_language


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


def zip_output_dir(output_folder_path):
    os.chdir(output_folder_path)
    shutil.make_archive("Json maker", "zip", "Json maker")
    shutil.rmtree("Json maker")
