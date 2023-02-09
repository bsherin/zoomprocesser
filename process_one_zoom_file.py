from tkinter import *
from tkinter.filedialog import askopenfile
from pzf import do_process

if __name__ == "__main__":
    root = Tk()
    root.geometry('200x100')
    root.withdraw()
    the_file = askopenfile()
    do_process(the_file)
# btn = Button(root, text='Open', command=lambda: do_process())
# btn.pack(side=TOP, pady=10)

# mainloop()