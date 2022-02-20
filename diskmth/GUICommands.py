from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import JsonManager
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
    output_folder_path = filedialog.askdirectory(initialdir=os.environ["USERPROFILE"] + "\\Desktop",
                                                 title=Utils.get_translations("other", "file_selector_GUI_title"))
    entry_output_path.delete(0, END)
    entry_output_path.insert(0, output_folder_path)


def open_output_folder(entry_output_path):
    global output_folder_path
    get_entries(entry_output_path=entry_output_path)
    filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    formatted_path = os.path.normpath(output_folder_path)

    if os.path.isdir(formatted_path):
        subprocess.run([filebrowser_path, formatted_path])


def generate_json(entry_modid, entry_material_name, entry_output_path, bool_check, listbox_json_list):
    get_entries(entry_modid=entry_modid, entry_material_name=entry_material_name, entry_output_path=entry_output_path,
                bool_check=bool_check, listbox_json_list=listbox_json_list)

    Utils.make_output_dir(output_folder_path)

    if is_zip_file:
        Utils.zip_output_dir(output_folder_path)


# Functions for LanguageGUI

def close_gui(root, parent_frame, listbox_json_list):
    root.destroy()
    parent_frame.wm_attributes("-disabled", False)
    parent_frame.wm_attributes("-topmost", True)
    parent_frame.wm_attributes("-topmost", False)
    listbox_json_list.delete(0, END)
    for json in JsonManager.get_json_list("items"):
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

def get_entries(entry_modid=None, entry_material_name=None, entry_output_path=None, bool_check=None,
                listbox_json_list=None):
    global modid
    global material_name
    global output_folder_path
    global is_zip_file
    global json_list

    empty_entry = False

    try:
        if entry_modid.get() == "":
            empty_entry = True
        else:
            modid = entry_modid.get()
    except AttributeError:
        pass

    try:
        if entry_material_name.get() == "":
            empty_entry = True
        else:
            material_name = entry_material_name.get()
    except AttributeError:
        pass

    try:
        if entry_output_path.get() == "":
            empty_entry = True
        else:
            output_folder_path = entry_output_path.get()
    except AttributeError:
        pass

    try:
        is_zip_file = bool_check.get()
    except AttributeError:
        pass

    try:
        json_list = []
        for selected_item in listbox_json_list.curselection():
            json_list.append(listbox_json_list.get(selected_item)
                             .replace(Utils.get_translations("other", "json_material"), "+++"))
        if not json_list:
            empty_entry = True
    except AttributeError:
        pass

    if empty_entry:
        messagebox.showerror(Utils.get_translations("other", "error_GUI_title"),
                             Utils.get_translations("labels", "label_blank_error_messagebox"))
