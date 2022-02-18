import tradlib
from tkinter import *
from PIL import Image, ImageTk
import GUICommands
import Utils
import tradlib
import os

global correct_picture


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

    def on_resize(event):
        global correct_picture

        scale = [1.0, 1.0]

        scale[0] = root.winfo_height() / 300
        scale[1] = root.winfo_width() / 500

        for row in range(root.grid_size()[0]):
            root.grid_rowconfigure(row, minsize=20 * scale[0])

        for column in range(root.grid_size()[1]):
            root.grid_columnconfigure(column, minsize=20 * scale[1])

        for widget in root.winfo_children():
            if isinstance(widget, Button) or isinstance(widget, Label):
                if widget.winfo_name() == "!label4":
                    test = int(scale[0])
                    widget.config(font=("Arial", 10))
                else:
                    widget.config(font=("Helvetica", int(scale[1] * 8)))

        default_picture = Image.open(Utils.get_resources_path("resources\\pictures\\browse.png"))
        resized_picture = default_picture.resize((int(20 * scale[0] + 5), int(20 * scale[1] + 5)), Image.ANTIALIAS)
        correct_picture = ImageTk.PhotoImage(resized_picture)

        button_select_output_path.config(image=correct_picture)

        # left part

        label_modid.config(text=Utils.get_translations("labels", "label_modid"))
        label_material_name.config(text=Utils.get_translations("labels", "label_material_name"))
        button_lang.config(text=Utils.get_translations("buttons", "button_lang"))
        button_github.config(text=Utils.get_translations("buttons", "button_github"))

        # middle part

        label_title.config(text=Utils.get_translations("labels", "label_title"))
        label_json_list.config(text=Utils.get_translations("labels", "label_json_list"))
        label_zip_folder.config(text=Utils.get_translations("labels", "label_zip_folder"))

        # right part

        label_output_path.config(text=Utils.get_translations("labels", "label_output_path"))
        button_open_output_folder.config(text=Utils.get_translations("buttons", "button_open_output_folder"))
        button_generate_json.config(text=Utils.get_translations("buttons", "button_generate_json"))
        label_credits.config(text=Utils.get_translations("labels", "label_credits"))

    # Set basic parameters of frame

    root.geometry("660x400")
    root.resizable(width=True, height=True)
    root.title(Utils.get_translations("other", "main_GUI_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    root.bind("<Configure>", on_resize)

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
                         command=lambda: GUICommands.launch_language_gui(root))
    button_lang.grid(row=10, column=1, rowspan=3, columnspan=3, sticky="NSEW")

    button_github = Button(root, bg="darkgray", bd=2, highlightthickness=0, command=GUICommands.browse_to_github)
    button_github.grid(row=10, column=5, rowspan=3, columnspan=3, sticky="NSEW")

    # middle part

    label_title = Label(root, bg="blue", bd=0, highlightthickness=0)
    label_title.grid(row=0, column=6, rowspan=2, columnspan=13, sticky="NSEW")

    label_json_list = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_json_list.grid(row=2, column=9, rowspan=1, columnspan=7, sticky="NSEW")

    listbox_json_list = Listbox(root, selectbackground="darkgray", selectmode="multiple", bd=0, highlightthickness=0)
    listbox_json_list.grid(row=3, column=9, rowspan=7, columnspan=7, sticky="NSEW")

    # for json in Utils.get_json_list("items"):
    # listbox_json_list.insert(END, str(json).replace("+++", Utils.get_translations("other", "json_material")))

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

    button_generate_json = Button(root, bg="darkgray", bd=2, highlightthickness=0, command=None)
    button_generate_json.grid(row=8, column=17, rowspan=2, columnspan=7, sticky="NSEW")

    label_credits = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_credits.grid(row=11, column=17, rowspan=1, columnspan=7, sticky="NSEW")

    # Loop the frame

    root.mainloop()
