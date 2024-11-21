import click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """ShellSleuth: Quickly find and manage your private tools, shortcuts, and aliases."""
    if ctx.invoked_subcommand is None:
        click.echo("hello world")
    else:
        click.echo("ShellSleuth: Quickly find and manage your private tools, shortcuts, and aliases.")


@click.command()
def list_aliases():
    """List all custom aliases defined in ~/.bashrc or ~/.zshrc."""
    # Implement the logic to list aliases
    click.echo("Listing all custom aliases...")


@click.command()
def list_executables():
    """List all executables in ~/bin and ~/.bin."""
    # Implement the logic to list executables
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
