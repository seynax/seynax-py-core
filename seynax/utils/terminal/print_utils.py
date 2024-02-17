from typing import Iterable, List

from utils.attributes.attribute_utils import non_none
from utils.terminal.color_utils import colorize


def print_iterable_binary(elements: Iterable, start: str = ''):
    for element in elements:
        if isinstance(element, List):
            print_iterable_binary(element, start + '\t')
            continue

        if isinstance(element, str):
            print(start + "- " + element)
            continue

        print_to_str(start + "- ", element)


def print_to_str(element, start: str = ''):
    print(start + str(element))


def print_non_none(message: str = None):
    if message is None:
        return

    print(message)


def print_color(color: str = None, message: str = None):
    if color is None or message is None:
        return

    print(colorize(color, non_none(message, '')))
