import configparser
import os

UTIL_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = UTIL_FILE_PATH.replace("common", "config") + "/config.ini"

def get_config_value(Section, Key):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH, "utf-8")
    return config.get(Section, Key)

