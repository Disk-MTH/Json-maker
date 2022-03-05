import glob
import os
import shutil


def get_all_resources():
    path_1 = "..\\diskmth\\resources\\*.*"
    path_2 = "..\\diskmth\\resources\\*\\*.*"
    path_3 = "..\\diskmth\\resources\\*\\*\\*.*"
    path_4 = "..\\diskmth\\resources\\*\\*\\*\\*.*"
    path_5 = "..\\diskmth\\resources\\*\\*\\*\\*\\*.*"
    files_path = []

    for i in glob.glob(path_1):
        files_path.append(os.path.abspath(i))
    for i in glob.glob(path_2):
        files_path.append(os.path.abspath(i))
    for i in glob.glob(path_3):
        files_path.append(os.path.abspath(i))
    for i in glob.glob(path_4):
        files_path.append(os.path.abspath(i))
    for i in glob.glob(path_5):
        files_path.append(os.path.abspath(i))
    return files_path


def get_full_command():
    resources_list = get_all_resources()

    command = "--onefile --windowed --clean --name \"Json maker\""
    command = "\"" + os.path.abspath("..\\python\\Scripts\\pyinstaller.exe").replace("\\", "/") + "\" " + command
    command = "\"" + os.path.abspath("..\\python\\python.exe").replace("\\", "/") + "\" " + command

    if os.path.exists("..\\diskmth\\resources\\icons\\app_icon.ico"):
        command = command + " --icon \"" + os.path.abspath("..\\diskmth\\resources\\icons\\app_icon.ico").replace("\\", "/") + "\""

    for i in range(len(resources_list)):
        command = command + " --add-data \"" + resources_list[i].replace("\\", "/") + ";.\""

    command = command + " \"" + os.path.abspath("..\\diskmth\\Main.py") + "\""

    return command


if __name__ == '__main__':
    os.chdir("..")
    try:
        os.mkdir("build")
    except FileExistsError:
        shutil.rmtree("build")
        os.mkdir("build")
    os.chdir("build")
    os.system("\"" + get_full_command() + "\"")
    os.system("pause")
