from utils.asker import Asker

ask_dict = {
    'a': {
        'enabled': 'yes',
        'sub': {
            'a.sub': 'coucou',
            'a.sub.sub': {
                'a.sub.sub.sub': 'pas coucou'
            }
        }
    },
    'b': {
        'enabled': 'no'
    }
}

asker = Asker()
print(str(asker.ask_from_dict(ask_dict)))
asker.ask_yes_no('initialize ?')