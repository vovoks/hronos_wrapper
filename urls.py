from settings import *


def get_token_url():
    return BASE_API_URL + JWT_TOKEN


def get_refresh_token_url():
    return BASE_API_URL + JWT_TOKEN_REFRESH


def get_schedule_url():
    return BASE_API_URL + SCHEDULE_API


def get_schedule_load_url():
    return BASE_API_URL + SCHEDULE_API
