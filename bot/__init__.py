import os
import ujson

CONFIG_FILE = os.environ.get('JHS_CONFIG_FILE')

if CONFIG_FILE:
    with open(CONFIG_FILE) as file_pointer:
        config = ujson.load(file_pointer)
else:
    config = {}
    raise Exception(
        "You didn't set \"JHS_CONFIG_FILE\" enviroment variable")
