import hashlib
import os
import time
import platform


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
    return file_info(file_path).st_size


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
