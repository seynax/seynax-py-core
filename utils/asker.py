from typing import List, Dict

from pygments                       import highlight, lexers, formatters

from .attributes                    import dict_utils
from .attributes.attribute_utils    import non_none
from .attributes.string_utils       import non_blank, blank
from .file.json_utils               import jsonify
from .name_utils                    import message_of, name_of
from .terminal.color_utils          import colorize
from .terminal.print_utils          import print_color
from .translate_utils               import translate


def value_is_yes(value: str):
    return not blank(value) and (value.lower() == 'yes' or value.lower() == 'y')


class Asker:
    def __init__(self):
        self.configuration  = {}
        self.current_dict   = None

    def start_section(self, name: str = None, message: str = None) -> {}:
        message = non_none(message, message_of(name))
        name    = non_blank(name, name_of(message), '_' + str(len(self.configuration)))
        print_color('\033[92m', message)

        self.current_dict   = {}
        dict_utils.put_if_exists(name, self.configuration, self.current_dict)
        self.configuration[name] = self.current_dict

        return self.current_dict

    def make_message(self, name: str = None, default_value: str = None, message: str = None, output_dict: {} = None, *appends: str) -> str:
        message = non_none(message, message_of(name) + ' ?')
        for append in appends:
            message += append
        message = translate(message, output_dict)
        message = colorize('\033[92m', message)
        if default_value is not None:
            message += ' (' + colorize('\033[96m', f'Default : {default_value}') + ') '
        message += ' : '
        return message

    def ask(self, name: str = None, default_value: str = None, message: str = None, output_dict: {} = None):
        _dict    = non_none(output_dict, self.current_dict)

        default_value = translate(default_value, _dict)
        if name in _dict:
            default_value = non_none(_dict[name], default_value)

        message = self.make_message(name, message, default_value, _dict)

        name    = non_blank(name, name_of(message), '_' + str(len(self.configuration)))

        value = non_blank(input(message), default_value)

        _dict[name] = value

        return value

    def ask_yes_no(self, name: str = None, default_value: str = None, message: str = None, output_dict: {} = None):
        return self.ask(name, default_value, self.make_message(name, message, default_value, non_none(output_dict, self.current_dict), ' (y.yes, n.no) '))

    def stop_section(self, no_print: bool = False) -> [(str, str, {}), (None, None, None)]:
        if self.current_dict is None:
            return None, None, None

        json_settings = jsonify(self.current_dict)
        colored_json = highlight(json_settings, lexers.JsonLexer(), formatters.TerminalFormatter())

        if not no_print:
            print(colored_json)

        return json_settings, colored_json, self.current_dict

    def is_yes(self, name: str) -> bool:
        return value_is_yes(self.get(name))

    def get(self, name: str):
        dict_iterator = self.current_dict
        splits = name.split('.')
        if isinstance(splits, List) and len(splits) > 1:
            for i in range(0, len(splits)):
                split = splits[i]
                if split in dict_iterator:
                    value = dict_iterator[split]
                    if isinstance(value, Dict) and i < len(splits) - 1:
                        dict_iterator = value
                        continue
                    elif isinstance(value, str):
                        return value_is_yes(split)
                    return None
        return self.current_dict.get(name)