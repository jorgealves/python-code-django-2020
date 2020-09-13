from django.core.management.base import BaseCommand
from pynamodb.constants import PAY_PER_REQUEST_BILLING_MODE

from api.models.comment import Comment
from api.models.episode import Episode
from api.models.release import Release

models = [
    Release,
    Episode,
    Comment
]


class Command(BaseCommand):
    help = 'Created dynamodb tables'

    def handle(self, *args, **options):
        try:
            for model in models:
                if model.exists():
                    model.delete_table()
                    model.create_table(billing_mode=PAY_PER_REQUEST_BILLING_MODE)
                    self.stdout.write(f'{str(model)} created')
            self.stdout.write(self.style.SUCCESS('Command ran successfully.'))
        except Exception as ex:
            self.stdout.write(f'ERROR > {ex}', )
