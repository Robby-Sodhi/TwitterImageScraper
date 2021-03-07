class myClass():
    def __init__(self, name, age, username):
        self.name = name
        self.username = username
        self.age = age

    def post(self, message):
        print(message.format(**self.__dict__))

instance = myClass("Robstersgaming", "50", "Rob")
instance.post("Hello {name} nice name!!! {age}, {username}")

import logging
from logging.handlers import RotatingFileHandler
import traceback

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler("log.txt", maxBytes=10000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
try:
    1/0
except Exception as e:
    logger.error(str(e))
    logger.error(traceback.format_exc())
    raise Exception(e)
