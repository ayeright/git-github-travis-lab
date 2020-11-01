from msc.rot13 import rot13
from msc.rot13 import rot13_char


def test_rot13_char_non_alpha():
    assert '#' == rot13_char('#')
