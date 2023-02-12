## Zoomprocessor

These are simple scripts to convert Zoom transcripts to csv files that are usefully formatted.

There are Mac executables in the "dist" folder. (Double click to unzip.)

There are two different executables, one that processes a single Zoom transcript, and another that will process
all of the files in a folder. These executables will prompt you to select a file or folder.

If you would rather invoke scripts from the command line you can run `python3 pzf.py <path to filename>` to convert a
single file. To process a folder you run this: `python3 pzdir.py <path to folder>`. This will require installing
dependencies, etc.

If you want to build new executables, you'll want to execute something like these commands

```
pyinstaller --onefile --noconsole --target-architecture universal2 process_zoom_folder.py
pyinstaller --onefile --noconsole --target-architecture universal2 process_one_zoom_file.py

```

A note: The transcripts produced by Zoom often contain successive turns of talk by the same speaker. In their
current form, the python scripts here merge these successive turns. But if you look in **pzf.py** at the `do_process` function,
you'll see that it takes an optional input `merge` that defaults to True. So, if you want, you can modify these scripts
so that the merging isn't done.

