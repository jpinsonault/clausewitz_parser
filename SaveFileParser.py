import re


class SaveFileParser(object):
    """Lets you access the save file like a python object"""
    def __init__(self, save_file):
        super(SaveFileParser, self).__init__()
        self.save_file = save_file
        self.file_lines = self.load_file()

        self._nation_size_stats = None

    @property
    def nation_size_stats(self):
        if not self._nation_size_stats:
            self._find_nation_size_stats()
        return self._nation_size_stats

    def load_file(self):
        with open(self.save_file, 'r') as save_file:
            return save_file.readlines()

    def _find_line(self, search):
        for index, line in enumerate(self.file_lines):
            if line.startswith(search):
                return index

    def _find_nation_size_stats(self):
        start_index = self._find_line('nation_size_statistics=')
        
    
class NationSizeStats(object):
    def __init__(self, lines, starting_index):
        super(NationSizeStats, self).__init__()
        self.lines = lines
        self.current_index = starting_index
        
    def next(self):
        ledger_data_y = self._find_line('ledger_data_y', self.current_index)