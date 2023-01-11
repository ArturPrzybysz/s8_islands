import pytest

from src.adapters.read_file import read_island_file, read_island_file_at_position
from tests import ASSETS_PATH


@pytest.mark.parametrize("island_file_path", [
    ASSETS_PATH / "islands0",
    ASSETS_PATH / "islands1",
    ASSETS_PATH / "islands2",
    ASSETS_PATH / "islands3",
    ASSETS_PATH / "islands4",
    ASSETS_PATH / "islands5",
])
def test_read_island_correct_files(island_file_path):
    # TODO: more thorough tests, in which specific file content is asserted.
    content = read_island_file(island_file_path)
    assert len({len(c) for c in content}) == 1


@pytest.mark.parametrize("island_file_path", [
    (ASSETS_PATH / "islands1"),
    (ASSETS_PATH / "islands2"),
    (ASSETS_PATH / "islands3"),
])
def test_read_island_file_at_position(island_file_path):
    # Test if the output of the `read_island_file` and `read_island_file_at_position` are the same.
    file_content = read_island_file(island_file_path)
    for y, line in enumerate(file_content):
        for x, expected_value in enumerate(line):
            value_at_position = read_island_file_at_position(island_file_path, x, y)
            assert expected_value == value_at_position
