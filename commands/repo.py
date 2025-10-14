"""
Entry point for all the repo-related commands.
"""

import os
import typer
from rich import print as fprint
from helpers.files import get_abs_path, is_directory

app = typer.Typer()

@app.command()
def analyze(path: str):
    """
    Analyze a folder path and print how many Git projects are in there.
    """
    full_path = get_abs_path(path)

    if not is_directory(full_path):
        fprint(f"[bold red]{full_path} is not a valid folder path[/bold red]")
        raise typer.Exit()

    fprint(f"Analyzing repos in folder: [blue]{full_path}[/blue]\n")
    fprint("[bold]Files:[/bold]")
    for folder in os.listdir(full_path):
        sub_folder_path = os.path.join(full_path, folder)

        if not is_directory(sub_folder_path):
            icon = "•"
            descriptor = "([bold red]is not a folder[/bold red])"
        else:
            icon = "▸"
            sub_folders = os.listdir(sub_folder_path)
            is_repo_msg = "([bold green]is a repo[/bold green])"
            not_is_repo_msg = "([bold red]is not a repo[/bold red])"

            descriptor = is_repo_msg if ".git" in sub_folders else not_is_repo_msg

        fprint(f"[bold yellow]{icon}[/bold yellow] {folder} {descriptor}")

    print()


@app.command()
def update(path: str):
    """
    Update to main/master all the available Git projects in the given path.
    """
    full_path = get_abs_path(path)

    fprint(f"Updating all repos in [blue]{full_path}[/blue]")
