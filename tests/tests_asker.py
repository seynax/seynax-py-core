from utils.asker import Asker

asker = Asker()
asker.start_section('new_section')
asker.ask('enabled', None, 'yes')
asker.stop_section()

print(str(asker.configuration))
