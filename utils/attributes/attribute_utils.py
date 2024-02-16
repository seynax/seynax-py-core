from __future__ import annotations

import inspect
from typing import List, Dict, Union, Tuple

   
# Function to check if casting is possible or not
def can_cast(source_type, dest_type):
    try:
        dest_type(source_type())
        return True
    except ValueError:
        return False


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


def attempt_call_method(method_source, method_name: str, parameters: Union[List, Dict, Tuple] = None, forced_parameters: Union[List, Dict, Tuple] = None, parent = None, unpack: bool = True, force_unpack: bool = False):
    if not hasattr(method_source, method_name):
        return method_source

    return attempt_call(getattr(method_source, method_name), parameters, forced_parameters, parent, unpack, force_unpack)


def attempt_call(_callable, parameters: Union[List, Dict, Tuple] = None, forced_parameters: Union[List, Dict, Tuple] = None, parent = None, unpack: bool = True, force_unpack: bool = False):
    if _callable is None or not callable(_callable):
        return _callable

    if (parameters is None or len(parameters) == 0) and parent is None and (forced_parameters is None or len(forced_parameters) == 0):
        return _callable()

    if isinstance(parameters, List):
        if forced_parameters is not None and isinstance(forced_parameters, List):
            for forced_parameter in forced_parameters:
                parameters.append(forced_parameter)

        return _callable(parameters)
    elif isinstance(forced_parameters, Tuple) or isinstance(parameters, Tuple):
        return _callable(non_none(forced_parameters, parameters))

    allower = None
    source  = None
    if isinstance(parameters, Dict):
        allower = lambda name: name in parameters
        source  = lambda name: parameters[name]
    elif parent is not None:
        if parameters is not None:
            allower = lambda name: hasattr(parent, name) and name in parameters
        else:
            allower = lambda name: hasattr(parent, name)
        source  = lambda name: getattr(parent, name)

    signature = inspect.signature(_callable)
    def attempt_call_with_parameters():
        final_parameters = non_none(parameters, forced_parameters)
        if final_parameters is not None and len(final_parameters) > 0:
            if force_unpack or len(signature.parameters) >= len(final_parameters) and unpack:
                return _callable(**final_parameters)
            return _callable(final_parameters)

        return _callable()

    if allower is None or source is None:
        return attempt_call_with_parameters()

    final_parameters = {}
    if forced_parameters is not None and isinstance(forced_parameters, Dict):
        for name, value in forced_parameters.items():
            final_parameters[name] = value

    for name, value in signature.parameters.items():
        if not allower(name):
            continue
        final_parameters[name] = source(name)

    return attempt_call_with_parameters()
