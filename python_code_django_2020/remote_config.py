import os


class ConfigHelper:

    @classmethod
    def get_config_value(cls, key: str, default: str = None) -> str:
        return os.getenv(key=key, default=default)
