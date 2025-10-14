"""
Entry point for all the repo-related commands.
"""

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

    fprint(f"Analyzing repos in folder: [blue]{full_path}[/blue]")


@app.command()
def update(path: str):
    """
    Update to main/master all the available Git projects in the given path.
    """
    full_path = get_abs_path(path)

    fprint(f"Updating all repos in [blue]{full_path}[/blue]")
