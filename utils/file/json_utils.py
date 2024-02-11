import json
import os.path

from utils.file.path_utils import correct_path


def jsonify(data: {}):
    return json.dumps(data, indent=4)


def write_json(data: {}, path):
    if len(data) == 0:
        return

    with open(correct_path(path), 'w') as file:
        # formatted = str(pprint.PrettyPrinter(indent=4, width=80, compact=False))
        # file.write(formatted)
        file.write(
            json.dumps(data, indent=4, sort_keys=False)
        )


def read_json(path) -> {}:
    path = correct_path(path)
    if not os.path.exists(path):
        return None

    with open(path, 'r') as file:
        data = json.load(file)

    return data
