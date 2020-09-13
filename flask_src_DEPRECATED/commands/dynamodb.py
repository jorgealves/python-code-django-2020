import click
from flask.cli import AppGroup
from pynamodb.constants import PAY_PER_REQUEST_BILLING_MODE

from flask_src_DEPRECATED.application import AppSingleton
from flask_src_DEPRECATED.models.comment import Comment
from flask_src_DEPRECATED.models.episode import Episode
from flask_src_DEPRECATED.models.release import Release


group = AppGroup('dynamodb')

models = [
    Release,
    Episode,
    Comment
]


@group.command('create')
def create_tables():
    try:
        for model in models:
            if not model.exists():
                model.create_table(billing_mode=PAY_PER_REQUEST_BILLING_MODE)
                click.secho(f'{str(model)} created', fg='green', bold=True)
        click.secho('Command ran successfully.', fg='green', bold=True)
    except Exception as ex:
        click.secho(f'ERROR > {ex}', fg='red', bold=True)


AppSingleton.get_instance().cli.add_command(group)
