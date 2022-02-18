import webbrowser


global modid
global material_name
global output_folder_path
global is_zip_file
global json_list

# Functions for MainGUI

def browse_to_github():
    webbrowser.open("https://github.com/Disk-MTH/Json-maker")


def get_entries():
    global modid
    global material_name
    global output_folder_path
    global is_zip_file
    global json_list

    modid = entry_modid.get()
    material_name = entry_material_name.get()
    output_folder_path = entry_output_path.get()
    is_zip_file = check.get()


def launch_language_gui(parent_frame):
    root.destroy()
    LanguageGUI.language_gui(root)


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
    global is_zip_file
    global json_list

    modid = entry_modid.get()
    material_name = entry_material_name.get()
    output_folder_path = entry_output_path.get()
    is_zip_file = check.get()

    json_list = []
    for selected_items in listbox_json_list.curselection():
        json_list.append(listbox_json_list.get(selected_items)
                         .replace(Utils.get_translations("other", "json_material"), "+++"))


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
    global is_zip_file
    global json_list

    get_entries()

    with open("C:\\Users\\gille_l9m5mj2\\Desktop\\ee.txt", "w") as file:
        file.write(Utils.get_resources_path("test"))

    json_list = []
    for selected_items in listbox_json_list.curselection():
        json_list.append(listbox_json_list.get(selected_items)
                         .replace(Utils.get_translations("other", "json_material"), "+++"))



