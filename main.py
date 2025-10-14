"""
Entry point for the `repo-manager` CLI app.
"""

import typer
from commands import repo

app = typer.Typer()
app.add_typer(repo.app)


if __name__ == "__main__":
    app()
