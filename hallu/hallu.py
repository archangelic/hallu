import click
import os

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("hallu y'all")
    else:
        pass

@cli.command('init')
@click.option('-n', '--name', prompt=True)
@click.option('-d', '--directory', default=os.getcwd())
def hallu_init(name, directory):
    if 'settings.py' not in os.listdir(directory):
        with open('settings.py', 'w') as settings:
            settings.write(f'NAME = "{name}"\n')
    click.echo(f'Project: "{name}" successfully initiated')

