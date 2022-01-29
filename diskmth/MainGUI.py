from tkinter import filedialog
from tkinter import *
import Utils
import webbrowser
import LanguageGUI
import os
import subprocess

global modid
global material_name
global output_folder_path
global json_list


def main_gui():
    # Create the frame

    root = Tk()

    # Initialisation of json and translations

    Utils.load_translations()
    Utils.load_json()

    # Definition of some useful functions

    def browse_to_github():
        webbrowser.open("https://github.com/Disk-MTH/Json-maker")

    def launch_language_gui(parent_frame):
        root.destroy()
        LanguageGUI.language_gui(root)

    def add_to_list():
        if not listbox_to_select.curselection() == ():
            for json in listbox_to_select.curselection():
                listbox_selected.insert(json, listbox_to_select.get(json))
                listbox_to_select.delete(json)

    def remove_from_list():
        if not listbox_selected.curselection() == ():
            for json in listbox_selected.curselection():
                listbox_to_select.insert(json, listbox_selected.get(json))
                listbox_selected.delete(json)

    def browse_output_path():
        global output_folder_path
        output_folder_path = filedialog.askdirectory(initialdir=os.environ["USERPROFILE"] + "\\Desktop",
                                                     title=Utils.get_translations("other", "file_selector_GUI_title"))
        entry_output_path.delete(0, END)
        entry_output_path.insert(0, output_folder_path)

    def get_entries():
        global modid
        global material_name
        global output_folder_path
        global json_list

        modid = entry_modid.get()
        material_name = entry_material_name.get()
        output_folder_path = entry_output_path.get()
        json_list = listbox_selected.get('@1,0', END)

    def open_output_folder():
        global output_folder_path
        get_entries()
        filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        formatted_path = os.path.normpath(output_folder_path)

        if os.path.isdir(formatted_path):
            subprocess.run([filebrowser_path, formatted_path])

    def generate_json():
        global modid
        global material_name
        global output_folder_path
        global json_list

        get_entries()

        print(modid)
        print(material_name)
        print(output_folder_path)
        print(json_list)

    # Set basic parameters of frame

    root.geometry("500x300")
    root.resizable(width=False, height=False)
    root.title(Utils.get_translations("other", "main_GUI_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    # Add components to frame

    label_background = Label(root, bg="gray", width=500, height=200, bd=0, highlightthickness=0)
    label_background.place(x=0, y=0)

    # left part

    label_modid = Label(root, bg="gray", text=Utils.get_translations("labels", "label_modid"), bd=0,
                        highlightthickness=0)
    label_modid.place(x=80 - label_modid.winfo_reqwidth() / 2, y=50)

    entry_modid = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_modid.place(x=10, y=70, width=140, height=30)

    label_material_name = Label(root, bg="gray", text=Utils.get_translations("labels", "label_material_name"), bd=0,
                                highlightthickness=0)
    label_material_name.place(x=80 - label_material_name.winfo_reqwidth() / 2, y=130)

    entry_material_name = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_material_name.place(x=10, y=150, width=140, height=30)

    button_lang = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_lang"), bd=2,
                         highlightthickness=0, command=lambda: launch_language_gui(root))
    button_lang.place(x=10, y=210, width=60, height=60)

    button_github = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_github"), bd=2,
                           highlightthickness=0, command=browse_to_github)
    button_github.place(x=90, y=210, width=60, height=60)

    # middle part

    label_title = Label(root, bg="gray", text=Utils.get_translations("labels", "label_title"), font="Arial", bd=0,
                        highlightthickness=0)
    label_title.place(x=root.winfo_width() / 2 - label_title.winfo_reqwidth() / 2, y=5)

    listbox_to_select = Listbox(root, selectbackground="darkgray", selectmode=MULTIPLE, bd=0, highlightthickness=0)
    listbox_to_select.place(x=160, y=50, width=170, height=60)

    for json in Utils.get_json_list("items"):
        listbox_to_select.insert(END, json)

    button_add_to_list = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_add_to_list"), bd=2,
                                highlightthickness=0, command=add_to_list)
    button_add_to_list.place(x=160, y=120, width=170, height=30)

    canvas_line = Canvas(root, bg="black", bd=0, highlightthickness=0)
    canvas_line.place(x=170, y=159, width=150, height=2)

    listbox_selected = Listbox(root, selectbackground="darkgray", selectmode=MULTIPLE, bd=0, highlightthickness=0)
    listbox_selected.place(x=160, y=170, width=170, height=60)

    button_remove_from_list = Button(root, bg="darkgray",
                                     text=Utils.get_translations("buttons", "button_remove_from_list"), bd=2,
                                     highlightthickness=0, command=remove_from_list)
    button_remove_from_list.place(x=160, y=240, width=170, height=30)

    # left part

    label_output_path = Label(root, bg="gray", text=Utils.get_translations("labels", "label_output_path"), bd=0,
                              highlightthickness=0)
    label_output_path.place(x=395 - label_output_path.winfo_reqwidth() / 2, y=50)

    entry_output_path = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_output_path.place(x=340, y=70, width=110, height=30)

    button_select_output_path_picture = PhotoImage(file=Utils.get_resources_path("resources\\pictures\\browse.png"))
    button_select_output_path = Button(root, image=button_select_output_path_picture, bd=2, highlightthickness=0,
                                       command=browse_output_path)
    button_select_output_path.place(x=460, y=70, width=30, height=30)

    button_open_output_folder = Button(root, bg="darkgray",
                                       text=Utils.get_translations("buttons", "button_open_output_folder"), bd=2,
                                       highlightthickness=0, command=open_output_folder)
    button_open_output_folder.place(x=340, y=130, width=150, height=40)

    button_generate_json = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_generate_json"),
                                  bd=2, highlightthickness=0, command=generate_json)
    button_generate_json.place(x=340, y=190, width=150, height=50)

    label_credits = Label(root, bg="gray", text=Utils.get_translations("labels", "label_credits"), bd=0,
                          highlightthickness=0)
    label_credits.place(x=360, y=250)

    # Loop the frame

    root.mainloop()
