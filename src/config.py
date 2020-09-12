import logging

from src.bl.helper import ConfigHelper


class BaseConfig:
    ENV = ConfigHelper.get_config_value('ENV', 'testing')
    IS_TESTING = ENV.lower() == 'testing'
    AWS_DDB_ENDPOINT_URL = None


class DevelopmentConfig(BaseConfig):
    AWS_DDB_ENDPOINT_URL = 'http://localhost:8000'


config_name = ConfigHelper.get_config_value('CONFIG_NAME', 'development')

config_map = {
    'development': DevelopmentConfig,
}

current_config = config_map.get(config_name)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
