"""
Helper for git repo handling.
"""

import os
import subprocess


def is_repo(path: str):
    """
    Check if a folder is a git repo.
    """
    sub_folders = os.listdir(path)

    return ".git" in sub_folders

def check_default_branch(path: str):
    """
    Check if a repo has a main branch (main, master) or return an error message
    if not.
    """
    result = subprocess.run(
        ["git", "--no-pager", "branch"],
        cwd=path,
        capture_output=True,
        check=False,
    )

    error = None
    main_branch = None

    if result.returncode != 0:
        error = result.stderr.decode().strip()

    stdout = result.stdout.decode().strip()

    if stdout.find("main") != -1:
        main_branch = "main"
    elif stdout.find("master") != -1:
        main_branch = "master"
    else:
        error = "No main branch was found (main or master)"


    return error, main_branch

def pull_changes(path: str, branch: str):
    """
    Pull changes into the branch in the repo specified by the path. Return the output
    of the operation.
    """
    result = subprocess.run(
        ["git", "pull", "origin", branch],
        cwd=path,
        capture_output=True,
        check=False,
    )

    error = None
    message = None

    if result.returncode != 0:
        error = result.stderr.decode().strip()
    else:
        message = result.stdout.decode().strip()

    return error, message
