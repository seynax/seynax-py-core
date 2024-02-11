from typing import Dict


def translate(message: str, from_dict: {} = None, parent_name: str = None):
    if message is None or from_dict is None:
        return message

    for name, value in from_dict.items():
        if parent_name is not None:
            absolute_name = parent_name + '.' + name
        else:
            absolute_name = name

        if isinstance(value, str):
            message = message.replace('%' + absolute_name + '%', value)
        elif isinstance(value, Dict):
            message = translate(message, value, absolute_name)
        else:
            message = message.replace('%' + absolute_name + '%', str(value))

    return message
