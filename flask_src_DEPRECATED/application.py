from typing import Optional

from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from flask_src_DEPRECATED import config


class AppSingleton:
    __instance: Optional[Flask] = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if AppSingleton.__instance is None:
            AppSingleton()
        return AppSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if AppSingleton.__instance is None:
            AppSingleton.__instance = Flask(__name__)
            AppSingleton.__instance.config.from_object(config.current_config)
            CORS(AppSingleton.__instance)
            # self.bootstrap_development_side_wheels()

    def bootstrap_development_side_wheels(self):
        if config.current_config.IS_TESTING:
            # --------------------------------------------------------------
            # legacy implementation
            # import boto3
            #
            # from helpers.dynamodb_helper import DynamodbClient
            #
            # dynamodb = boto3.resource(
            #     'dynamodb',
            #     region_name=current_config.AWS_ACCESS_REGION,
            #     aws_access_key_id=current_config.AWS_ACCESS_KEY_ID,
            #     aws_secret_access_key=current_config.AWS_SECRET_ACCESS_KEY,
            #     endpoint_url=current_config.AWS_DDB_ENDPOINT_URL)
            # DynamodbClient.set_connection(dynamodb)
            # legacy implementation
            # --------------------------------------------------------------

            # --------------------------------------------------------------
            # pynamodb implementation
            from pynamodb.connection import TableConnection
            original_init = TableConnection.__init__

            def init(*args, **kwargs):
                kwargs['host'] = config.current_config.AWS_DDB_ENDPOINT_URL
                return original_init(*args, **kwargs)

            TableConnection.__init__ = init
            # pynamodb implementation
            # --------------------------------------------------------------


app = AppSingleton.get_instance()
api = Api(app)
