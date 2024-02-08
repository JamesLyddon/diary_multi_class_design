from lib.todo import Todo

"""
Test Todo initialises correctly with self.task = task and self.compelte = False by default
"""

def test_initialisation():
    todo = Todo("walk the dog")
    assert todo.task == "walk the dog"
    assert todo.complete == False

"""
Test mark compelte sets the self.complete to True
"""
def test_mark_complete():
    todo = Todo("feed the cat")
    assert todo.complete == False
    todo.mark_complete()
    assert todo.complete == True