from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import JsonManager
import LanguageGUI
import subprocess
import webbrowser
import shutil
import Utils
import os

global modid
global material_name
global output_folder_path
global is_zip_file
global json_list
global selected_json


# Functions for MainGUI

def browse_to_github():
    webbrowser.open("https://github.com/Disk-MTH/Json-maker")


def launch_language_gui(root, listbox_json_list):
    global selected_json
    selected_json = list(listbox_json_list.curselection())
    root.wm_attributes("-disabled", True)
    LanguageGUI.language_gui(root, listbox_json_list)


def browse_output_path(entry_output_path):
    global output_folder_path
    entry_output_path.delete(0, END)
    entry_output_path.insert(0, filedialog.askdirectory(initialdir=os.environ["USERPROFILE"] + "\\Desktop",
                                                        title=Utils.get_translations("other",
                                                                                     "file_selector_GUI_title")))


def open_output_folder(entry_output_path):
    global output_folder_path
    get_entries(entries_to_get={"entry_output_path": entry_output_path})
    if Utils.check_empty_entry(entries_to_check={"entry_output_path": output_folder_path}):
        filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

        formatted_path = os.path.normpath(output_folder_path)
        if os.path.isdir(formatted_path):
            subprocess.run([filebrowser_path, formatted_path])


def generate_json(entry_modid, entry_material_name, entry_output_path, bool_check, listbox_json_list):
    get_entries(entries_to_get={"entry_modid": entry_modid, "entry_material_name": entry_material_name,
                                "entry_output_path": entry_output_path, "bool_check": bool_check,
                                "listbox_json_list": listbox_json_list})
    if Utils.check_empty_entry(entries_to_check={"entry_modid": modid, "entry_material_name": material_name,
                                                 "listbox_json_list": json_list,
                                                 "entry_output_path": output_folder_path}):
        Utils.make_output_dir(output_folder_path)
        JsonManager.create_json_lists_to_generate(json_list, material_name)
        JsonManager.create_json_files(modid, material_name, output_folder_path)
        if JsonManager.cancel_generate:
            is_output_empty = True
            for root, folders, files in os.walk(output_folder_path + "\\Json maker"):
                if files:
                    is_output_empty = False
            if is_output_empty:
                shutil.rmtree(output_folder_path + "\\Json maker")
            JsonManager.cancel_generate = False
        else:
            if is_zip_file:
                Utils.zip_output_dir(output_folder_path)
            messagebox.showinfo(Utils.get_translations("other", "finish_GUI_title"),
                                Utils.get_translations("labels", "label_finish_messagebox"))


# Functions for LanguageGUI

def close_gui(root, parent_frame, listbox_json_list):
    root.destroy()
    parent_frame.wm_attributes("-disabled", False)
    parent_frame.wm_attributes("-topmost", True)
    parent_frame.wm_attributes("-topmost", False)
    listbox_json_list.delete(0, END)
    for json in JsonManager.get_json_list():
        listbox_json_list.insert(END, str(json).replace("+++", Utils.get_translations("other", "json_material")))
    for json in selected_json:
        listbox_json_list.select_set(json)


def apply_changes(listbox_languages_list, root, parent_frame, listbox_json_list):
    try:
        selected_language = listbox_languages_list.get(listbox_languages_list.curselection())
        Utils.set_active_language(selected_language)
        close_gui(root, parent_frame, listbox_json_list)
    except TclError:
        close_gui(root, parent_frame, listbox_json_list)


# Other functions

def get_entries(entries_to_get):
    global modid
    global material_name
    global output_folder_path
    global is_zip_file
    global json_list

    for key, value in entries_to_get.items():
        if key == "entry_modid":
            modid = value.get()
        elif key == "entry_material_name":
            material_name = value.get()
        elif key == "entry_output_path":
            output_folder_path = value.get()
        elif key == "bool_check":
            is_zip_file = value.get()
        elif key == "listbox_json_list":
            json_list = []
            for selected_item in value.curselection():
                json_list.append(value.get(selected_item))
