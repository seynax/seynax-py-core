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

    def ask(self, name: str = None, default_value: str = None, output_dict: {} = None, message: str = None):
        _dict    = non_none(output_dict, self.current_dict)
        print(self.current_dict)

        default_value = translate(default_value, _dict)
        if name in _dict:
            default_value = non_none(_dict[name], default_value)

        message = non_none(message, message_of(name) + ' ?')
        message = translate(message, _dict)
        message = colorize('\033[92m', message)
        if default_value is not None:
            message += ' (' + colorize('\033[96m', f'Default : {default_value}') + ') '
        message += ' : '

        name    = non_blank(name, name_of(message), '_' + str(len(self.configuration)))

        value = non_blank(input(message), default_value)

        _dict[name] = value

        return value

    def stop_section(self, no_print: bool = False) -> [(str, str, {}), (None, None, None)]:
        if self.current_dict is None:
            return None, None, None

        json_settings = jsonify(self.current_dict)
        colored_json = highlight(json_settings, lexers.JsonLexer(), formatters.TerminalFormatter())

        if not no_print:
            print(colored_json)

        return json_settings, colored_json, self.current_dict

    def is_yes(self, name: str):
        dict_iterator = self.current_dict
        for sub in name.split('.'):
            if sub in dict_iterator:
                dict_iterator = dict_iterator[sub]

        return value_is_yes(name)
