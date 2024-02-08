from lib.diary_entry import DiaryEntry

"""
Test initialises with instance variables set to arguments as expected
Without a valid phone number in the contents
"""

def test_initialisation_no_phone_number():
    entry = DiaryEntry("Title", "Diary entry contents")
    assert entry.title == "Title"
    assert entry.contents == "Diary entry contents"
    assert entry.length == 3
    assert entry.numbers == []

"""
Test initialises with instance variables set to arguments as expected
With a valid phone number in the contents
"""

def test_initialisation_with_phone_number():
    entry = DiaryEntry("Title", "Diary entry contents 07985581179")
    assert entry.title == "Title"
    assert entry.contents == "Diary entry contents 07985581179"
    assert entry.length == 4
    assert entry.numbers == ["07985581179"]

"""
Test initialises with instance variables set to arguments as expected
With 2 valid phone numbers in the contents
"""

def test_initialisation_with_two_phone_numbers():
    entry = DiaryEntry("Title", "Diary 07984523080 entry contents 07985581179")
    assert entry.title == "Title"
    assert entry.contents == "Diary 07984523080 entry contents 07985581179"
    assert entry.length == 5
    assert entry.numbers == ["07984523080", "07985581179"]

"""
Test read time returns the correct response as an int for minutes (rounded down)
Test expecting non-decimal
"""

def test_read_time():
    entry = DiaryEntry("Title", "one two three four five")
    assert entry.read_time(1) == 5

"""
Test read time returns the correct response as an int for minutes (rounded down)
Test expecting non-decimal
"""

def test_read_time():
    entry = DiaryEntry("Title", "one two three four five")
    assert entry.read_time(2) == 2