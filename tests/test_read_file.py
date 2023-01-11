import pytest

from src.adapters.read_file import read_island_file, read_island_file_at_position
from src.utils.types import WATER, LAND
from tests import ASSETS_PATH


@pytest.mark.parametrize("bad_island_file_path", [
    ASSETS_PATH / "bad_islands1",
    ASSETS_PATH / "bad_islands2",
    ASSETS_PATH / "non-existent-file"
])
def test_read_island_file_throws(bad_island_file_path):
    with pytest.raises(RuntimeError):
        read_island_file(bad_island_file_path)


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


@pytest.mark.parametrize("island_file_path, x, y, expected_value", [
    (ASSETS_PATH / "islands1", 0, 0, WATER),
    (ASSETS_PATH / "islands1", 1, 1, LAND),
    (ASSETS_PATH / "islands1", 2, 2, WATER),
])
def test_read_island_file_at_position(island_file_path, x, y, expected_value):
    assert read_island_file_at_position(island_file_path, x, y) == expected_value
