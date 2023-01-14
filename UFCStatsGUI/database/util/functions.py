import json


def read_json(file_name):
    with open(file_name, "rb") as f:
        return json.load(f)
