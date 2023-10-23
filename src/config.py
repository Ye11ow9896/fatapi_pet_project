from dotenv import load_dotenv
import os

load_dotenv()


PG_HOST = os.environ.get('PG_HOST')
PG_USER = os.environ.get('PG_USER')
PG_DB_NAME = os.environ.get('PG_DB_NAME')
PG_PORT = os.environ.get('PG_PORT')
PG_PASS = os.environ.get('PG_PASS')

SALT = os.environ.get('SALT')