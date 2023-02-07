import os
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
from process_one_zoom_file import do_process
root = Tk()
root.geometry('200x100')
root.withdraw()

the_dir = askdirectory()

for fname in os.listdir(the_dir):
    os.chdir(the_dir)
    if fname[0] == ".":
        continue
    with open(fname) as file:
        do_process(file)

