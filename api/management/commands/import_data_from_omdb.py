from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Created dynamodb tables'

    def handle(self, *args, **options):
        try:
            title_data = self.import_title_data()
            self.import_episodes(data=title_data)
            self.stdout.write(self.style.SUCCESS('Command ran successfully.'))
        except Exception as ex:
            self.stdout.write(f'ERROR > {ex}', )

    def import_title_data(self) -> dict:
        pass

    def import_episodes(self, data: dict) -> None:
        pass
