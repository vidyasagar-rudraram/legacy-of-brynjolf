import pytest
from room import Room
from brynjolf import Brynjolf
from establishment import establishment
from enlightenment import enlightenment
from util import path_dict, short_distance, find_character_index
from test_base import set_keyboard_input, get_display_output


r = Room('room.txt')
(x, y) = r.brynjolf
b = Brynjolf(r.room, r.brynjolf, r.guards, r.exit)


def test_short_distance():
    assert short_distance(r.brynjolf, r.exit)[0] == 'r'


def find_bynjolf():
    assert find_character_index(r.room, "B") == r.brynjolf

def find_exit():
    assert find_character_index(r.room, "E") == r.exit

def find_guards():
    assert find_character_index(r.room, "G") == r.guards


# @pytest.mark.parametrize(
#     'direction, res', [
#         ('l', 0),
#         ('r', 1),
#         ('u', 1),
#         ('d', 2),
#     ]
# )
def test_enlightenment():
    set_keyboard_input(['l'])
    enlightenment(b)
    output = get_display_output()
    # assert output
