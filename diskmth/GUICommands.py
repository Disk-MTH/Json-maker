from tkinter import filedialog
from tkinter import *
import LanguageGUI
import subprocess
import webbrowser
import Utils
import os

global modid
global material_name
global output_folder_path
global is_zip_file
global json_list


# Functions for MainGUI

def browse_to_github():
    webbrowser.open("https://github.com/Disk-MTH/Json-maker")


def launch_language_gui(root):
    root.wm_attributes("-disabled", True)
    LanguageGUI.language_gui(root)


def browse_output_path(entry_output_path):
    global output_folder_path
    output_folder_path = filedialog.askdirectory(initialdir=os.environ["USERPROFILE"] + "\\Desktop",
                                                 title=Utils.get_translations("other", "file_selector_GUI_title"))
    entry_output_path.delete(0, END)
    entry_output_path.insert(0, output_folder_path)


def open_output_folder(entry_output_folder_path):
    global output_folder_path
    get_entries(entry_output_folder_path=entry_output_folder_path)
    filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    formatted_path = os.path.normpath(output_folder_path)

    if os.path.isdir(formatted_path):
        subprocess.run([filebrowser_path, formatted_path])


def generate_json():
    pass


# Functions for MainGUI

def close_gui(root, parent_frame):
    root.destroy()
    parent_frame.wm_attributes("-disabled", False)
    parent_frame.wm_attributes("-topmost", True)
    parent_frame.wm_attributes("-topmost", False)


def apply_changes(listbox_languages_list, root, parent_frame):
    try:
        selected_language = listbox_languages_list.get(listbox_languages_list.curselection())
        Utils.set_active_language(selected_language)
        close_gui(root, parent_frame)
    except TclError:
        close_gui(root, parent_frame)


# Other functions

def get_entries(entry_modid=None, entry_material_name=None, entry_output_folder_path=None, bool_check=None,
                listbox_json_list=None):
    global modid
    global material_name
    global output_folder_path
    global is_zip_file
    global json_list

    try:
        modid = entry_modid.get()
    except AttributeError:
        pass

    try:
        material_name = entry_material_name.get()
    except AttributeError:
        pass

    try:
        output_folder_path = entry_output_folder_path.get()
    except AttributeError:
        pass

    try:
        is_zip_file = check.get()
    except AttributeError:
        pass

    try:
        json_list = []
        for selected_item in listbox_json_list.curselection():
            json_list.append(listbox_json_list.get(selected_items)
                             .replace(Utils.get_translations("other", "json_material"), "+++"))
    except AttributeError:
        pass
