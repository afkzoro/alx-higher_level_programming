#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename) as fp:
        return json.load(fp)
