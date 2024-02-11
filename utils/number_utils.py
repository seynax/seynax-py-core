from __future__ import annotations

import re
from string_utils import blank


def is_number(value: str) -> bool:
    """
        Verify if value is not blank (see blank method in attribute_utils.py)
        Replace ',' by '.'
        Verify if is number (numeric, digit or decimal)
    """
    if blank(value):
        return False

    _value = value.replace(',', '.')

    return value.isnumeric() or value.isdigit() or value.isdecimal()


def to_number(value: str) -> [None | int | float]:
    """
        Verify if value is not blank (see blank method in attribute_utils.py)
        Replace ',' by '.', remove white characters
        Verify if is number (numeric, digit or decimal)
        If yes return number (int or float) else return None
    """
    if blank(value):
        return None

    _value = value.replace(',', '.').replace(' ', '')
    _value = re.sub('\\s+', '', _value)

    # TODO enable OR disable WARNING
    # TODO terminal colors
    if _value.count('.') > 1:
        print("[WARNING] Number are in incorrect format with multiple '.' !")

    if _value.replace('.', '', 1).isdecimal():
        return float(_value)

    if _value.isnumeric() or _value.isdigit():
        return int(_value)

    return None


def digit_list(number) -> []:
    digits = []
    for digit in str(number):
        if digit.isnumeric():
            digits.append(float(digit))
        else:
            digits.append(digit)

    return digits


def number_count(number) -> int:
    return len(digit_list(number))
