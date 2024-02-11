from typing import Dict

from utils.attributes.attribute_utils import one_none


def merge(source: {}, destination: {}):
    if source is None or destination is None:
        return None

    for sub_source_name, sub_source_value in source.items():
        if sub_source_name not in destination or not isinstance(sub_source_value, Dict):
            destination[sub_source_name] = sub_source_value
            continue

        sub_destination = destination[sub_source_name]
        if isinstance(sub_destination, Dict):
            destination[sub_source_name] = merge(sub_source_value, destination[sub_source_name])

    return destination


def put_if_exists(name: str = None, from_dict: {} = None, into_dict: {} = None):
    if one_none(name, from_dict, into_dict):
        return

    if name in from_dict:
        into_dict[name] = from_dict[name]
