
def name_of(message: str = None):
    if message is None:
        return ''

    return message.replace(' ', '_').lower()


def message_of(name: str = None):
    if name is None:
        return ''

    return name.replace('_', ' ').capitalize()
