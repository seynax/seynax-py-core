from .file_utils import *


class FileListener:
    def __init__(self, file_path: str):
        self.path = file_path
        self.info = None

    def has_change(self) -> bool:
        self.info = file_info(self.path, self.info)
        return self.info['has_changed']

    def do_it_if_has_changed(self, function):
        if self.has_change():
            function(self)
            return True
        return False
