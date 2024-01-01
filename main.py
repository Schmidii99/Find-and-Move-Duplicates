import time
from pprint import pprint
from tkinter import Tk
from tkinter.filedialog import askdirectory

import os
import shutil

import hashlib
from File import MyFile


def iterate_folder(path, existing_files: dict) -> dict:
    walker = os.walk(path)
    for folder, sub_folders, files in walker:
        for file in files:
            print(f"Found file {file}")
            existing_files[file] = MyFile.from_path(os.path.join(folder, file))
        for sub_folder in sub_folders:
            existing_files = iterate_folder(sub_folder, existing_files)

    return existing_files


def move_duplicates(path, uniqe_files: dict, destination):
    walker = os.walk(path)
    for folder, sub_folders, files in walker:
        for file in files:
            file_path = os.path.join(folder, file)
            files_obj = uniqe_files.get(file)
            if files_obj is not None:
                if files_obj == MyFile.from_path(file_path):
                    print(f"Moved identical file: {file_path}")
                    shutil.move(file_path, os.path.join(destination, file))

        for sub_folder in sub_folders:
            move_duplicates(sub_folder, uniqe_files, destination)


if __name__ == '__main__':
    Tk().withdraw()

    # The files in this folder won't be moved
    original = askdirectory(title="Select the original folder")
    # The files in this folder WILL be compared and moved
    addition = askdirectory(title="Select the additional folder")
    # duplicate files will be moved from addition to this folder
    destination = askdirectory(title="Select the duplicate destination folder")

    files_dict = dict()
    files_dict = iterate_folder(original, files_dict)
    print("--------------------------------------------------")
    time.sleep(3)
    move_duplicates(addition, files_dict, destination)
    print("--------------------------------------------------")
    print("Done")
