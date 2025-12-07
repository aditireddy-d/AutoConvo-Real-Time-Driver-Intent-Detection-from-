import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_files(directory, ext=".wav"):
    return [f for f in os.listdir(directory) if f.endswith(ext)]
