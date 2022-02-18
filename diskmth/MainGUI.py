from tkinter import *
import Utils


def main_gui():
    # Create the frame

    root = Tk()

    # Initialisation of json and translations

    Utils.load_translations()
    Utils.load_json()

    # Definition of some useful functions

    def on_resize(event):
        scale = [1.0, 1.0]

        scale[0] = root.winfo_height() / 300
        scale[1] = root.winfo_width() / 500

        for row in range(root.grid_size()[0]):
            root.grid_rowconfigure(row, minsize=20 * scale[0])

        for column in range(root.grid_size()[1]):
            root.grid_columnconfigure(column, minsize=20 * scale[1])

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

    label_modid = Label(root, bg="gray", text=Utils.get_translations("labels", "label_modid"), bd=0,
                        highlightthickness=0)
    label_modid.grid(row=2, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    entry_modid = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_modid.grid(row=3, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    label_material_name = Label(root, bg="gray", text=Utils.get_translations("labels", "label_material_name"), bd=0,
                                highlightthickness=0)
    label_material_name.grid(row=6, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    entry_material_name = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_material_name.grid(row=7, column=1, rowspan=1, columnspan=7, sticky="NSEW")

    button_lang = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_lang"), bd=2,
                         highlightthickness=0, command=None)
    button_lang.grid(row=10, column=1, rowspan=3, columnspan=3, sticky="NSEW")

    button_github = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_github"), bd=2,
                           highlightthickness=0, command=None)
    button_github.grid(row=10, column=5, rowspan=3, columnspan=3, sticky="NSEW")

    # middle part

    label_title = Label(root, bg="gray", text=Utils.get_translations("labels", "label_title"), font="Arial", bd=0,
                        highlightthickness=0)
    label_title.grid(row=0, column=8, rowspan=2, columnspan=9, sticky="NSEW")

    label_json_list = Label(root, bg="gray", text=Utils.get_translations("labels", "label_json_list"), bd=0,
                            highlightthickness=0)
    label_json_list.grid(row=2, column=9, rowspan=1, columnspan=7, sticky="NSEW")

    listbox_json_list = Listbox(root, selectbackground="darkgray", selectmode="multiple", bd=0, highlightthickness=0)
    listbox_json_list.grid(row=3, column=9, rowspan=7, columnspan=7, sticky="NSEW")

    for json in Utils.get_json_list("items"):
        listbox_json_list.insert(END, str(json).replace("+++", Utils.get_translations("other", "json_material")))

    label_zip_folder = Label(root, bg="gray", text=Utils.get_translations("labels", "label_zip_folder"), bd=0,
                             highlightthickness=0)
    label_zip_folder.grid(row=11, column=9, rowspan=1, columnspan=7, sticky="NSEW")

    check = BooleanVar()
    checkbutton_zip_folder = Checkbutton(root, bg="gray", activebackground="gray",
                                         variable=check, onvalue=True, offvalue=False, bd=0, highlightthickness=0)
    checkbutton_zip_folder.grid(row=12, column=12, rowspan=1, columnspan=1, sticky="NSEW")

    # left part

    label_output_path = Label(root, bg="gray", text=Utils.get_translations("labels", "label_output_path"), bd=0,
                              highlightthickness=0)

    label_output_path.grid(row=2, column=17, rowspan=1, columnspan=5, sticky="NSEW")

    entry_output_path = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_output_path.grid(row=3, column=17, rowspan=1, columnspan=5, sticky="NSEW")

    button_select_output_path_picture = PhotoImage(file=Utils.get_resources_path("resources\\pictures\\browse.png"))
    button_select_output_path = Button(root, image=button_select_output_path_picture, bd=2, highlightthickness=0,
                                       command=None)
    button_select_output_path.grid(row=3, column=23, rowspan=1, columnspan=1, sticky="NSEW")

    button_open_output_folder = Button(root, bg="darkgray",
                                       text=Utils.get_translations("buttons", "button_open_output_folder"), bd=2,
                                       highlightthickness=0, command=None)
    button_open_output_folder.grid(row=6, column=17, rowspan=1, columnspan=7, sticky="NSEW")

    button_generate_json = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_generate_json"),
                                  bd=2, highlightthickness=0, command=None)
    button_generate_json.grid(row=9, column=17, rowspan=2, columnspan=7, sticky="NSEW")

    label_credits = Label(root, bg="gray", text=Utils.get_translations("labels", "label_credits"), bd=0,
                          highlightthickness=0)
    label_credits.grid(row=12, column=17, rowspan=1, columnspan=7, sticky="NSEW")

    # Loop the frame

    root.mainloop()
