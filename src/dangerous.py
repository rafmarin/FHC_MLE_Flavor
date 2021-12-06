import requests


def status_ok(url="https://www.google.com", **kwargs):
    return requests.head(url, verify=False, **kwargs).ok
