import os 

def set_input_path(relative_path:str, current_path:str):
    return os.path.relpath(relative_path, current_path)
