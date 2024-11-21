import click
from loguru import logger

from src.core.logger_ import init_logger
from src.utils.file_info import get_file_type


def init():
    init_logger()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    init()
    """shell_sleuth: Quickly find and manage your private tools, shortcuts, and aliases."""
    if ctx.invoked_subcommand is None:
        logger.debug(f"{ctx=}")
        logger.info(f"{ctx=}")
        click.echo("hello world")
    else:
        click.echo("shell_sleuth: Quickly find and manage your private tools, shortcuts, and aliases.")


@click.command()
def list_aliases():
    """List all custom aliases defined in ~/.bashrc or ~/.zshrc."""
    # Implement the logic to list aliases
    click.echo("Listing all custom aliases...")


@click.command('le')
def list_executables():
    """List all executables in ~/bin and ~/.bin."""
    # Implement the logic to list executables
    import os
    current_dir = os.getcwd()
    logger.debug(f"{current_dir=}")
    file_1 = os.listdir(current_dir)[0]
    logger.info(f"{file_1=}")
    logger.info(f"{get_file_type(file_1)=}")
    click.echo("Listing all executables...")


@click.command()
def command_history():
    """Get command usage frequency from history and sort them."""
    # Implement the logic to get and sort command history
    click.echo("Getting command usage frequency from history...")


cli.add_command(list_aliases)
cli.add_command(list_executables)
cli.add_command(command_history)

if __name__ == "__main__":
    cli()
