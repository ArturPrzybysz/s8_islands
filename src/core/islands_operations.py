import functools
import sys
from pathlib import Path

from src.utils.types import LAND

sys.setrecursionlimit(100)


class IslandSolver:
    def __init__(self, islands: list[list[bool]]):
        self.islands = islands
        self.row_count = len(islands)
        self.col_count = len(islands[0])
        self.dfs_directions = [(-1, -1), (-1, 0), (-1, 1),
                               (0, -1), (0, 1),
                               (1, -1), (1, 0), (1, 1)]
        self.visited = [[False for _ in range(self.col_count)] for _ in range(self.row_count)]

    def _should_visit(self, x: int, y: int, visited: list[list[bool]]) -> bool:
        if not (0 <= x < self.row_count and 0 <= y < self.col_count):
            return False
        should_be_visited = not visited[x][y] and self.islands[x][y] == LAND
        return should_be_visited

    # @functools.lru_cache(maxsize=1000)
    def _dfs(self, x: int, y: int):
        stack = [(x, y)]

        while len(stack):
            x_i, y_i = stack[-1]
            stack.pop()
            self.visited[x_i][y_i] = True

            for dx, dy in self.dfs_directions:
                new_x = x_i + dx
                new_y = y_i + dy
                if self._should_visit(new_x, new_y, self.visited):
                    stack.append((new_x, new_y))

    def count_islands(self, ) -> int:
        """
        :return: number of islands found
        """
        island_count = 0

        for x in range(self.row_count):
            for y in range(self.col_count):
                if not self.visited[x][y] and self.islands[x][y] == LAND:
                    self._dfs(x, y)
                    island_count += 1

        return island_count


def count_islands_capped_memory(file_path: Path) -> int:
    return -1
