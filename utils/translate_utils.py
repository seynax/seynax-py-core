
def translate(value: str, dict: {} = None):
    if value is None or dict is None:
        return value

    for _name, _value in dict.items():
        value = value.replace('%' + _name + '%', _value)

    return value