
def translate(value: str, from_dict: {} = None):
    if value is None or from_dict is None:
        return value

    for _name, _value in from_dict.items():
        value = value.replace('%' + _name + '%', _value)

    return value
