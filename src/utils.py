import json

def load_manifest(path):

    with open(path, encoding="utf8") as f:
        return json.load(f)
