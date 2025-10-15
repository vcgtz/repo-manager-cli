"""
Entry point for all the repo-related commands.
"""

import os
import typer
from rich import print as fprint
from helpers.files import get_abs_path, is_directory
from helpers.git import is_repo, check_default_branch, pull_changes

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

    fprint(f"Analyzing content within the folder: [blue]{full_path}[/blue]\n")
    fprint("[bold]Dir Content:[/bold]")

    for folder in os.listdir(full_path):
        sub_folder_path = os.path.join(full_path, folder)

        if not is_directory(sub_folder_path):
            descriptor = "(file)"
        else:
            descriptor = "(repo)" if is_repo(sub_folder_path) else "(folder)"

        print(f"● {folder} {descriptor}")


@app.command()
def update(path: str):
    """
    Update to main/master all the available Git projects in the given path.
    """
    full_path = get_abs_path(path)

    fprint(f"Updating all the repos within the folder: [blue]{full_path}[/blue]\n")
    fprint("[bold]Repos:[/bold]")

    for folder in os.listdir(full_path):
        sub_folder_path = os.path.join(full_path, folder)

        if is_directory(sub_folder_path) and is_repo(sub_folder_path):
            branch_error, branch = check_default_branch(sub_folder_path)

            if branch_error:
                fprint(f"● {folder}\n[red]{branch_error}[/red]")
            else:
                pull_error, output = pull_changes(sub_folder_path, str(branch))
                context = f"[red]{pull_error}[/red]" if pull_error else f"[green]{output}[/green]"

                fprint(f"● {folder}\n{context}")
