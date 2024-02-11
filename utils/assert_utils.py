from utils.terminal.print_utils import print_non_none


def assert_none(value=None, message: str = None):
    if value is None:
        print_non_none(message)
        return True
    return False
