def increment_by_one(i):
    while i != 3:
        i += 1
    return i
        
def test_answer():
        assert increment_by_one(1) == 3

def decrement_by_one(i):
    while i != 1:
        i -= 1
    return i

def test_answer1():
    assert decrement_by_one(3) == 1
