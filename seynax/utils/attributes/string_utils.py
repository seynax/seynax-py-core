import re


def is_enclosed_by(value: str, enclose: str) -> bool:
    return value.startswith(enclose) and value.endswith(enclose) and len(value) > 1


def blank(value: str) -> bool:
    """
        Return true if value not none, len > 0 and not contains only white characters
    """
    return not value or len(value) == 0 or re.match('\s+', value)


def non_blank(*values: str):
    if values is None:
        return None

    for value in values:
        if blank(value):
            continue
        return value

    return None
