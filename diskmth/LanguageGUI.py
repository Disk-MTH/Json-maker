from tkinter import *
import Utils
import MainGUI


def language_gui(parent_frame):
    # Create the frame

    root = Tk()

    # Initialisation of some useful variables

    languages_list = Utils.get_languages_list()

    # Definition of some useful functions

    def close():
        root.destroy()
        MainGUI.main_gui()

    def apply_changes():
        try:
            selected_language = listbox_languages_list.get(listbox_languages_list.curselection())
            Utils.set_active_language(selected_language)
            close()
        except TclError:
            close()

    # Set basic parameters of frame

    root.geometry("250x300")
    root.resizable(width=False, height=False)
    root.title(Utils.get_translations("other", "translations_GUI_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    # Add components to frame

    root.protocol("WM_DELETE_WINDOW", close)

    label_background = Label(root, bg="gray", width=250, height=300, bd=0, highlightthickness=0)
    label_background.place(x=0, y=0)

    label_title = Label(root, bg="gray", text=Utils.get_translations("labels", "label_title_language"), font="Arial",
                        bd=0, highlightthickness=0)
    label_title.place(x=root.winfo_width() / 2 - label_title.winfo_reqwidth() / 2, y=5)

    listbox_languages_list = Listbox(root, selectbackground="darkgray", bd=0, highlightthickness=0)
    listbox_languages_list.place(x=25, y=35, width=200, height=175)

    for languages in languages_list:
        listbox_languages_list.insert(END, languages)

    button_apply_changes = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_apply_changes"),
                                  bd=2, highlightthickness=0, command=apply_changes)
    button_apply_changes.place(x=25, y=230, width=200, height=50)

    # Loop the frame

    root.mainloop()
