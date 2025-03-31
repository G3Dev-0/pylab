import shutil

import os.path

IMG_PATH = "./img"
TXT_PATH = "./txt"
JSON_PATH = "./json"

def check_for_dir_file_to_save(path:str, check_dir:str, replace_existing:bool=False) -> bool :
    """
    Checks whether the check_dir already exists, if not it creates it.\\
    It then checks if the file at path already exists, if so, it asks for a replacement confirmation from the user, but only if replace existing is set to false.\\
    Otherwise it will automatically replace the file without asking anything to the user.

    Params:
        path (str) : the file path
        check_dir (str) : the directory path where the file will be saved
        replace_existng (bool) : if set to True it automatically replaces an already existing file (if there is any), otherwise it asks the user to confirm before proceding

    Returns:
        save_state (bool) : True if it can save, False if the user asked to not replace the file
    """
    if not os.path.exists(check_dir): os.mkdir(check_dir)
    if os.path.exists(path) and not replace_existing:
        if input(f"Another file with the same name already exists at '{path}'. Do you want to replace it? [ENTER/n]") == "n":
            return False
    return True

def close(sayGoodbye:bool=True):
    """
    Deletes the __pychace__ folder.\\
    Call this when closing the program.
    """
    shutil.rmtree("./scripts/__pycache__")
    print("Done!")

def read(path : str) -> list[str] :
    """
    Reads the lines of a given file

    Params:
        path (str) : the file path

    Returns:
        lines (list[str]) : the lines read from the file
    """
    lines = []
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def write(file_name:str, content:str, replace_existing:bool=False):
    """
    Writes the content to a "*.txt" file with a specific name.
    The file will be saved to "./txt/{file_name}.txt"

    Params:
        file_name (str) : the file name
        content (str) : the content to be written to the file
        replace_existng (bool) : if set to True it automatically replaces an already existing file (if there is any), otherwise it asks the user to confirm before proceding
    """
    path = f"{TXT_PATH}/{file_name}.txt"
    if not check_for_dir_file_to_save(path, TXT_PATH, replace_existing):
        return
    with open(path, "w") as f:
        f.write(content)