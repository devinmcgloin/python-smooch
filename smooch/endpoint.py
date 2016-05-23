import requests

from .authentication import JWT_TOKEN
from .exceptions import response_to_error


def ask(endpoint, data, method='get', files=None):
    url = "https://api.smooch.io/v1/{0}".format(endpoint)

    if method == 'get':
        caller_func = requests.get
    elif method == 'post':
        caller_func = requests.post
    elif method == 'put':
        caller_func = requests.put
    elif method == 'delete':
        caller_func = requests.delete

    headers = header()
    if files:
        headers.pop('content-type')

    response = caller_func(url=url, headers=headers, json=data)

    if response.status_code == 200 or response.status_code == 201:
        return response

    else:
        raise response_to_error(response)


def header():
    return {
        'authorization': 'Bearer {0}'.format(JWT_TOKEN),
        'content-type': 'application/json'
    }
