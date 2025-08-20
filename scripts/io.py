import shutil

import os.path

# call this before running any other commands
def set_home_dir(home_dir:str, verbose:bool=True):
    global HOME_DIR, IMG_PATH, TXT_PATH, JSON_PATH
    HOME_DIR = f"{os.getcwd()}/{home_dir}"
    IMG_PATH = f"{HOME_DIR}/img"
    TXT_PATH = f"{HOME_DIR}/txt"
    JSON_PATH = f"{HOME_DIR}/json"
    if (verbose):
        print("Starting PYLAB on:")
        print(f"- home dir: {HOME_DIR}")
        print(f"- image dir: {IMG_PATH}")
        print(f"- text dir: {TXT_PATH}")
        print(f"- json dir: {JSON_PATH}")

def get_home_dir():
    return HOME_DIR

def path(*paths:str):
    """
    Builds a path by joining together the given set of paths.
    Joins with " / ", BACKSLASHES are NOT allowed.
    Params:
        paths (str) : a tuple of paths to join together
    Returns:
        path (str) : the joined paths
    """
    paths = list(paths)
    endsWithSlash = paths[-1][-1] == "/"
    result = ""
    for i in range(len(paths)):
        p = paths[i]
        if "\\" in p:
            print("[Error]: Paths cannot contain \"\\\", only \"/\"")
            return None
        paths[i] = p.strip("/")
    
    return "/" + "/".join(paths) + ("/" if endsWithSlash else "")


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
    Deletes the __pycache__ folder.\\
    Call this when closing the program.
    """
    shutil.rmtree(f"{HOME_DIR}/scripts/__pycache__")
    if sayGoodbye: print("Done!")
    exit(0)

def read(path : str) -> list[str] :
    """
    Reads the lines of a given file

    Params:
        path (str) : the file path

    Returns:
        lines (list[str]) : the lines read from the file
    """
    lines = []
    with open(f"/{HOME_DIR}/" + path, "r") as f:
        lines = f.readlines()
    return lines

def write(file_name:str, content:str, replace_existing:bool=False):
    """
    Writes the content to a file with a specific name.
    The file will be saved to "./txt/{file_name}"

    Params:
        file_name (str) : the file name
        content (str) : the content to be written to the file
        replace_existng (bool) : if set to True it automatically replaces an already existing file (if there is any), otherwise it asks the user to confirm before proceding
    """
    path = f"{TXT_PATH}/{file_name}"
    if not check_for_dir_file_to_save(path, TXT_PATH, replace_existing):
        return
    with open(path, "w") as f:
        f.write(content)