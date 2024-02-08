from lib.diary import Diary

"""
Test Diary class instance initialises with 3 empty lists as expected
"""

def test_instantiates_with_3_empty_lists():
    diary = Diary()
    assert diary.entries == []
    assert diary.todos == []
    assert diary.contacts == []