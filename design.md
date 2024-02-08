# Diary Program Design

## User Stories

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

nouns [diary, diary entry, diary entry list, todo list, todo entry, mobile phone list, mobile phone entry]
verbs [read past entries, select best entry for time given]

## Diagram

┌────────────────────────────┐
│ Diary                      │
│                            │
│ - diary entry list         │
│ - todo list                │
│ - phone number list        │
│ + list diary entries       │
│ + list phone numbers       │
│ + list todos               │
│ + get best entry for time  │
│ + (add todo)               │
│ + (list complete)          │
│ + (list incomplete)        │
└────────────────────────────┘
            │        │           
            │        └──────────┐     
            ▼                   │
┌────────────────────────────┐  │
│ Diary Entry                │  │
│                            │  │
│ - title                    │  │
│ - contents                 │  │
│ + estimate read time       │  │
│ + extract phone numbers    │  │
└────────────────────────────┘  │
                                │
                                │ 
                                ▼
                    ┌────────────────────────────┐
                    │ Todo                       │
                    │                            │
                    │ - task                     │
                    │ - complete                 │
                    │ + mark task complete       │
                    └────────────────────────────┘

```python
class Diary:
    def __init__(self):
        self.entries = []
        self.todos = []
        self.contacts = []
    
    def add_entry(self, entry):
        # extract a list of phone numbers from entry
        # append phone numbers to self.contacts (not nested lists)
        self.entries.append(entry)

    def list_entries(self):
        return self.entries

    def get_best_entry_for_time(self, wpm, time):
        pass

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

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.word_count = len(contents.split())
        self.numbers = []

    def read_time(self, wpm):
        pass

class Todo:
    def __init__(self, task)
        self.task = task
        self.complete = False

    def mark_complete(self)
        self.complete = True
```

## Integration Test Examples

"""
Test adding a diary entry and a todo to a new Diary then
Test listing out diary entries and todos
"""


"""
Test adding an entry with a phone number then check the number is listed in contacts
"""

"""
Test adding multiple diary entries then test getting back the appropriate entry based on time constraint
"""

"""
Test adding multiple todos, making some as complete, then listing complete and incomplete todos
"""

## Diary Unit Test Examples

"""
Test Diary class instance initialises with 3 empty lists as expected
"""

## DiaryEntry Unit Test Examples

"""
Test initialises with instance variables set to arguments as expected
Without a valid phone number in the contents
"""

"""
Test initialises with instance variables set to arguments as expected
With a valid phone number in the contents
"""

"""
Test initialises with instance variables set to arguments as expected
With 2 valid phone numbers in the contents
"""

"""
Test reading time returns the correct response as an int for minutes (rounded down)
"""

## Todo Unit Test Examples

"""
Test Todo initialises correctly with self.task = task and self.compelte = False by default
"""

"""
Test mark compelte sets the self.complete to True
"""