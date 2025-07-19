#!/usr/bin/env python3
import requests

def access_nested_map(nested_map, path):
    """Access a value in a nested map using a sequence of keys."""
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

def get_json(url):
    response=requests.get(url)
    return response.json()

def memoize(method):
    """Memoization decorator"""
    attr_name = "_memoize_" + method.__name__

    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper




