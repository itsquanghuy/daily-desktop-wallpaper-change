from main.engines.probe import is_ready


def test_is_ready():
    assert is_ready() is True
