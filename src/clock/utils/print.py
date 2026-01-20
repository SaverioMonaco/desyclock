"""
Pretty terminal printing utilities for pybib.

Provides:
- error()
- warn()
- success()
- info()
- rainbow()
"""

from rich.console import Console
from rich.text import Text

__all__ = [
    "error",
    "warn",
    "success",
    "info",
    "rainbow",
]

_console = Console()


def error(msg: str) -> None:
    """Print an error message."""
    _console.print(f"[bold red]✖[/bold red] {msg}")


def warn(msg: str) -> None:
    """Print a warning message."""
    _console.print(f"[bold yellow]⚠[/bold yellow] {msg}")


def success(msg: str) -> None:
    """Print a success message."""
    _console.print(f"[bold green]✔[/bold green] {msg}")


def info(msg: str) -> None:
    """Print an informational message."""
    _console.print(f"[cyan]ℹ INFO:[/cyan] {msg}")


def rainbow(msg: str) -> None:
    """Print a rainbow-colored message (character-by-character)."""
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    text = Text()

    for i, char in enumerate(msg):
        text.append(char, style=colors[i % len(colors)])

    _console.print(text)