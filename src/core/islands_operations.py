from pathlib import Path

from src.utils.types import LAND


class IslandSolver:
    # TODO: To improve scalability the self.visited should be replaced with a class that would allow for:
    # 1. in-memory check
    # 2. in-fs check, for example SQLite or just a pickled set.
    # This would overcome the limitation of too big file with a lot of islands running out of memory.

    def __init__(self, islands: list[list[bool]]):
        self.islands = islands
        self.row_count = len(islands)
        self.col_count = len(islands[0])
        self.dfs_directions = [(-1, -1), (-1, 0), (-1, 1),
                               (0, -1), (0, 1),
                               (1, -1), (1, 0), (1, 1)]
        self.visited: set[tuple] = set()

    def _should_visit(self, x: int, y: int, visited: set[tuple]) -> bool:
        if not (0 <= x < self.row_count and 0 <= y < self.col_count):
            return False
        should_be_visited = (x, y) not in visited and self.islands[x][y] == LAND
        return should_be_visited

    def _dfs(self, x: int, y: int):
        stack: list[tuple] = [(x, y)]

        while len(stack):
            x_i, y_i = stack[-1]
            stack.pop()
            self.visited.add((x_i, y_i))

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
                if (x, y) not in self.visited and self.islands[x][y] == LAND:
                    self._dfs(x, y)
                    island_count += 1

        return island_count


def count_islands_capped_memory(file_path: Path) -> int:
    return -1
