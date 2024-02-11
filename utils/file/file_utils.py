import glob
import hashlib
import os
import shutil
import time
import platform
from typing import List

from utils.file.path_utils import correct_path, join_path
from utils.attributes.string_utils import blank


def file_md5(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def file_stats(file_path: str):
    return os.stat(file_path)


def creation_date(file_path: str):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(file_path)
    else:
        stat = os.stat(file_path)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def modification_date(file_path: str):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = file_stats(file_path)
    return time.ctime(mtime)


def bytes_length(file_path: str) -> int:
    return file_info(file_path)['stats'].st_size


def file_info(file_path: str, last_info = None):
    info = {'path': file_path}

    if not os.path.exists(file_path):
        info['exists'] = False
        info['has_changed'] = False
        return info
    stats = file_stats(file_path)
    info['exists'] = True
    info['stats'] = stats
    info['creation_date'] = time.ctime(stats.st_ctime)
    info['modification_date'] = time.ctime(stats.st_mtime)
    info['md5'] = file_md5(file_path)

    if last_info is None:
        info['has_changed'] = True
    elif not last_info['exists']:
        info['has_changed'] = True
    elif info['modification_date'] != last_info['modification_date']:
        info['has_changed'] = True
    elif info['creation_date'] != last_info['creation_date']:
        info['has_changed'] = True
    elif info['md5'] != last_info['md5']:
        info['has_changed'] = True
    else:
        info['has_changed'] = False

    return info


def find_first_file(patterns: [str, [str]], default: str = None, directory: str = None):
    if isinstance(patterns, List):
        for pattern in patterns:
            find = find_first_file(pattern, default)
            if not blank(find) and find != default:
                return find
        return default

    finds = glob.glob(join_path(directory, patterns))

    find = None
    if len(finds) > 0:
        find = finds[0]

    if blank(find):
        find = default

    return find


def make_folder_if_not_exists(path: str):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)


def copy_all(from_path, to_path):
    from_path = correct_path(from_path)
    to_path = correct_path(to_path)

    if not os.path.exists(from_path):
        return

    from_is_file = os.path.isfile(from_path)

    if not from_is_file:
        if os.path.exists(to_path) and os.path.isfile(to_path):
            return
        make_folder_if_not_exists(to_path)

        files = os.listdir(from_path)
        for file in files:
            copy_all(join_path(from_path, file), join_path(to_path, file))
        return

    shutil.copy2(from_path, to_path)
