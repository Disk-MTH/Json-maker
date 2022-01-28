from tkinter import *
import Utils
import webbrowser

def main_gui():
    # Create the frame

    root = Tk()

    # Initialisation of some useful variables

    translation_dictionary = Utils.get_translations_dict()
    active_language = "english"

    # Definition of some useful functions

    def get_translations(translation_group, translation_key):
        for languages in translation_dictionary:
            if languages["language"] == active_language:
                try:
                    return languages[translation_group][0][translation_key]
                except KeyError:
                    return "Error"

    def select_language():
        pass

    def browse_to_github():
        webbrowser.open("https://github.com/Disk-MTH/Json-maker")

    # Set basic parameters of frame

    root.geometry("500x300")
    root.resizable(width=False, height=False)
    root.title(get_translations("other", "app_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    # Add components to frame

    label_background = Label(bg="gray", width=500, height=200, bd=0, highlightthickness=0)
    label_background.place(x=0, y=0)

    # left part

    label_modid = Label(root, bg="gray", text=get_translations("labels", "label_modid"), bd=0, highlightthickness=0)
    label_modid.place(x=80 - label_modid.winfo_reqwidth() / 2, y=50)

    entry_modid = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_modid.place(x=10, y=70, width=140, height=30)

    label_material_name = Label(root, bg="gray", text=get_translations("labels", "label_material_name"), bd=0,
                                highlightthickness=0)
    label_material_name.place(x=80 - label_material_name.winfo_reqwidth() / 2, y=130)

    entry_material_name = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_material_name.place(x=10, y=150, width=140, height=30)

    button_lang = Button(root, bg="darkgray", text=get_translations("buttons", "button_lang"), bd=2,
                         highlightthickness=0)
    button_lang.place(x=10, y=210, width=60, height=60)

    button_github = Button(root, bg="darkgray", text=get_translations("buttons", "button_github"), bd=2,
                           highlightthickness=0, command=browse_to_github)
    button_github.place(x=90, y=210, width=60, height=60)

    # middle part

    label_title = Label(bg="gray", text=get_translations("labels", "label_title"), font="Arial", bd=0,
                        highlightthickness=0)
    label_title.place(x=root.winfo_width() / 2 - label_title.winfo_reqwidth() / 2, y=5)

    listbox_to_select = Listbox(root, selectbackground="darkgray", selectmode=MULTIPLE, bd=0, highlightthickness=0)
    listbox_to_select.place(x=160, y=50, width=170, height=60)

    listbox_to_select.insert(END, "a")
    listbox_to_select.insert(END, "b")
    listbox_to_select.insert(END, "c")
    listbox_to_select.insert(END, "d")

    button_add_to_list = Button(root, bg="darkgray", text=get_translations("buttons", "button_add_to_list"), bd=2,
                                highlightthickness=0)
    button_add_to_list.place(x=160, y=120, width=170, height=30)

    canvas_line = Canvas(root, bg="black", bd=0, highlightthickness=0)
    canvas_line.place(x=170, y=159, width=150, height=2)

    listbox_selected = Listbox(root)
    listbox_selected.place(x=160, y=170, width=170, height=60)

    button_remove_from_list = Button(root, bg="darkgray", text=get_translations("buttons", "button_remove_from_list"),
                                     bd=2, highlightthickness=0)
    button_remove_from_list.place(x=160, y=240, width=170, height=30)

    # left part

    label_output_path = Label(root, bg="gray", text=get_translations("labels", "label_output_path"), bd=0,
                              highlightthickness=0)
    label_output_path.place(x=395 - label_output_path.winfo_reqwidth() / 2, y=50)

    entry_output_path = Entry(root, bg="white", bd=0, highlightthickness=0)
    entry_output_path.place(x=340, y=70, width=110, height=30)

    button_select_output_path_picture = PhotoImage(file=Utils.get_resources_path("resources\\pictures\\browse.png"))
    button_select_output_path = Button(root, image=button_select_output_path_picture, bd=2, highlightthickness=0)
    button_select_output_path.place(x=460, y=70, width=30, height=30)

    button_open_output_folder = Button(root, bg="darkgray",
                                       text=get_translations("buttons", "button_open_output_folder"), bd=2,
                                       highlightthickness=0)
    button_open_output_folder.place(x=340, y=130, width=150, height=40)

    button_generate_json = Button(root, bg="darkgray", text=get_translations("buttons", "button_generate_json"), bd=2,
                                  highlightthickness=0)
    button_generate_json.place(x=340, y=190, width=150, height=50)

    label_credits = Label(root, bg="gray", text=get_translations("labels", "label_credits"), bd=0, highlightthickness=0)
    label_credits.place(x=360, y=250)

    # Loop the frame

    root.mainloop()
