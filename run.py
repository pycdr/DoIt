from rich.console import Console
from rich.syntax import Syntax
from os import system
console = Console()
console.print("""welcome to the [u blue]DoIt[/u blue] program!
hope to enjoy it.
well, we are in first versions so it is on [i]delevoping[/i].
anyway, you can run as [bold green]GUI(graphical user interface)[/bold green] or [bold red]CLI(command line interface)[/bold red].
the CLI version document will be uploaded on github and you should use it with arguments,
but for now if you want to see its demo,
GUI is going to load by [i]electron[/i]...""")
console.print(Syntax("cd ./GUI/\nelectron ./index.js","bash", theme="monokai", line_numbers=False))
system("cd ./GUI/; electron ./index.js")
