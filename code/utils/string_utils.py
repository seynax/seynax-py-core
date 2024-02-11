import re


def is_enclosed_by(value: str, enclose: str) -> bool:
    return value.startswith(enclose) and value.endswith(enclose) and len(value) > 1


def blank(value: str) -> bool:
    """
        Return true if value not none, len > 0 and not contains only white characters
    """
    return not value or re.match('\\s+', value)
