import logging

from flask_src_DEPRECATED.bl.helper import ConfigHelper


class BaseConfig:
    # Environment
    ENV = ConfigHelper.get_config_value('ENV', 'development')
    IS_TESTING = ENV.lower() == 'testing'

    # Cloud
    REGION = ConfigHelper.get_config_value('REGION', None)

    # DynamoDB
    AWS_DDB_ENDPOINT_URL = ConfigHelper.get_config_value('AWS_DDB_ENDPOINT_URL', None)


class DevelopmentConfig(BaseConfig):
    AWS_DDB_ENDPOINT_URL = 'http://database:8000'


config_name = ConfigHelper.get_config_value('CONFIG_NAME', 'development')

config_map = {
    'development': DevelopmentConfig,
}

current_config = config_map.get(config_name)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
