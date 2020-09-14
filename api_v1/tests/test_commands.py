from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class ImportDataCommandTest(TestCase):

    def setUp(self) -> None:
        call_command('refresh_dynamodb_tables')

    def tearDown(self) -> None:
        call_command('refresh_dynamodb_tables')

    def test_import_data_command(self):
        out = StringIO()
        call_command('import_data_from_omdb', stdout=out)
        self.assertIn('Command ran successfully.', out.getvalue())
