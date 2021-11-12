"""
Creates a list of sequentially named folders.

Prompts the user to select a destionation folder under which to create sub-folders,
as well as the number of sub-folders to create and the suffixes for the folder names.
"""
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

application_window = tk.Tk()

# Ask the user to select a folder
src = filedialog.askdirectory(parent=application_window,
                              initialdir=os.getcwd(),
                              title="Please select the destination folder.")
n_colonies = simpledialog.askinteger("Input", 
                                     "How many colonies are there in total?",
                                     parent=application_window,
                                     minvalue = 0)
suffix = simpledialog.askstring("Input", "What is the folder suffix? E.g. SIS01-T, LNR02-N",
                                parent=application_window)
application_window.destroy()


for foldername in range (1,n_colonies): 
    os.mkdir(os.path.join(src,suffix+"-"+str(foldername))) #change the suffix to fit site codes
