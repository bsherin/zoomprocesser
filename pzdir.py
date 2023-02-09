import os
import sys
from pzf import do_process


def do_dir_process(dir_name):
    os.chdir(dir_name)
    for fname in os.listdir(dir_name):
        if fname[0] == ".":
            continue
        with open(fname) as file:
            do_process(file)


if __name__ == "__main__":
    dname = sys.argv[1]
    do_dir_process(dname)