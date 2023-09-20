import os

from dotenv import load_dotenv
from types import MethodType
from django.test.runner import DiscoverRunner
from django.db import connections

load_dotenv()

user = os.getenv('POSTGRES_USER')

SQL = f"CREATE SCHEMA indicators AUTHORIZATION {user};"


def prepare_database(self):
    self.connect()
    self.connection.cursor().execute(SQL)


class PostgresSchemaTestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs):
        for connection_name in connections:
            connection = connections[connection_name]
            connection.prepare_database = MethodType(
                prepare_database, connection
            )
        return super().setup_databases(**kwargs)
