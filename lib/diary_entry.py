import re

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.length = len(contents.split())
        self.numbers = re.findall(r'\b0[0-9]{10}\b', contents) # regex stolen from Kay

    def read_time(self, wpm):
        return int(self.length / wpm)