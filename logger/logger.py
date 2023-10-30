import logging
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(filename='logger/api.log')
handler.setLevel(level=logging.WARNING)
handler.setFormatter(fmt=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logger.addHandler(hdlr=handler)
