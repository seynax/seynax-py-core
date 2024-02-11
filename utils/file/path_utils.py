import platform


def correct_path(path):
    if not isinstance(path, str):
        path = str(path)

    if 'windows' in platform.system().lower():
        return path.replace('/', '\\')
    if 'linux' in platform.system().lower():
        return path.replace('\\', '/')

    return path


def join_path(from_path, to_path):
    separator = '/'
    if 'windows' in platform.system().lower():
        separator = '\\'

    from_path = correct_path(str(from_path))
    to_path = correct_path(str(to_path))

    if not from_path.endswith(separator) and not to_path.startswith(separator):
        return from_path + separator + to_path

    return from_path + to_path
