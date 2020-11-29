# Third party imports
import pytest


def test_print_hi(capsys):
    # Local application imports
    from app.main import print_hi

    # Happy flow
    name = "Chris"
    print_hi(name)
    captured = capsys.readouterr()
    assert captured.out.startswith(f"Hi, {name} it is currently")

    # Invalid type
    name = 1
    with pytest.raises(TypeError):
        print_hi(name)

    # Invalid length
    name = ""
    with pytest.raises(ValueError):
        print_hi(name)
