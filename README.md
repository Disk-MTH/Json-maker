# Json maker

This project does not require any administrator permission, either for the setup 
of the environment or for the build of the project. So you can use this project 
on any windows computer. (If you are ever asked for permissions open an 
issue so I can see what this is due to)


## Presentation

This project repository is a tool to shorten a long and tedious task: making jsons for minecraft mods. Instead of copying and pasting by hand and giving the right names and modid, this tool does it for you automatically.


## How to use and edit?

This project is completely self-contained: you don't need to have python installed, 
or anything else!

**__/!\ WARNING :__**

If during one of the following steps a SmartScreen window opens saying 
"SmartScreen has protected your computer", this is normal: the .exe files (which I made 
entirely myself) do not have a digital signature therefore windows defender is in panic. 
(If ever you do not trust my scripts do not go further because you will necessarily 
need them! Moreover you can see their "contents" in the "[uncompiled scripts](https://github.com/Disk-MTH/Json-maker/tree/master/scripts/uncompiled%20scripts)" folder).

Once the environment is setup (see below), it will take VERY long to move the folder, 
so choose a "permanent" location!


### Use:

Just download the latest [release](https://github.com/Disk-MTH/Json-maker/releases) available and run it. You don't have to do anything more than read what is written in the GUI!


### Edit:

1) Download:

To start, above the frame containing the code, there is a green button titled "Code", 
click on it, then on "Download ZIP" (or use [this link](https://github.com/Disk-MTH/Json-maker/archive/refs/heads/master.zip)). This will download you a .zip 
folder which you will need to extract (I recommend extracting to a "permanet" location). 

2) Setup:

(Warning : This step can be very long (depends on your computer))

Then in the unzipped folder find the "[scripts](https://github.com/Disk-MTH/Json-maker/tree/master/scripts)" folder and run the "setup.exe" 
file. This will open a window of the control terminal in which you will be able to 
follow the decompilation of the integrated python interpreter. (If you go back to 
the root folder of the project you can find a "python" folder that has been 
created).

/!\ : In case of update, if you resetup the python environment, it will overwrite the old 
one

3) Run:

To launch the application you simply need to run the "run.exe" file that you may have 
seen in the "[scripts](https://github.com/Disk-MTH/Json-maker/tree/master/scripts)" folder.

4) Edit:

To add new jsons, go to the "[diskmth/resources/json](https://github.com/Disk-MTH/Json-maker/tree/master/diskmth/resources/json)" folder and open the "[available_json](https://github.com/Disk-MTH/Json-maker/blob/master/diskmth/resources/json/available_json.json)" file with a text editor. Then just look at how the json's are saved and copy-paste changing the names. Then add the json in the right folders (if you use this tool I assume you know how Minecraft json works). Look in the other json already present how to do so that the names are replaced correctly (the modid indicated in the json provided must be "---" and the name of the material "+++"). 

You can also change translations or add new ones via the "[lang](https://github.com/Disk-MTH/Json-maker/tree/master/diskmth/resources/lang)" folder. Again you just have to look at how the languages ​​already present are made and copy and paste. For more information on language files see my "[Tradlib](https://github.com/Disk-MTH/Tradlib)" library. 

Finally you can change the default language when opening the GUI by changing the "active_language" variable at the top of the "[Utils.py](https://github.com/Disk-MTH/Json-maker/blob/master/diskmth/Utils.py)" file.

5) Build:

To compile the program, nothing could be easier: all you have to do is run the 
"build.exe" file and a control terminal window will open. Wait for the end of the 
execution (when the terminal displays "press a key to continue ...") and you will see in 
the main folder a "build" folder in which 2 folders and 1 file will be present. go to the 
"dist" folder and you will have your compiled application. (If there is no icon or if the 
images do not all work, check the name of your images and restart a compilation. If 
that still does not work open an issue).

/!\ : If you ever rebuild the program after making changes, the program will overwrite 
the old build files.


## License

All the files in this repository are completely free of rights (see the [license](https://github.com/Disk-MTH/Json-maker/blob/master/license.txt)) so 
you can grab the images, the code ... and do whatever you want with them (just 
respect the [license](https://github.com/Disk-MTH/Json-maker/blob/master/license.txt)).

Thanks for reading and good development!

Disk_MTH