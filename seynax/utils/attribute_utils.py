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


def not_none(value, default):
    if value is None:
        return default

    return value
