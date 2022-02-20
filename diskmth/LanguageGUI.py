from tkinter import *
import Utils
import tradlib
import GUICommands

global correct_picture


def language_gui(parent_frame, listbox_json_list):
    # Create the frame

    root = Tk()

    # Definition of some useful functions

    def on_update(event):
        global correct_picture

        scale = [1.0, 1.0]

        scale[0] = root.winfo_height() / 300
        scale[1] = root.winfo_width() / 240

        for row in range(root.grid_size()[0]):
            root.grid_rowconfigure(row, minsize=20 * scale[0])

        for column in range(root.grid_size()[1]):
            root.grid_columnconfigure(column, minsize=20 * scale[1])

        for widget in root.winfo_children():
            if isinstance(widget, Button) or isinstance(widget, Label):
                if widget.winfo_name() == "!label2":
                    widget.config(font=("TkDefaultFont", int(scale[1] * 15)))
                else:
                    widget.config(font=("TkDefaultFont", int(scale[1] * 8)))

    # Set basic parameters of frame

    root.geometry("240x300")
    root.resizable(width=True, height=True)
    root.title(Utils.get_translations("other", "translations_GUI_title"))
    root.iconbitmap(Utils.get_resources_path("resources\\icons\\app_icon.ico"))

    # Add components to frame

    root.bind("<Configure>", on_update)
    root.protocol("WM_DELETE_WINDOW", lambda: GUICommands.close_gui(root, parent_frame, listbox_json_list))

    label_background = Label(root, bg="gray", bd=0, highlightthickness=0)
    label_background.grid(row=0, column=0, rowspan=16, columnspan=13, sticky="NSEW")

    label_title = Label(root, bg="gray", text=Utils.get_translations("labels", "label_title_language"), font="Arial",
                        bd=0, highlightthickness=0)
    label_title.grid(row=0, column=2, rowspan=1, columnspan=8, sticky="NSEW")

    listbox_languages_list = Listbox(root, selectbackground="darkgray", bd=0, highlightthickness=0)
    listbox_languages_list.grid(row=2, column=1, rowspan=8, columnspan=10, sticky="NSEW")

    for languages in tradlib.get_available_languages():
        listbox_languages_list.insert(END, languages)

    button_apply_changes = Button(root, bg="darkgray", text=Utils.get_translations("buttons", "button_apply_changes"),
                                  bd=2, highlightthickness=0,
                                  command=lambda: GUICommands.apply_changes(listbox_languages_list, root, parent_frame,
                                                                            listbox_json_list))
    button_apply_changes.grid(row=11, column=1, rowspan=2, columnspan=10, sticky="NSEW")

    # Loop the frame

    root.mainloop()
