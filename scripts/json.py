import scripts.io as io

import json

def load(path:str) -> dict:
    """
    Reads and parses to python code types the contents of a given json file

    Params:
        path (str) : the json file path

    Returns:
        json (dict) : the parsed json values
    """
    loaded_lines = io.read(path)

    lines = []
    # parse lines by removing comments
    is_in_comment_block = False
    COMMENT_LINE = "//"
    COMMENT_BLOCK_START = "/*"
    COMMENT_BLOCK_END = "*/"
    for line in loaded_lines:
        line = line.strip()
        # comment line not at the beginning
        if COMMENT_LINE in line and line.strip().index(COMMENT_LINE) > 0:
            line = line[:line.index(COMMENT_LINE)]

        # one-line comment block
        if COMMENT_BLOCK_START in line and COMMENT_BLOCK_END in line:
            block_start = line.index(COMMENT_BLOCK_START)
            block_end = line.index(COMMENT_BLOCK_END) + 2
            if block_start > block_end: continue
            line = line[:block_start] + line[block_end:]

        # end comment block
        if COMMENT_BLOCK_END in line and is_in_comment_block:
            line = line[line.index(COMMENT_BLOCK_END) + 2:]
            is_in_comment_block = False
        
        # comment line
        if is_in_comment_block or line.startswith(COMMENT_LINE): continue
        
        # start comment block
        if COMMENT_BLOCK_START in line and not is_in_comment_block:
            line = line[:line.index(COMMENT_BLOCK_START)]
            is_in_comment_block = True
        
        lines.append(line)
    jsonContent = "".join(lines)
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
    path = f"{io.JSON_PATH}/{file_name}.json"
    if not io.check_for_dir_file_to_save(path, io.JSON_PATH, replace_existing):
        return
    with open(path, "w") as f:
        f.write(json.dumps(content, indent=4))