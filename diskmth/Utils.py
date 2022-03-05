from tkinter import messagebox
import tradlib
import shutil
import sys
import os

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


def check_empty_entry(entries_to_check):
    for key, value in entries_to_check.items():
        if (key == "entry_modid" and value == "") or (key == "entry_material_name" and value == "") or \
                (key == "listbox_json_list" and not value):
            messagebox.showerror(get_translations("other", "error_GUI_title"),
                                 get_translations("labels", "label_blank_error_messagebox"))
            break

        elif key == "entry_output_path":
            if value == "":
                messagebox.showerror(get_translations("other", "error_GUI_title"),
                                     get_translations("labels", "label_blank_error_messagebox"))
                break
            else:
                try:
                    os.chdir(value)
                    return True
                except FileNotFoundError:
                    messagebox.showerror(get_translations("other", "error_GUI_title"),
                                         get_translations("labels", "label_path_error_messagebox"))
                    break
    return False


def make_output_dir(output_folder_path):
    os.chdir(output_folder_path)

    try:
        os.mkdir("Json maker")
        os.chdir("Json maker")
    except FileExistsError:
        os.chdir("Json maker")

    try:
        os.mkdir("blockstates")
    except FileExistsError:
        pass

    try:
        os.mkdir("models")
        os.chdir("models")
    except FileExistsError:
        os.chdir("models")

    try:
        os.mkdir("block")
    except FileExistsError:
        pass

    try:
        os.mkdir("item")
    except FileExistsError:
        pass

    os.chdir(output_folder_path)


def zip_output_dir(output_folder_path):
    os.chdir(output_folder_path)

    try:
        shutil.make_archive("Json maker", "zip", "Json maker")
        shutil.rmtree("Json maker")
    except FileExistsError:
        shutil.rmtree("Json maker.zip")
        shutil.make_archive("Json maker", "zip", "Json maker")
        shutil.rmtree("Json maker")
