from __future__ import annotations


def get_all(cls, desired_type: type):
    """
        Return all "type" attributes of cls, into dict like attributes[attribute_name] = attribute_value
    """
    attributes = {}

    for attribute_name in dir(cls):
        attribute = getattr(cls, attribute_name)

        if isinstance(attribute, desired_type):
            attributes[attribute_name] = attribute

    return attributes


def non_none(*values):
    if values is None:
        return None

    for value in values:
        if value is None:
            continue
        return value

    return None


def one_none(*values) -> bool:
    if values is None:
        return True

    for value in values:
        if value is None:
            return True
    return False
