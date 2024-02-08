class Diary:
    def __init__(self):
        self.entries = []
        self.todos = []
        self.contacts = []

    def add_entry(self, entry):
        self.entries.append(entry)
        self.contacts += entry.numbers

    def list_entries(self):
        return self.entries
    

    def get_best_entry_for_time(self, wpm, minutes):
        available_word_count = wpm * minutes
        longest_viable_count = 0
        longest_viable_entry = None
        for entry in self.entries:
            length = entry.length
            if length == available_word_count:
                return entry
            elif length < available_word_count and entry.length > longest_viable_count:
                longest_viable_count = length
                longest_viable_entry = entry
        if not longest_viable_entry:
            return "No suitable entry!"
        return longest_viable_entry

    def list_contacts(self):
        return self.contacts
    
    def add_todo(self, todo):
        self.todos.append(todo)

    def list_todos(self):
        return [todo.task for todo in self.todos]
    
    def list_complete_todos(self):
        return [todo.task for todo in self.todos if todo.complete]

    def list_incomplete_todos(self):
        return [todo.task for todo in self.todos if not todo.complete]