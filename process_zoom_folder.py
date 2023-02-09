import os
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
from process_one_zoom_file import do_process
from pzdir import do_dir_process
root = Tk()
root.geometry('200x100')
root.withdraw()

the_dir = askdirectory()
do_dir_process(the_dir)


