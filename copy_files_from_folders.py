"""
Copies files from many folders.

Prompts the user for the source directory containing a set of folders, then 
copies out the last image from each folder. (This was used for a particular
project).
"""
import os
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog
import ctypes

application_window = tk.Tk()

# Ask the user to select a folder
src = filedialog.askdirectory(parent=application_window,
                                 initialdir=os.getcwd(),
                                 title="Please select the source folder containing all the colony folders.")
site = simpledialog.askstring("Input", "What is the site name? (e.g. LNR02, SIS01)",
                                parent=application_window)
application_window.destroy()

if not os.path.exists(os.path.join(src,"For report")):
    dest = os.makedirs(os.path.join(src,"For report"))

for folder in os.listdir(src): 
    if folder.startswith(site):
        folderpath = os.path.join(src,folder)
        if not len(os.listdir(folderpath)) == 0: 
            #copies last image in each subfolder
            img = os.listdir(folderpath)[-1] 
            imgpath = os.path.join(folderpath,img)
            imgcopy = shutil.copy(imgpath, os.path.join(src,"For report"))
            newname = os.path.join(src,"For report",folder+'.jpg')
            os.rename(imgcopy,newname)
            
ctypes.windll.user32.MessageBoxW(0, "All done!", "Message", 1)