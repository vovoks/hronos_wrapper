from typing import Dict, Any

from helper import REQUEST_TYPE, GET, POST, DATA

from requests import get, post, Response
from urls import *


def handler(url: str, request_type: REQUEST_TYPE, request_data: DATA = None):
    errors = []
    response = []

    def resp():
        return {'errors': errors,
                'response': response}

    if request_type == 'post' and request_data is not None:
        r = post(url, request_data)
    else:
        r = get(url)

    if r.status_code != 200:
        errors.append([r.status_code, r.text])
    else:
        response.append([r.text])
    return resp()


def get_token(login: str, password: str) -> dict[str, str]:
    handler(get_token_url(), POST, {'login': login, 'password': password})
