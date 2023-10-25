import configparser
from enum import Enum


msg = configparser.ConfigParser()
msg.read('messages.ini')


class UserMessages(str, Enum):
    not_found = msg['user']['not_found']
    updated_success = msg['user']['updated_success']
    deleted_success = msg['user']['deleted_success']
    incorrect_password = msg['user']['incorrect_password']
    login_success = msg['user']['login_success']


class RegionMessages(str, Enum):
    already_exist = msg['region']['already_exist']
    adding_success = msg['region']['adding_success']
    not_found = msg['region']['not_found']


class ApiSourceMessages(str, Enum):
    not_found = msg['api_source']['not_found']
    already_exist = msg['api_source']['already_exist']