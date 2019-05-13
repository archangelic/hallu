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
@click.option('-d', '--directory', default=None)
def hallu_init(name, directory):
    if not directory:
        directory = os.getcwd()
    elif directory not in os.listdir(os.getcwd()):
        os.mkdir(directory)
        os.chdir(directory)
    cur_dir = os.getcwd()
    dirs = ['site', 'zine']
    if 'settings.py' not in os.listdir(cur_dir):
        with open('settings.py', 'w') as settings:
            settings.write(f'NAME = "{name}"\n')
    for folder in dirs:
        try:
            os.mkdir(folder)
        except FileExistsError:
            click.echo(f'{folder} directory already exists')
    click.echo(f'Project: "{name}" successfully initiated')

