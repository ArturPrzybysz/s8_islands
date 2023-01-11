import pytest

from src.adapters.read_file import read_island_file
from src.core.islands_operations import IslandSolver, count_islands_capped_memory
from tests import ASSETS_PATH


@pytest.mark.parametrize("file_path, expected_island_count", [
    (ASSETS_PATH / "islands0", 0),
    (ASSETS_PATH / "islands1", 1),
    (ASSETS_PATH / "islands2", 1),
    (ASSETS_PATH / "islands3", 3),
    (ASSETS_PATH / "islands4", 5),
    (ASSETS_PATH / "islands5", 1),
])
def test_count_islands(file_path, expected_island_count):
    islands = read_island_file(file_path)
    count: int = IslandSolver(islands).count_islands()
    assert count == expected_island_count


@pytest.mark.parametrize("file_path, expected_island_count", [
    (ASSETS_PATH / "islands0", 0),
    (ASSETS_PATH / "islands1", 1),
    (ASSETS_PATH / "islands2", 1),
    (ASSETS_PATH / "islands3", 2),
    (ASSETS_PATH / "islands4", 5),
    (ASSETS_PATH / "islands5", 1),
])
def test_count_islands_capped_memory(file_path, expected_island_count):
    count: int = count_islands_capped_memory(file_path)
    assert count == expected_island_count
