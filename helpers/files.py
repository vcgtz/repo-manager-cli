import os


def get_abs_path(path: str):
    return os.path.abspath(path)

def is_directory(path: str):
    return os.path.isdir(path)
