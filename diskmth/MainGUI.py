from tkinter import *
from PIL import Image, ImageTk
import JsonManager
import GUICommands
import tradlib
import Utils
import os


global correct_picture
global selected_items


def main_gui():
    # Create the frame

    root = Tk()

    # Initialization of some useful variables:

    bool_check = BooleanVar()

    # Initialization of json and translations

    tradlib.set_translations_files_path(os.environ["USERPROFILE"] +
                                        "\\Desktop\\dev\\Json maker\\diskmth\\resources\\lang", True)
    tradlib.load_translations_files()

    # Definition of some useful functions

    def on_update(event):
        global correct_picture
        global selected_items

        scale = [1.0, 1.0]

        scale[0] = root.winfo_height() / 300
        scale[1] = root.winfo_width() / 500

        for row in range(root.grid_size()[0]):
            root.grid_rowconfigure(row, minsize=20 * scale[0])

        for column in range(root.grid_size()[1]):
            root.grid_columnconfigure(column, minsize=20 * scale[1])

        updated_font = ("TkDefaultFont", int(scale[1] * 6.5))

        # left part

        label_modid.config(text=Utils.get_translations("labels", "label_modid"), font=updated_font)
        label_material_name.config(text=Utils.get_translations("labels", "label_material_name"), font=updated_font)
        button_lang.config(text=Utils.get_translations("buttons", "button_lang"), font=updated_font)
        button_github.config(text=Utils.get_translations("buttons", "button_github"), font=updated_font)

        # middle part

        label_title.config(text=Utils.get_translations("labels", "label_title"), font=("Arial", int(scale[1] * 12)))
        label_json_list.config(text=Utils.get_translations("labels", "label_json_list"), font=updated_font)
        label_zip_folder.config(text=Utils.get_translations("labels", "label_zip_folder"), font=updated_font)

        # right part

        label_output_path.config(text=Utils.get_translations("labels", "label_output_path"), font=updated_font)
        default_picture = Image.open(Utils.get_resources_path("resources\\pictures\\browse.png"))
        resized_picture = default_picture.resize((int(20 * scale[0] + 5), int(20 * scale[1] + 5)), Image.ANTIALIAS)
        correct_picture = ImageTk.PhotoImage(resized_picture)
        button_select_output_path.config(image=correct_picture)
        button_open_output_folder.config(text=Utils.get_translations("buttons", "button_open_output_folder"),
                                         font=updated_font)
        button_generate_json.config(text=Utils.get_translations("buttons", "button_generate_json"), font=updated_font)
        label_credits.config(text=Utils.get_translations("labels", "label_credits"), font=updated_font)

    # Set basic parameters of frame

    root.geometry("660x400")
    root.resizable(width=True, height=True)
    root.title(Utils.get_translations("other", "main_GUI_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    root.bind("<Configure>", on_update)

    # Add components to frame

    label_background = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_background.grid(row=0, column=0, rowspan=16, columnspan=26, sticky="NSEW")

    # left part

    label_modid = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_modid.grid(row=2, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    entry_modid = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_modid.grid(row=3, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    label_material_name = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_material_name.grid(row=6, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    entry_material_name = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_material_name.grid(row=7, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    button_lang = Button(root, bg="darkgray", bd=2, highlightthickness=0,
                         command=lambda: GUICommands.launch_language_gui(root, listbox_json_list))
    button_lang.grid(row=10, column=1, rowspan=3, columnspan=3, sticky="NSEW")

    button_github = Button(root, bg="darkgray", bd=2, highlightthickness=0, command=GUICommands.browse_to_github)
    button_github.grid(row=10, column=5, rowspan=3, columnspan=3, sticky="NSEW")

    # middle part

    label_title = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_title.grid(row=0, column=6, rowspan=2, columnspan=13, sticky="NSEW")

    label_json_list = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_json_list.grid(row=2, column=9, rowspan=1, columnspan=7, sticky="NSEW")

    listbox_json_list = Listbox(root, selectbackground="darkgray", selectmode="multiple", bd=0, highlightthickness=0)
    listbox_json_list.grid(row=3, column=9, rowspan=7, columnspan=7, sticky="NSEW")

    for json in JsonManager.get_json_list():
        listbox_json_list.insert(END, json)

    label_zip_folder = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_zip_folder.grid(row=11, column=9, rowspan=1, columnspan=7, sticky="NSEW")

    checkbutton_zip_folder = Checkbutton(root, bg="gray", activebackground="gray",
                                         variable=bool_check, onvalue=True, offvalue=False, bd=0, highlightthickness=0)
    checkbutton_zip_folder.grid(row=12, column=12, rowspan=1, columnspan=1, sticky="NSEW")

    # right part

    label_output_path = Label(root, bg="gray", bd=0,highlightthickness=0)
    label_output_path.grid(row=2, column=17, rowspan=1, columnspan=5, sticky="NSEW")

    entry_output_path = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_output_path.grid(row=3, column=17, rowspan=1, columnspan=5, sticky="NSEW")

    button_select_output_path = Button(root, bd=2, highlightthickness=0,
                                       command=lambda: GUICommands.browse_output_path(entry_output_path))
    button_select_output_path.grid(row=3, column=23, rowspan=1, columnspan=1, sticky="NSEW")

    button_open_output_folder = Button(root, bg="darkgray", bd=2, highlightthickness=0,
                                       command=lambda: GUICommands.open_output_folder(entry_output_path))
    button_open_output_folder.grid(row=5, column=17, rowspan=1, columnspan=7, sticky="NSEW")

    button_generate_json = Button(root, bg="darkgray", bd=2, highlightthickness=0,
                                  command=lambda: GUICommands.generate_json(entry_modid, entry_material_name,
                                                                            entry_output_path, bool_check,
                                                                            listbox_json_list))
    button_generate_json.grid(row=8, column=17, rowspan=2, columnspan=7, sticky="NSEW")

    label_credits = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_credits.grid(row=11, column=17, rowspan=1, columnspan=7, sticky="NSEW")

    # Loop the frame

    root.mainloop()
