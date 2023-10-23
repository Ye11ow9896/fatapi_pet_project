import logging
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(filename='logger/api.log')
handler.setLevel(level=logging.WARNING)
handler.setFormatter(fmt=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger_api = logging.getLogger()
logger_api.setLevel(logging.WARNING)
logger_api.addHandler(hdlr=handler)

print(logger_api.handlers)
print(logger_api.level)
