from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.todo import Todo

"""
Test adding a diary entry with a phone number and a todo to a new Diary then
Test listing out diary entries, todos, and contacts
"""

def test_add_entry_with_phone_number_and_todo():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "new phone number is 07985837242")
    entry_2 = DiaryEntry("Title 2", "new phone number is 07985837424")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)
    assert diary.entries == [entry_1, entry_2]
    assert diary.list_entries() == [entry_1, entry_2]
    assert diary.todos == [todo_1, todo_2]
    assert diary.list_todos() == ["walk the dog", "feed the cat"]
    assert diary.contacts == ["07985837242", "07985837424"]
    assert diary.list_contacts() == ["07985837242", "07985837424"]

"""
Test adding multiple todos, making some as complete, then listing complete and incomplete todos
"""

def test_todos_list_functionality():
    diary = Diary()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("feed the cat")
    todo_3 = Todo("buy some milk")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)
    diary.add_todo(todo_3)
    assert diary.list_todos() == ["walk the dog", "feed the cat", "buy some milk"]
    diary.todos[0].mark_complete()
    assert diary.list_complete_todos() == ["walk the dog"]
    assert diary.list_incomplete_todos() == ["feed the cat", "buy some milk"]

"""
Test adding multiple diary entries then test getting back the appropriate entry based on time constraint
"""

def test_best_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "one")
    entry_2 = DiaryEntry("Title", "one two")
    entry_3 = DiaryEntry("Title", "one two three")
    entry_4 = DiaryEntry("Title", "one two three four")
    entry_5 = DiaryEntry("Title", "one two three four five")
    entry_6 = DiaryEntry("Title", "one two three four five six")
    diary.add_entry(entry_3)
    diary.add_entry(entry_5)
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_4)
    diary.add_entry(entry_6)
    assert diary.list_entries() == [entry_3, entry_5, entry_1, entry_2, entry_4, entry_6]
    assert diary.get_best_entry_for_time(1, 1) == entry_1
    assert diary.get_best_entry_for_time(2, 3) == entry_6
    assert diary.get_best_entry_for_time(1, 4) == entry_4
    assert diary.get_best_entry_for_time(1, 10) == entry_6
    assert diary.get_best_entry_for_time(1, 0) == "No suitable entry!"
    assert diary.get_best_entry_for_time(1, 10) == entry_6
    assert diary.get_best_entry_for_time(10, 1) == entry_6