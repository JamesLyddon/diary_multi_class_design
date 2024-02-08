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
        closest_time = 0
        closest_entry = None
        for entry in self.entries:
            current = entry.read_time(wpm)
            if current == minutes:
                return entry
            elif current < minutes and current > closest_time:
                closest_time = current
                closest_entry = entry
        if not closest_entry:
            return "No suitable entry!"
        return closest_entry

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