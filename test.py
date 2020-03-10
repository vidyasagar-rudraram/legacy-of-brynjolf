import pytest
from room import Room
from brynjolf import Brynjolf
from establishment import establishment
from enlightenment import enlightenment
from util import path_dict, short_distance, find_character_index
from test_base import set_keyboard_input, get_display_output


def set_room(filename):
    r = Room(filename)
    b = Brynjolf(r.room, r.brynjolf, r.guards, r.exit)
    return r, b


def test_room():
    r, b = set_room('room.txt')
    assert r.room == [[0, 0, 0, 'X'], ['G', 0, 0, 'X'], [0, 'B', 0, 'E'], ['X', 0, 'G', 0]]


@pytest.mark.parametrize(
    'room, brynjolf_exit_guards', [
        ('room.txt', [(2, 1), (2, 3), [(1, 0), (3, 2)]]),
        ('room1.txt', [(2, 1), (1, 3), [(1, 0), (3, 2)]])
    ]
)
def test_brynjolf_exit_guards(room, brynjolf_exit_guards):
    r = Room(room)
    assert r.brynjolf == brynjolf_exit_guards[0]
    assert r.exit == brynjolf_exit_guards[1]
    assert r.guards == brynjolf_exit_guards[2]


@pytest.mark.parametrize(
    'direction, res', [
        ('', 'win: rr'),
        ('l', 'win: rrr'),
        ('r', 'win: r'),
        ('u', 'win: dr'),
        ('d', 'stuck: no way to win'),
    ]
)
def test_enlightenment(direction, res):
    set_keyboard_input([direction])
    r, b = set_room('room.txt')
    enlightenment(b)
    output = get_display_output()[-1]
    assert output == res


@pytest.mark.parametrize(
    'direction, res', [
        ('ludrr', '(lose: executed 2 moves out of 5)'),
        ('rurdr', '(win: executed 3 moves out of 5)'),
        ('uuuuuu', '(undecided: executed 4 moves out of 6)'),
        ('lrlrl', '(undecided: executed 5 moves out of 5)')
    ]
)
def test_establishment(direction, res):
    set_keyboard_input([direction])
    r, b = set_room('room1.txt')
    establishment(b)
    output = get_display_output()[-1]
    assert output == res
