import glob
import os
import shutil


def getAllResourcesPath():
    path1 = "..\\diskmth\\resources\\*.*"
    path2 = "..\\diskmth\\resources\\*\\*.*"
    path3 = "..\\diskmth\\resources\\*\\*\\*.*"
    filesPath = []
    for i in glob.glob(path1):
        filesPath.append(os.path.abspath(i))
    for i in glob.glob(path2):
        filesPath.append(os.path.abspath(i))
    for i in glob.glob(path3): 
        filesPath.append(os.path.abspath(i))
    return filesPath

def getFullCommand():
    resourcesList = getAllResourcesPath()
    command = "--onefile --windowed --clean --name \"Advent calendar\""
    command = "\"" + os.path.abspath("..\\python\\Scripts\\pyinstaller.exe").replace("\\", "/") + "\" " + command
    command = "\"" + os.path.abspath("..\\python\\python.exe").replace("\\", "/") + "\" " + command

    if os.path.exists("..\\diskmth\\resources\\icons\\app_icon.ico"):
        command = command + " --icon \"" + os.path.abspath("..\\diskmth\\resources\\icons\\app_icon.ico").replace("\\", "/") + "\""

    for i in range(len(resourcesList)):
        command = command + " --add-data \"" + resourcesList[i].replace("\\", "/") + ";.\""

    command = command +  " --collect-data \"pygame\""
    command = command + " \"" + os.path.abspath("..\\diskmth\\Main.py") + "\""
    return command

if __name__ == '__main__':
    pythonPath = "\"" + os.path.abspath("..\\python\\python.exe").replace("\\", "/") + "\""
    os.chdir("..")
    try:
        os.mkdir("build")
    except FileExistsError:
        shutil.rmtree("build")
        os.mkdir("build")
    os.chdir("build")
    os.system("\"" + getFullCommand() + "\"")
    os.system("pause")