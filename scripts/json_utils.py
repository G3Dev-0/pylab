from scripts import io_utils

import json

def load(path:str) -> dict:
    """
    Reads and parses to python code types the contents of a given json file

    Params:
        path (str) : the json file path

    Returns:
        json (dict) : the parsed json values
    """
    jsonContent = "\n".join(io_utils.read(path))
    return json.loads(jsonContent)

def write(file_name:str, content:dict, replace_existing:bool=False):
    """
    Writes the content to a "*.json" file with a specific name.
    The file will be saved to "./json/{file_name}.json"

    Params:
        file_name (str) : the file name
        content (dict) : the content to be written to the file
        replace_existng (bool) : if set to True it automatically replaces an already existing file (if there is any), otherwise it asks the user to confirm before proceding
    """
    path = f"{io_utils.JSON_PATH}/{file_name}.json"
    if not io_utils.check_for_dir_file_to_save(path, io_utils.JSON_PATH, replace_existing):
        return
    with open(path, "w") as f:
        f.write(json.dumps(content, indent=4))