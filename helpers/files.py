"""
Helper for file handling.
"""

import os


def get_abs_path(path: str):
    """
    Get absolute path from a given relative path.
    """
    return os.path.abspath(path)

def is_directory(path: str):
    """
    Check if a path is a directory.
    """
    return os.path.isdir(path)
